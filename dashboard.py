import streamlit as st
import pandas as pd
from bokeh.models import DatetimeTickFormatter, ColumnDataSource
from bokeh.plotting import figure
from bokeh.palettes import Category20
from bokeh.models import HoverTool

# Load & preprocess
df = pd.read_csv("https://raw.githubusercontent.com/sanfla/Coffee-shop-analysis/refs/heads/main/Project.csv")
df['transaction_datetime'] = pd.to_datetime(df['transaction_date'] + ' ' + df['transaction_time'], dayfirst=True)
df['date'] = df['transaction_datetime'].dt.date
df['Month Name'] = df['transaction_datetime'].dt.strftime('%B')
df.sort_values('transaction_datetime', inplace=True)

st.set_page_config(layout="wide")
st.title("📊 Coffee Shop Dashboard")

# Sidebar Buat Filter
st.sidebar.header("🔍 Filters")
store_option = st.sidebar.selectbox("Store Location", ['All'] + sorted(df['store_location'].unique()))

# Slider Buat Tanggal
ordered_months = ["January", "February", "March", "April", "May", "June"]
month_option = st.sidebar.select_slider(
    "Select Month",
    options=["All"] + ordered_months,
    value="All"
)

# Filternya
df_filtered = df.copy()
if store_option != 'All':
    df_filtered = df_filtered[df_filtered['store_location'] == store_option]
if month_option != 'All':
    df_filtered = df_filtered[df_filtered['Month Name'] == month_option]

# Metrics Kotak 
avg_order = df_filtered['Total_Bill'].sum() / df_filtered['transaction_id'].nunique() if df_filtered['transaction_id'].nunique() > 0 else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Orders", f"{df_filtered['transaction_id'].nunique():,}", border=True)
col2.metric("Total Revenue", f"${df_filtered['Total_Bill'].sum():,.2f}", border=True)
col3.metric("Total Products", f"{df_filtered['transaction_qty'].sum():,}", border=True)
col4.metric("Avg Order Revenue", f"${avg_order:.2f}", border=True)

# Plot 1: Daily Revenue
st.markdown("### 💵 Daily Revenue Trend")
daily_revenue = df_filtered.groupby('date')['Total_Bill'].sum().reset_index()
if daily_revenue.empty:
    daily_revenue = pd.DataFrame({'date': [pd.Timestamp.today().date()], 'Total_Bill': [0]})

source_daily = ColumnDataSource(daily_revenue)
p_daily = figure(x_axis_type="datetime", title="Daily Revenue", height=350,
                 tools="pan,wheel_zoom,reset,hover",
                 tooltips=[("Date", "@date{%F}"), ("Revenue", "@Total_Bill{$0,0.00}")])
p_daily.line(x='date', y='Total_Bill', source=source_daily, line_width=2, color=Category20[20][2])
p_daily.xaxis.axis_label = "Date"
p_daily.yaxis.axis_label = "Revenue ($)"
p_daily.xaxis.formatter = DatetimeTickFormatter(days="%b %d")
st.bokeh_chart(p_daily, use_container_width=True)

# KOLOM PLOT 2, 3, 4
col_plot2, col_plot3, col_plot4 = st.columns(3)

# Plot 2: Revenue by Month
with col_plot2:
    st.markdown("#### 📆 Monthly Revenue")
    ordered_months = ["January", "February", "March", "April", "May", "June"]
    df_filtered['Month Name'] = pd.Categorical(df_filtered['Month Name'], categories=ordered_months, ordered=True)

    month_rev = df_filtered.groupby('Month Name')['Total_Bill'].sum().reindex(ordered_months).fillna(0).reset_index()
    source_month = ColumnDataSource(month_rev)
    p_month = figure(x_range=month_rev['Month Name'].tolist(), title="Revenue by Month", height=300,
                     tools="hover", tooltips="@{Month Name}: @$Total_Bill{$0,0.00}")
    p_month.vbar(x='Month Name', top='Total_Bill', source=source_month, width=0.6, color=Category20[20][4])
    p_month.xaxis.major_label_orientation = 1.0
    p_month.yaxis.axis_label = "Revenue ($)"
    st.bokeh_chart(p_month, use_container_width=True)

# Plot 3: Product Category Sales Percentage
with col_plot3:
    st.markdown("#### 🏷️ Product Category Sales (%)")
    category_pct = df_filtered['product_category'].value_counts(normalize=True).mul(100).round(2)
    if category_pct.empty:
        cat_df = pd.DataFrame({'category': ['No Data'], 'percent': [100]})
    else:
        cat_df = pd.DataFrame({'category': category_pct.index, 'percent': category_pct.values})
    source_cat = ColumnDataSource(cat_df)
    p_cat = figure(x_range=cat_df['category'].tolist(), title="Category Share", height=300,
                   tools="hover", tooltips="@category: @percent%")
    p_cat.vbar(x='category', top='percent', width=0.5, source=source_cat, color=Category20[20][6])
    p_cat.yaxis.axis_label = "Percentage (%)"
    p_cat.xaxis.major_label_orientation = 1.0
    st.bokeh_chart(p_cat, use_container_width=True)

# Plot 4: Pie Chart - Size Distribution
with col_plot4:
    st.markdown("#### 🥤 Sales Distribution by Size (%)")
    size_count = df_filtered['Size'].value_counts()
    if size_count.empty:
        size_df = pd.DataFrame({
            'size': ['No Data'],
            'count': [1],
            'percent': [100],
            'angle': [2 * 3.1416],
            'color': ['#eeeeee'],
            'start_angle': [0],
            'end_angle': [2 * 3.1416]
        })
    else:
        size_df = pd.DataFrame({
            'size': size_count.index,
            'count': size_count.values
        })
        size_df['percent'] = (size_df['count'] / size_df['count'].sum() * 100).round(2)
        size_df['angle'] = size_df['percent'] / 100 * 2 * 3.1416
        size_df['color'] = Category20[len(size_df)]
        size_df['start_angle'] = size_df['angle'].cumsum().shift(fill_value=0)
        size_df['end_angle'] = size_df['angle'].cumsum()

    source_size = ColumnDataSource(size_df)
    p_size = figure(height=300, title="Size Share", toolbar_location=None,
                    tools="hover", tooltips="@size: @percent%", x_range=(-0.5, 1.0))
    p_size.wedge(x=0, y=1, radius=0.4,
                 start_angle='start_angle', end_angle='end_angle',
                 line_color="white", fill_color='color',
                 legend_field='size', source=source_size)
    p_size.axis.visible = False
    p_size.grid.visible = False
    st.bokeh_chart(p_size, use_container_width=True)

# Plot 5: Top 10 Best-Selling Products
st.markdown("### 🥇 Top 10 Best-Selling Products")
top_products = (
    df_filtered.groupby('product_type')['transaction_qty']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
if top_products.empty:
    top_products = pd.DataFrame({'product_type': ['No Data'], 'transaction_qty': [0]})

source_top = ColumnDataSource(top_products)
p_top = figure(x_range=top_products['product_type'].tolist(),
               height=350, title="Top 10 Best-Selling Products",
               tools="hover", tooltips="@product_type: @transaction_qty units")

p_top.vbar(x='product_type', top='transaction_qty', width=0.6, source=source_top, color=Category20[20][8])
p_top.xaxis.major_label_orientation = 1.0
p_top.yaxis.axis_label = "Units Sold"
st.bokeh_chart(p_top, use_container_width=True)
