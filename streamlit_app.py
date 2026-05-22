import streamlit as st
import math

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="ChemAssist Lab", page_icon="🧪", layout="centered")

st.title("🧪 ChemAssist: All-in-One Lab Calculator")
st.write("Aplikasi pembantu praktikum kimia untuk tugas akhir Logika & Pemrograman.")
st.markdown("---")

# --- MEMBUAT NAVIGASI TAB (Fitur yang bikin terlihat lengkap) ---
tab1, tab2, tab3 = st.tabs(["💧 Pembuatan & Pengenceran", "🧬 Kalkulator pH", "📦 Info Bahan Kimia"])

# =========================================================================
# TAB 1: KALKULATOR LARUTAN
# =========================================================================
with tab1:
    st.header("Kalkulator Pembuatan & Pengenceran")
    
    pilihan_sub = st.radio("Pilih Jenis Analisis:", ["Membuat Larutan dari Padatan", "Pengenceran Cairan"])
    
    if pilihan_sub == "Membuat Larutan dari Padatan":
        st.subheader("Hitung Massa yang Harus Ditimbang")
        # Input
        mr = st.number_input("Masukkan Massa Molar / Mr Zat (g/mol):", min_value=0.1, value=40.0, step=0.1)
        molaritas = st.number_input("Molaritas yang Diinginkan (M):", min_value=0.001, value=0.100, format="%.3f")
        volume_ml = st.number_input("Volume Larutan yang Dibuat (mL):", min_value=1.0, value=100.0, step=10.0)
        
        # Logika Rumus: gram = (M * Mr * V_ml) / 1000
        if st.button("Hitung Massa Padatan", key="btn_massa"):
            massa = (molaritas * mr * volume_ml) / 1000
            st.success(f"⚖️ **Massa yang harus ditimbang:** {massa:.4f} gram")
            st.info(f"Cara pembuatan: Timbang {massa:.4f} gram zat, masukkan ke labu takar {volume_ml:.0f} mL, lalu tambahkan akuades hingga tanda batas.")

    else:
        st.subheader("Hitung Volume Pengenceran (M1 x V1 = M2 x V2)")
        # Input
        m1 = st.number_input("Molaritas Larutan Pekat / Stok (M1):", min_value=0.01, value=12.0)
        m2 = st.number_input("Molaritas Larutan yang Diinginkan (M2):", min_value=0.01, value=1.0)
        v2 = st.number_input("Volume Larutan yang Diinginkan (V2) dalam mL:", min_value=1.0, value=100.0)
        
        # Logika Rumus: V1 = (M2 * V2) / M1
        if st.button("Hitung Volume Pekat", key="btn_encer"):
            if m1 <= m2:
                st.error("Molaritas awal (M1) harus lebih besar dari molaritas akhir (M2)!")
            else:
                v1 = (m2 * v2) / m1
                st.success(f"🧪 **Volume larutan pekat yang diambil (V1):** {v1:.2f} mL")
                st.info(f"Cara pembuatan: Pipet {v1:.2f} mL larutan pekat, masukkan ke labu takar, encerkan dengan akuades hingga {v2:.0f} mL.")

# =========================================================================
# TAB 2: KALKULATOR pH
# =========================================================================
with tab2:
    st.header("Kalkulator pH Larutan Kuat")
    st.write("Menghitung pH berdasarkan konsentrasi H+ atau OH-")
    
    jenis_zat = st.selectbox("Jenis Larutan:", ["Asam Kuat (Misal: HCl, H2SO4)", "Basa Kuat (Misal: NaOH, KOH)"])
    valensi = st.number_input("Valensi Zat (Jumlah H+ atau OH- dalam senyawa):", min_value=1, max_value=3, value=1)
    konsentrasi = st.number_input("Konsentrasi Larutan (Molaritas):", min_value=0.0, value=0.0100, format="%.4f")
    
    if st.button("Hitung pH Larutan", key="btn_ph"):
        if konsentrasi <= 0:
            st.error("Konsentrasi harus lebih besar dari 0!")
        else:
            # Logika Kimia & Matematika
            total_konsentrasi = konsentrasi * valensi
            log_nilai = -math.log10(total_konsentrasi)
            
            if "Asam" in jenis_zat:
                ph_akhir = log_nilai
            else:
                ph_akhir = 14 - log_nilai
                
            # Output Visual dengan Metric
            st.metric(label="Nilai pH Akhir", value=f"{ph_akhir:.2f}")
            
            # Logika tambahan untuk indikator warna sederhana
            if ph_akhir < 7:
                st.warning("Sifat Larutan: ASAM")
            elif ph_akhir > 7:
                st.info("Sifat Larutan: BASA")
            else:
                st.success("Sifat Larutan: NETRAL")

# =========================================================================
# TAB 3: INFO BAHAN KIMIA (MSDS MINI)
# =========================================================================
with tab3:
    st.header("Informasi & Simbol Bahaya Bahan Kimia")
    st.write("Pilih bahan kimia untuk melihat rumus, Mr, dan tingkat bahayanya.")
    
    # Logika Python menggunakan Dictionary (Sangat dinilai tinggi di matkul Pemrograman)
    data_bahan = {
        "Akuades (H2O)": {"Formula": "H2O", "Mr": 18.02, "Bahaya": "Aman / Non-Hazardous", "Status": "Normal"},
        "Asam Klorida (HCl)": {"Formula": "HCl", "Mr": 36.46, "Bahaya": "Korosif, Menyebabkan iritasi kulit dan mata berat.", "Status": "Bahaya"},
        "Natrium Hidroksida (NaOH)": {"Formula": "NaOH", "Mr": 40.00, "Bahaya": "Korosif kuat, menyebabkan luka bakar kulit.", "Status": "Bahaya"},
        "Etanol (C2H5OH)": {"Formula": "C2H5OH", "Mr": 46.07, "Bahaya": "Cairan mudah terbakar (Flammable).", "Status": "Bahaya"}
    }
    
    pilihan_bahan = st.selectbox("Pilih Bahan Kimia:", list(data_bahan.keys()))
    
    # Menampilkan info berdasarkan pilihan
    info = data_bahan[pilihan_bahan]
    
    st.subheader(f"Detail: {pilihan_bahan}")
    st.write(f"**Rumus Kimia:** {info['Formula']}")
    st.write(f"**Massa Molar (Mr):** {info['Mr']} g/mol")
    
    if info['Status'] == "Bahaya":
        st.error(f"⚠️ **Peringatan Bahaya:** {info['Bahaya']}")
    else:
        st.success(f"✅ **Keterangan:** {info['Bahaya']}")
