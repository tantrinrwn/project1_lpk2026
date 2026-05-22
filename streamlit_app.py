import streamlit as st
import math

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Asisten Lab ", page_icon="🧪", layout="centered")

st.title("🧪 Asisten Lab: Lab Kalkulator ")
st.write("Aplikasi komprehensif praktikum kimia untuk tugas akhir Logika & Pemrograman.")
st.markdown("---")

# --- MEMBUAT NAVIGASI TAB ---
tab1, tab2, tab3 = st.tabs(["💧 Pembuatan & Pengenceran", "🧬 Kalkulator pH", "📦 Database Bahan Lab"])

# =========================================================================
# TAB 1: KALKULATOR LARUTAN MULTI-SATUAN
# =========================================================================
with tab1:
    st.header("Kalkulator Larutan (M, N, ppm, %)")
    
    opsi_satuan = st.selectbox("Pilih Satuan Konsentrasi:", ["Molaritas (M)", "Normalitas (N)", "ppm (mg/L)", "Persen Massa (%)"])
    pilihan_sub = st.radio("Pilih Jenis Analisis:", ["Membuat Larutan dari Padatan", "Pengenceran Cairan"], key="sub_tab1")
    
    mr = st.number_input("Massa Molar / Mr Zat (g/mol):", min_value=0.1, value=40.0, step=0.1)
    
    if opsi_satuan == "Normalitas (N)":
        valensi_n = st.number_input("Valensi Zat (Ekivalen H+/OH-/Elektron):", min_value=1, value=1, step=1)

    st.markdown("---")

    if pilihan_sub == "Membuat Larutan dari Padatan":
        st.subheader("Hitung Massa Padatan yang Harus Ditimbang")
        volume_ml = st.number_input("Volume Larutan yang Ingin Dibuat (mL):", min_value=1.0, value=100.0, step=10.0)
        
        if opsi_satuan == "Molaritas (M)":
            c_m = st.number_input("Konsentrasi Molaritas yang Diinginkan (M):", min_value=0.0001, value=0.1000, format="%.4f")
            if st.button("Hitung Massa", key="btn_m_padat"):
                massa = (c_m * mr * volume_ml) / 1000
                st.success(f"⚖️ **Massa Padatan:** {massa:.4f} gram")
                
        elif opsi_satuan == "Normalitas (N)":
            c_n = st.number_input("Konsentrasi Normalitas yang Diinginkan (N):", min_value=0.0001, value=0.1000, format="%.4f")
            if st.button("Hitung Massa", key="btn_n_padat"):
                # BE = Mr / Valensi
                be = mr / valensi_n
                massa = (c_n * be * volume_ml) / 1000
                st.success(f"⚖️ **Massa Padatan:** {massa:.4f} gram")
                
        elif opsi_satuan == "ppm (mg/L)":
            c_ppm = st.number_input("Konsentrasi ppm yang Diinginkan (mg/L):", min_value=0.1, value=100.0)
            if st.button("Hitung Massa", key="btn_ppm_padat"):
                # ppm = mg / L -> massa (g) = (ppm * V_L) / 1000
                massa = (c_ppm * (volume_ml / 1000)) / 1000
                st.success(f"⚖️ **Massa Padatan:** {massa:.4f} gram ({massa*1000:.2f} mg)")
                
        elif opsi_satuan == "Persen Massa (%)":
            c_persen = st.number_input("Persen Massa Zat yang Diinginkan (% w/w):", min_value=0.01, max_value=100.0, value=5.0)
            rho = st.number_input("Massa Jenis Pelarut/Larutan (g/mL) [Default Air = 1.0]:", min_value=0.1, value=1.0, format="%.2f")
            if st.button("Hitung Massa", key="btn_pct_padat"):
                massa_total_larutan = volume_ml * rho
                massa = (c_persen / 100) * massa_total_larutan
                st.success(f"⚖️ **Massa Padatan:** {massa:.4f} gram")
                st.info(f"Larutkan {massa:.4f} g zat ke dalam {massa_total_larutan - massa:.2f} g pelarut.")

    else:
        st.subheader("Hitung Volume Pengenceran (C1 x V1 = C2 x V2)")
        c1 = st.number_input("Konsentrasi Larutan Pekat / Stok (C1):", min_value=0.0001, value=10.0, format="%.4f")
        c2 = st.number_input("Konsentrasi Larutan Hasil Pengenceran (C2):", min_value=0.0001, value=1.0, format="%.4f")
        v2 = st.number_input("Volume Larutan Hasil Pengenceran (V2) dalam mL:", min_value=1.0, value=100.0)
        
        if st.button("Hitung Volume Pekat", key="btn_pengenceran"):
            if c1 <= c2:
                st.error("Konsentrasi awal (C1) harus lebih besar dari konsentrasi akhir (C2)!")
            else:
                v1 = (c2 * v2) / c1
                st.success(f"🧪 **Volume larutan pekat yang diambil (V1):** {v1:.2f} mL")
                st.info(f"Encerkan {v1:.2f} mL stok hingga tanda batas labu takar {v2:.0f} mL.")

