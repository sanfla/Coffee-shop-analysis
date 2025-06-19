# 📊 Coffee Shop Analysis Dashboard

Selamat datang di proyek **Coffee Shop Analysis**!  
Dashboard ini dikembangkan menggunakan **Streamlit** dan **Bokeh** untuk memberikan visualisasi interaktif terhadap data penjualan sebuah coffee shop. Proyek ini bertujuan untuk memudahkan pemilik bisnis atau analis data dalam memahami tren penjualan harian, kategori produk, ukuran minuman, dan produk terlaris.

🔗 **Live Demo:** [coffee-shop-dash.streamlit.app](https://coffee-shop-dash.streamlit.app/)

---

## 📁 Dataset

Dataset yang digunakan berasal dari Kaggle:  
📦 [Coffee Shop Sales Dataset – Kaggle](https://www.kaggle.com/datasets/divu2001/coffee-shop-sales-analysis/data)

Dataset ini berisi data transaksi yang mencakup:
- `transaction_date` dan `transaction_time`
- `store_location`, `product_category`, `product_type`
- `Size`, `transaction_qty`, `Total_Bill`

---

## 🚀 Fitur Dashboard

✅ **Filter Interaktif:**
- Filter berdasarkan **Store Location**
- Pilih **Bulan** menggunakan `select_slider`

📊 **Ringkasan Statistik:**
- Total Orders  
- Total Revenue  
- Total Products Sold  
- Average Order Revenue  

📈 **Visualisasi Bokeh:**
1. **💵 Daily Revenue Trend** – Grafik garis tren pendapatan harian  
2. **📆 Monthly Revenue** – Diagram batang pendapatan bulanan  
3. **🏷️ Product Category Sales (%)** – Persentase penjualan berdasarkan kategori  
4. **🥤 Sales Distribution by Size** – Pie chart distribusi ukuran minuman  
5. **🥇 Top 10 Best-Selling Products** – Daftar 10 produk terlaris  

---

## 🛠️ Instalasi Lokal

### 1. Clone repositori ini
```bash
git clone https://github.com/sanfla/Coffee-shop-analysis.git
cd Coffee-shop-analysis

## Kelompok:
1. Bagas Eko Tjahyono Putro
2. Arief Muhammad Usry
3. Ghazy Fadhal Ramadhan
