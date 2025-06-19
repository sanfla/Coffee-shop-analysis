# 📊 Coffee Shop Analysis Dashboard

Selamat datang di proyek **Coffee Shop Analysis**!  
Dashboard ini dikembangkan dengan **Streamlit** dan **Bokeh** untuk membantu menganalisis performa penjualan dari sebuah coffee shop berdasarkan data transaksi.

🔗 [Live Demo](#) https://coffee-shop-dash.streamlit.app/

## 📁 Dataset
Dataset digunakan langsung dari file `Project.csv` yang didapat dari kaggle:  
https://www.kaggle.com/datasets/divu2001/coffee-shop-sales-analysis/data

Berisi data transaksi penjualan dengan fitur seperti:
- `transaction_date`, `transaction_time`
- `store_location`, `product_category`, `product_type`
- `Size`, `transaction_qty`, `Total_Bill`

## 🚀 Fitur Dashboard

✅ **Filter Sidebar**  
- Lokasi toko (Store Location)  
- Bulan (Month) menggunakan select slider  

✅ **Key Metrics**  
- Total Orders  
- Total Revenue  
- Total Products Sold  
- Average Order Revenue  

✅ **Visualisasi Interaktif** dengan Bokeh:
1. **💵 Daily Revenue Trend**  
2. **📆 Monthly Revenue**  
3. **🏷️ Product Category Sales (%)**  
4. **🥤 Sales Distribution by Size (Pie Chart)**  
5. **🥇 Top 10 Best-Selling Products**

## 🛠️ Instalasi Lokal

### 1. Clone repo ini
```bash
git clone https://github.com/sanfla/Coffee-shop-analysis.git
cd Coffee-shop-analysis
