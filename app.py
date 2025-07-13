import streamlit as st
from optimizer import optimize_risol

st.set_page_config(page_title="Optimasi Produksi Risol", layout="centered")

st.title("📊 Optimasi Produksi Risol Mayo & Sayur")
st.write("Simulasi ini menggunakan model Linear Programming untuk menentukan jumlah produksi yang memaksimalkan keuntungan.")

if st.button("🔍 Jalankan Optimasi"):
    hasil = optimize_risol()

    if hasil["status"] == "Optimal":
        st.success("✅ Solusi Optimal Ditemukan")
        st.markdown(f"""
        - 🥪 **Jumlah Risol Mayo**: {hasil['risol_mayo']} buah  
        - 🥕 **Jumlah Risol Sayur**: {hasil['risol_sayur']} buah  
        - 💰 **Total Keuntungan Maksimal**: Rp {hasil['total_keuntungan']:,}
        """)
    else:
        st.error("❌ Solusi tidak ditemukan.")