# =========================================================================
# TAB 2: KALKULATOR pH
# =========================================================================
with tab2:
    st.header("Kalkulator pH Larutan")
    
    kategori = st.selectbox("Kategori Larutan:", ["Asam Kuat", "Basa Kuat", "Asam Lemah", "Basa Lemah"])
    konsentrasi_ph = st.number_input("Konsentrasi Larutan (Molaritas):", min_value=1e-6, value=0.0100, format="%.5f")
    
    if "Kuat" in kategori:
        valensi_ph = st.number_input("Valensi Larutan (Jumlah H+ atau OH-):", min_value=1, max_value=3, value=1)
    else:
        # Jika asam/basa lemah, butuh nilai konstanta disosiasi Ka atau Kb
        label_k = "Ka (Konstanta Asam)" if "Asam" in kategori else "Kb (Konstanta Basa)"
        k_value = st.number_input(f"Masukkan Nilai {label_k}:", min_value=1e-10, max_value=1.0, value=1.8e-5, format="%.2e")

    if st.button("Hitung Nilai pH", key="btn_hitung_ph"):
        if "Asam Kuat" == kategori:
            h_plus = konsentrasi_ph * valensi_ph
            ph_akhir = -math.log10(h_plus)
        elif "Basa Kuat" == kategori:
            oh_min = konsentrasi_ph * valensi_ph
            poh = -math.log10(oh_min)
            ph_akhir = 14 - poh
        elif "Asam Lemah" == kategori:
            # Rumus: [H+] = sqrt(Ka * M)
            h_plus = math.sqrt(k_value * konsentrasi_ph)
            ph_akhir = -math.log10(h_plus)
        elif "Basa Lemah" == kategori:
            # Rumus: [OH-] = sqrt(Kb * M)
            oh_min = math.sqrt(k_value * konsentrasi_ph)
            poh = -math.log10(oh_min)
            ph_akhir = 14 - poh
            
        st.metric(label=f"Hasil Analisis pH ({kategori})", value=f"{ph_akhir:.2f}")
        
        # Logika Kondisional Karakteristik Sifat
        if ph_akhir < 3: st.error("Sifat Larutan: ASAM KUAT 🟥")
        elif ph_akhir < 7: st.warning("Sifat Larutan: ASAM LEMAH 🟨")
        elif ph_akhir == 7: st.success("Sifat Larutan: NETRAL 🟩")
        elif ph_akhir <= 11: st.info("Sifat Larutan: BASA LEMAH 🟦")
        else: st.error("Sifat Larutan: BASA KUAT 🟪")

# =========================================================================
# TAB 3: DATABASE BAHAN LAB
# =========================================================================
with tab3:
    st.header("Database Bahan Kimia Laboratorium")
    st.write("Daftar referensi sifat dan klasifikasi bahaya GHS bahan kimia.")
    
    # Penambahan variasi bahan laboratorium populer
    data_bahan = {
        "Akuades (H2O)": {"Formula": "H2O", "Mr": 18.02, "Sifat": "Pelarut universal, netral.", "Bahaya": "Aman / Non-Hazardous", "Status": "Aman"},
        "Asam Klorida (HCl)": {"Formula": "HCl", "Mr": 36.46, "Sifat": "Asam kuat, cairan beruap cair.", "Bahaya": "Korosif, iritasi saluran pernapasan.", "Status": "Bahaya"},
        "Natrium Hidroksida (NaOH)": {"Formula": "NaOH", "Mr": 40.00, "Sifat": "Basa kuat, padatan pelet putih, higroskopis.", "Bahaya": "Korosif berat, menyebabkan luka bakar parah.", "Status": "Bahaya"},
        "Etanol (C2H5OH)": {"Formula": "C2H5OH", "Mr": 46.07, "Sifat": "Pelarut organik, mudah menguap.", "Bahaya": "Cairan mudah terbakar (Flammable).", "Status": "Bahaya"},
        "Asam Asetat (CH3COOH)": {"Formula": "CH3COOH", "Mr": 60.05, "Sifat": "Asam lemah, berbau menyengat tajam (cuka).", "Bahaya": "Korosif pada konsentrasi pekat, cairan mudah terbakar.", "Status": "Bahaya"},
        "Asam Sulfat (H2SO4)": {"Formula": "H2SO4", "Mr": 98.08, "Sifat": "Asam kuat bervalensi 2, cairan kental berenergi eksotermik tinggi.", "Bahaya": "Sangat korosif, destruktif pada jaringan kulit.", "Status": "Bahaya"},
        "Natrium Klorida (NaCl)": {"Formula": "NaCl", "Mr": 58.44, "Sifat": "Garam dapur, padatan kristal putih.", "Bahaya": "Aman pada konsentrasi normal.", "Status": "Aman"},
        "Aseton (CH3COCH3)": {"Formula": "CH3COCH3", "Mr": 58.08, "Sifat": "Pelarut organik polar, sangat mudah menguap.", "Bahaya": "Sangat mudah terbakar, iritasi mata.", "Status": "Bahaya"},
        "Tembaga(II) Sulfat (CuSO4)": {"Formula": "CuSO4", "Mr": 159.61, "Sifat": "Garam anorganik, umumnya berwarna biru (hidrat).", "Bahaya": "Toksik bagi lingkungan akuatik, berbahaya jika tertelan.", "Status": "Bahaya"},
    }
    
    pilihan_bahan = st.selectbox("Pilih Bahan Kimia:", list(data_bahan.keys()))
    info = data_bahan[pilihan_bahan]
    
    st.subheader(f"🔍 Detail Spesifikasi: {pilihan_bahan}")
    
    # Layout kolom agar rapi
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"🧪 **Rumus Kimia:** {info['Formula']}")
    with col2:
        st.warning(f"⚖️ **Massa Molar (Mr):** {info['Mr']} g/mol")
        
    st.write(f"ℹ️ **Karakteristik Sifat:** {info['Sifat']}")
    
    if info['Status'] == "Bahaya":
        st.error(f"⚠️ **Klasifikasi Bahaya GHS:** {info['Bahaya']}")
    else:
        st.success(f"✅ **Klasifikasi Bahaya GHS:** {info['Bahaya']}")
