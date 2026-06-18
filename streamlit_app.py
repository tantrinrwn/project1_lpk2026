# =========================
# IMPORT LIBRARY
# =========================

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import random
import time
import math
import json
import os
import hashlib
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="ChemAssist Ultra",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================
# USER DATABASE
# =========================

USER_FILE = "users.json"

if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w") as f:
        json.dump({}, f)


def load_users():
    with open(USER_FILE, "r") as f:
        return json.load(f)


def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# =========================
# SESSION STATE
# =========================

default_session = {
    "login": False,
    "username": "",
    "nama": "",
    "menu": "🏠 Home",
    "history": []
}


for key, value in default_session.items():
    if key not in st.session_state:
        st.session_state[key] = value
# ================= PAGE FUNCTIONS =================

def home():
    st.write("Ini halaman home / dashboard")

def larutan():
    st.write("Halaman Larutan")

def ph():
    st.write("Halaman pH")

def info():
    st.write("Halaman Informasi Bahan Kimia")

def analisis():
    st.write("Halaman Analisis Kimia")

def tentang():
    st.write("Halaman Tentang")

# =========================
# GLOBAL STYLE
# =========================

st.markdown("""
<style>

/* ================= BACKGROUND ================= */

.stApp {
    background: linear-gradient(
        135deg,
        #F0F9FF,
        #E0F2FE,
        #BAE6FD,
        #7DD3FC
    );
}

.block-container {
    padding-top: 2rem;
}

/* ================= LOGO ANIMATION ================= */

.logo-container {
    text-align:center;
    margin-bottom:10px;
}

.logo-spin {
    font-size:80px;
    display:inline-block;
    animation: spin 6s linear infinite;
    transform-origin:center;
}

@keyframes spin {
    from {
        transform:rotate(0deg);
    }
    to {
        transform:rotate(360deg);
    }
}
/* ================= LOGIN ================= */

.login-title {
    text-align: center;

    font-size: 58px;
    font-weight: 900;

    color: #1E3A8A;
}


.login-sub {
    text-align: center;

    color: #475569;
    font-size: 18px;

    margin-bottom: 35px;
}


.stTabs {
    background: rgba(255,255,255,0.90);

    backdrop-filter: blur(20px);

    padding: 35px;

    border-radius: 30px;

    box-shadow:
        0 15px 35px rgba(37,99,235,0.18);
}


button[data-baseweb="tab"] {
    font-size: 16px !important;
    font-weight: 700 !important;
}


.login-box-title {
    text-align: center;

    font-size: 28px;
    font-weight: 800;

    color: #2563EB;

    margin-bottom: 20px;
}


/* ================= INPUT ================= */

.stTextInput input {
    background: white !important;

    border-radius: 14px !important;

    border: 1px solid #BFDBFE !important;

    padding: 10px;
}


/* ================= BUTTON ================= */

.stButton button {
    width: 100% !important;

    height: 52px !important;

    border-radius: 15px !important;

    background: white !important;

    color: #2563EB !important;

    border: 1px solid #BFDBFE !important;

    font-size: 16px !important;

    font-weight: 700 !important;

    box-shadow:
        0 6px 15px rgba(37,99,235,0.12) !important;

    transition: 0.3s;
}


.stButton button:hover {

    transform: translateY(-2px);

    background: #EFF6FF !important;
}


/* ================= SIDEBAR ================= */

section[data-testid="stSidebar"] {

    background: rgba(255,255,255,0.55);

    backdrop-filter: blur(20px);

    border-right:
        1px solid rgba(255,255,255,0.4);
}


/* ================= CARD ================= */

.card,
.metric-box,
.feature-card,
.info-box,
.tentang-box {

    border-radius: 25px;

    padding: 25px;

    box-shadow:
        0 10px 25px rgba(37,99,235,0.15);
}


/* ================= METRIC ================= */

.metric-box {

    background:
        rgba(255,255,255,0.75);

    text-align: center;

    backdrop-filter: blur(18px);
}


.metric-box h2 {
    font-size: 40px;

    margin-bottom: 5px;
}


.metric-box h3 {
    font-size: 32px;

    font-weight: 900;

    color: #2563EB;
}


.metric-box p {
    color: #475569;
}


/* ================= FEATURE CARD ================= */

.feature-card {

    background: linear-gradient(
        135deg,
        #3B82F6,
        #2563EB
    );

    min-height: 160px;

    margin-bottom: 20px;
}


.feature-title {

    color: white;

    font-size: 22px;

    font-weight: 800;

    margin-bottom: 10px;
}


.feature-desc {

    color: #E0F2FE;

    line-height: 1.6;
}


/* ================= STATUS CARD ================= */

.card {

    background:
        rgba(255,255,255,0.75);

    backdrop-filter: blur(18px);
}


/* ================= SCROLLBAR ================= */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-thumb {
    background: #60A5FA;
    border-radius: 20px;
}

/* ================= HEADER TITLE ================= */

.main-title {
    text-align: center !important;
    font-size: 64px !important;
    font-weight: 900 !important;

    color: #0B1F5E !important;

    letter-spacing: 2px !important;
    text-transform: uppercase !important;

    margin-top: 5px !important;
    margin-bottom: 8px !important;

    text-shadow: 
        0 4px 15px rgba(11, 31, 94, 0.3) !important;
}

.subtitle {
    text-align: center !important;

    color: #1E3A8A !important;

    font-size: 20px !important;
    font-weight: 500 !important;

    letter-spacing: 1px !important;
}

</style>
""", unsafe_allow_html=True)



# ================= LOGIN PAGE =================

if not st.session_state.login:

    users = load_users()

    # Header Login
    st.markdown("""
    <div class="login-title">
        🧪 ChemAssist Ultra
    </div>

    <div class="login-sub">
        Smart Chemical Analysis Platform
    </div>
    """, unsafe_allow_html=True)


    # Posisi tengah
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        # Tab Login dan Register
        tab1, tab2 = st.tabs([
            "🔐 Sign In",
            "📝 Sign Up"
        ])


        # ================= SIGN IN =================
        with tab1:

            st.markdown("""
            <div class='login-box-title'>
                Welcome Back 👋
            </div>
            """, unsafe_allow_html=True)

            username = st.text_input("Username", key="login_username")
            password = st.text_input("Password", type="password", key="login_password")

            if st.button("🚀 Login", key="btn_login", use_container_width=True):

                username_clean = username.strip().lower()

                user = users.get(username_clean)

                if user:

                    if user["password"] == hash_password(password):

                        user["last_login"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                        users[username_clean] = user
                        save_users(users)

                        st.session_state.login = True
                        st.session_state.username = username_clean
                        st.session_state.nama = user["nama"]

                        st.success("Login berhasil ✅")
                        time.sleep(1)
                        st.rerun()

                    else:
                        st.error("Password salah")

                else:
                    st.error("Username tidak ditemukan")


        # ================= SIGN UP =================
        with tab2:

            st.markdown("""
            <div class='login-box-title'>
                Create Account ✨
            </div>
            """, unsafe_allow_html=True)

            nama = st.text_input("Nama Lengkap", key="signup_nama")
            email = st.text_input("Email", key="signup_email")
            username_baru = st.text_input("Username", key="signup_username")
            password_baru = st.text_input("Password", type="password", key="signup_password")
            konfirmasi = st.text_input("Konfirmasi Password", type="password", key="signup_konfirmasi")

            if st.button("📝 Daftar", key="btn_signup", use_container_width=True):

                username_clean = username_baru.strip().lower()

                # ===== VALIDASI =====
                if not nama or not email or not username_baru or not password_baru:
                    st.warning("Semua data wajib diisi")

                elif password_baru != konfirmasi:
                    st.error("Konfirmasi password tidak cocok")

                elif username_clean in users:
                    st.error("Username sudah digunakan")

                else:

                    users[username_clean] = {
                        "nama": nama,
                        "email": email,
                        "password": hash_password(password_baru),
                        "last_login": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    }

                    save_users(users)

                    st.success("Akun berhasil dibuat 🎉")
                    time.sleep(1)
                    st.rerun()

    st.stop()
    
# ================= SESSION =================

if "direct_menu" not in st.session_state:
    st.session_state["direct_menu"] = "🏠 Home"

if "analisis_selesai" not in st.session_state:
    st.session_state.analisis_selesai = False

# ================= DATA PH =================

data_ph={

"HCl":{"nama":"Asam Klorida","jenis":"Asam kuat","valensi":1,"Mr":36.46},
"H2SO4":{"nama":"Asam Sulfat","jenis":"Asam kuat","valensi":2,"Mr":98.08},
"HNO3":{"nama":"Asam Nitrat","jenis":"Asam kuat","valensi":1,"Mr":63.01},
"HClO4":{"nama":"Asam Perklorat","jenis":"Asam kuat","valensi":1,"Mr":100.46},
"HBr":{"nama":"Asam Bromida","jenis":"Asam kuat","valensi":1,"Mr":80.91},
"HI":{"nama":"Asam Iodida","jenis":"Asam kuat","valensi":1,"Mr":127.91},
"HClO3":{"nama":"Asam Klorat","jenis":"Asam kuat","valensi":1,"Mr":84.46},
"HClO":{"nama":"Asam Hipoklorit","jenis":"Asam lemah","Ka":3e-8,"Mr":52.46},
"CH3COOH":{"nama":"Asam Asetat","jenis":"Asam lemah","Ka":1.8e-5,"Mr":60.05},
"HF":{"nama":"Asam Fluorida","jenis":"Asam lemah","Ka":6.8e-4,"Mr":20.01},
"HCOOH":{"nama":"Asam Format","jenis":"Asam lemah","Ka":1.8e-4,"Mr":46.03},
"H3PO4":{"nama":"Asam Fosfat","jenis":"Asam lemah","Ka":7.5e-3,"Mr":98.00},
"H2CO3":{"nama":"Asam Karbonat","jenis":"Asam lemah","Ka":4.3e-7,"Mr":62.03},
"HCN":{"nama":"Asam Sianida","jenis":"Asam lemah","Ka":4.9e-10,"Mr":27.03},
"H2S":{"nama":"Asam Sulfida","jenis":"Asam lemah","Ka":1e-7,"Mr":34.08},

"NaOH":{"nama":"Natrium Hidroksida","jenis":"Basa kuat","valensi":1,"Mr":40.00},
"KOH":{"nama":"Kalium Hidroksida","jenis":"Basa kuat","valensi":1,"Mr":56.11},
"Ba(OH)2":{"nama":"Barium Hidroksida","jenis":"Basa kuat","valensi":2,"Mr":171.34},
"Ca(OH)2":{"nama":"Kalsium Hidroksida","jenis":"Basa kuat","valensi":2,"Mr":74.09},
"Sr(OH)2":{"nama":"Stronsium Hidroksida","jenis":"Basa kuat","valensi":2,"Mr":121.63},
"LiOH":{"nama":"Litium Hidroksida","jenis":"Basa kuat","valensi":1,"Mr":23.95},
"RbOH":{"nama":"Rubidium Hidroksida","jenis":"Basa kuat","valensi":1,"Mr":102.47},

"NH3":{"nama":"Amonia","jenis":"Basa lemah","Kb":1.8e-5,"Mr":17.03},
"NH4OH":{"nama":"Amonium Hidroksida","jenis":"Basa lemah","Kb":1.8e-5,"Mr":35.05},
"CH3NH2":{"nama":"Metilamina","jenis":"Basa lemah","Kb":4.4e-4,"Mr":31.06},
"C2H5NH2":{"nama":"Etilamina","jenis":"Basa lemah","Kb":5.6e-4,"Mr":45.08},
"C5H5N":{"nama":"Piridina","jenis":"Basa lemah","Kb":1.7e-9,"Mr":79.10},
"Al(OH)3":{"nama":"Aluminium Hidroksida","jenis":"Basa lemah","Kb":1e-9,"Mr":78.00}

}

# ================= DATABASE =================

db={

"HCl":["Asam Klorida","Asam kuat","36.46 g/mol","Korosif","Cairan bening","H-Cl"],
"H2SO4":["Asam Sulfat","Asam kuat","98.08 g/mol","Sangat korosif","Cairan kental","HO-SO2-OH"],
"HNO3":["Asam Nitrat","Asam kuat","63.01 g/mol","Oksidator kuat","Cairan bening","O=N(OH)=O"],
"CH3COOH":["Asam Asetat","Asam lemah","60.05 g/mol","Iritasi kulit","Cairan bening","CH3-COOH"],
"HF":["Asam Fluorida","Asam lemah","20.01 g/mol","Sangat beracun","Cairan bening","H-F"],
"NaOH":["Natrium Hidroksida","Basa kuat","40.00 g/mol","Korosif","Padatan putih","Na-OH"],
"KOH":["Kalium Hidroksida","Basa kuat","56.11 g/mol","Korosif","Padatan putih","K-OH"],
"Ca(OH)2":["Kalsium Hidroksida","Basa kuat","74.09 g/mol","Iritasi","Serbuk putih","Ca-(OH)2"],
"NH3":["Amonia","Basa lemah","17.03 g/mol","Gas beracun","Gas tidak berwarna","NH3"],
"NH4OH":["Amonium Hidroksida","Basa lemah","35.05 g/mol","Iritasi paru","Cairan bening","NH4OH"],

"NaCl":["Natrium Klorida","Garam","58.44 g/mol","Relatif aman","Kristal putih","Na-Cl"],
"KCl":["Kalium Klorida","Garam","74.55 g/mol","Iritasi ringan","Kristal putih","K-Cl"],
"AgNO3":["Perak Nitrat","Garam","169.87 g/mol","Oksidator","Kristal putih","Ag-NO3"],
"CuSO4":["Tembaga Sulfat","Garam","159.61 g/mol","Beracun","Kristal biru","Cu-SO4"],
"FeCl3":["Besi(III) Klorida","Garam","162.20 g/mol","Korosif","Kristal coklat","Fe-Cl3"],
"MgSO4":["Magnesium Sulfat","Garam","120.37 g/mol","Iritasi ringan","Kristal putih","Mg-SO4"],
"Na2CO3":["Natrium Karbonat","Garam basa","105.99 g/mol","Iritasi","Serbuk putih","Na2-CO3"],
"NaHCO3":["Natrium Bikarbonat","Garam basa","84.01 g/mol","Relatif aman","Serbuk putih","Na-HCO3"],
"C2H5OH":["Etanol","Alkohol","46.07 g/mol","Mudah terbakar","Cairan bening","CH3-CH2-OH"],
"CH3OH":["Metanol","Alkohol","32.04 g/mol","Beracun","Cairan bening","CH3-OH"],

"Acetone":["Aseton","Keton","58.08 g/mol","Mudah terbakar","Cairan bening","CH3-CO-CH3"],
"Benzene":["Benzena","Aromatik","78.11 g/mol","Karsinogen","Cairan bening","C6H6"],
"Toluene":["Toluena","Aromatik","92.14 g/mol","Beracun","Cairan bening","C6H5-CH3"],
"Glucose":["Glukosa","Karbohidrat","180.16 g/mol","Relatif aman","Kristal putih","C6H12O6"],
"Sucrose":["Sukrosa","Karbohidrat","342.30 g/mol","Relatif aman","Kristal putih","C12H22O11"],
"Urea":["Urea","Amida","60.06 g/mol","Iritasi ringan","Kristal putih","NH2-CO-NH2"],
"KMnO4":["Kalium Permanganat","Oksidator","158.04 g/mol","Oksidator kuat","Kristal ungu","KMnO4"],
"K2Cr2O7":["Kalium Dikromat","Oksidator","294.18 g/mol","Toksik","Kristal oranye","K2Cr2O7"],
"Pb(NO3)2":["Timbal Nitrat","Garam","331.20 g/mol","Beracun","Kristal putih","Pb(NO3)2"],
"ZnSO4":["Seng Sulfat","Garam","161.44 g/mol","Iritasi","Kristal putih","ZnSO4"],

"Na2SO4":["Natrium Sulfat","Garam","142.04 g/mol","Iritasi ringan","Kristal putih","Na2SO4"],
"HgCl2":["Merkuri(II) Klorida","Garam","271.50 g/mol","Sangat beracun","Kristal putih","HgCl2"],
"CHCl3":["Kloroform","Pelarut","119.38 g/mol","Beracun jika terhirup","Cairan bening","CHCl3"],
"CCl4":["Karbon Tetraklorida","Pelarut","153.82 g/mol","Toksik","Cairan bening","CCl4"],
"H2O2":["Hidrogen Peroksida","Oksidator","34.01 g/mol","Oksidator kuat","Cairan bening","H-O-O-H"],
"NaNO3":["Natrium Nitrat","Garam","85.00 g/mol","Oksidator","Kristal putih","NaNO3"],
"NH4Cl":["Amonium Klorida","Garam","53.49 g/mol","Iritasi","Kristal putih","NH4Cl"],
"NH4NO3":["Amonium Nitrat","Garam","80.04 g/mol","Oksidator","Kristal putih","NH4NO3"],
"CaCO3":["Kalsium Karbonat","Garam","100.09 g/mol","Iritasi ringan","Serbuk putih","CaCO3"],
"MgCl2":["Magnesium Klorida","Garam","95.21 g/mol","Iritasi ringan","Kristal putih","MgCl2"],
"Al2(SO4)3":["Aluminium Sulfat","Garam","342.15 g/mol","Iritasi","Kristal putih","Al2(SO4)3"],
"H3BO3":["Asam Borat","Asam lemah","61.83 g/mol","Iritasi ringan","Kristal putih","B(OH)3"],
"NaClO":["Natrium Hipoklorit","Oksidator","74.44 g/mol","Korosif","Cairan kuning pucat","NaClO"],
"CH3COCH3":["Aseton","Keton","58.08 g/mol","Mudah terbakar","Cairan bening","CH3-CO-CH3"],
"C6H12O6":["Glukosa","Karbohidrat","180.16 g/mol","Relatif aman","Kristal putih","C6H12O6"],
"C12H22O11":["Sukrosa","Karbohidrat","342.30 g/mol","Relatif aman","Kristal putih","C12H22O11"],
"FeSO4":["Besi(II) Sulfat","Garam","151.91 g/mol","Iritasi","Kristal hijau","FeSO4"],
"CuCl2":["Tembaga(II) Klorida","Garam","134.45 g/mol","Beracun","Kristal hijau","CuCl2"],
"Na3PO4":["Natrium Fosfat","Garam basa","163.94 g/mol","Iritasi","Serbuk putih","Na3PO4"],
"KNO3":["Kalium Nitrat","Garam","101.10 g/mol","Oksidator","Kristal putih","KNO3"]

}

# ================= NAVIGATION HELPER =================

def go_to(page_name):
    st.session_state.menu = page_name

if "menu" not in st.session_state:
    st.session_state.menu = "🏠 Home"

# ================= HEADER GLOBAL =================
st.markdown("""

<div class="logo-container">
    <div class="logo-spin">🧪</div>
</div>

<div class="main-title">
ChemAssist Dashboard
</div>

<div class="subtitle">
Sistem Analisis Parameter Laboratorium Kimia Interaktif
</div>

""", unsafe_allow_html=True)

# ================= SIDEBAR =================

with st.sidebar:

    if st.session_state.login:
        st.success(
            f"👤 {st.session_state.nama}"
        )
        
    users = load_users()

    if st.session_state.username in users:

        st.caption(
            f"🕒 Login terakhir: "
            f"{users[st.session_state.username]['last_login']}"
        )

    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False

    dark_mode = st.toggle(
         "🌙 Dark Mode",
        value=st.session_state.dark_mode
     )

    st.session_state.dark_mode = dark_mode

    if dark_mode:
        sidebar_bg = "#0F172A"
        nav_bg = "#1E293B"
        nav_text = "white"
    else:
        sidebar_bg = "#E0F2FE"
        nav_bg = "#FFFFFF"
        nav_text = "#0F172A"

    selected = option_menu(
        menu_title="✨ ChemAssist Menu",

        options=[
            "🏠 Home",
            "💧 Larutan",
            "⚗️ pH",
            "📚 Informasi Bahan Kimia",
            "🧪 Analisis Kimia",
            "ℹ️ Tentang"
        ],

        icons=[
            "house-fill",
            "droplet-fill",
            "eyedropper",
            "book-fill",
            "activity",
            "info-circle-fill"
        ],

        menu_icon="stars",

        default_index=[
            "🏠 Home",
            "💧 Larutan",
            "⚗️ pH",
            "📚 Informasi Bahan Kimia",
            "🧪 Analisis Kimia",
            "ℹ️ Tentang"
        ].index(st.session_state.menu),

        styles={

            "container": {
                "padding": "15px",
                "background-color": sidebar_bg,
                "border-radius": "20px",
            },

            "icon": {
                "color": "#38BDF8",
                "font-size": "20px"
            },

            "nav-link": {
                "font-size": "17px",
                "text-align": "left",
                "margin": "8px",
                "padding": "12px",
                "border-radius": "14px",
                "background-color": nav_bg,
                "color": nav_text,
                "font-weight": "600",
                "--hover-color": "#334155",
            },

            "nav-link-selected": {
                "background": "linear-gradient(90deg,#38BDF8,#2563EB)",
                "color": "white",
                "font-weight": "bold",
            },
        }
    )
    st.session_state.menu = selected

    st.markdown("---")

    if st.button("🚪 Logout"):
        st.session_state.login = False
        st.session_state.username = ""
        st.session_state.nama = ""
        st.rerun()

menu = selected
# ================= DARK MODE =================

if dark_mode:

    st.markdown("""
    <style>

    /* ================= BACKGROUND ================= */

    .stApp{
        background:linear-gradient(
        135deg,
        #020617,
        #0F172A,
        #111827
        ) !important;
    }

    /* ================= SIDEBAR ================= */

    section[data-testid="stSidebar"]{
        background:#0F172A !important;
    }

    section[data-testid="stSidebar"] > div{
        background:#0F172A !important;
    }

    section[data-testid="stSidebar"] *{
        color:white !important;
    }

    /* ChemAssist Menu */

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] h4,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span{
        color:white !important;
    }

    /* ================= CARD ================= */

    .card{
        background:rgba(15,23,42,0.70) !important;
        border:1px solid rgba(255,255,255,0.08) !important;
        color:white !important;
    }

    /* ================= HOME CARD ================= */

    .home-card{
        background:linear-gradient(
        135deg,
        #1E293B,
        #334155
        ) !important;

        border:1px solid rgba(255,255,255,0.08) !important;

        box-shadow:
        0 8px 25px rgba(0,0,0,0.4) !important;
    }

    .home-card h3,
    .home-card p{
        color:white !important;
    }

    /* ================= METRIC ================= */

    .metric-box{
        background:rgba(15,23,42,0.70) !important;
        border:1px solid rgba(255,255,255,0.08) !important;
        color:white !important;
    }

    .metric-box h2{
        color:#38BDF8 !important;
    }

    .metric-box h3{
        color:white !important;
    }

    .metric-box p{
        color:#E2E8F0 !important;
    }

    /* ================= BUTTON ================= */

    .stButton > button{
        background:#1E293B !important;
        color:white !important;
        border:1px solid #334155 !important;
    }

    .stButton > button:hover{
        background:#2563EB !important;
        color:white !important;
    }

    /* ================= INPUT ================= */

    .stTextInput input,
    .stNumberInput input{
        background:#1E293B !important;
        color:white !important;
        border:1px solid #334155 !important;
    }
   .stSelectbox div[data-baseweb="select"]{
        background:#1E293B !important;
    }

    .stSelectbox div[data-baseweb="select"] *{
        color:white !important;
    }

    /* ================= TEXT ================= */

    h1,h2,h3,h4,h5,h6{
        color:white !important;
    }

    p,span,label{
        color:#E2E8F0 !important;
    }

    .main-title{
        color:white !important;
    }

    .subtitle{
        color:#CBD5E1 !important;
    }

    /* ================= INFO ================= */

    .stAlert{
        background:#1E293B !important;
        color:white !important;
    }

    /* ================= TENTANG ================= */

    .tentang-box{
        background:rgba(15,23,42,0.7) !important;
        border:1px solid rgba(255,255,255,0.08) !important;
    }

    .tentang-box *{
        color:white !important;
    }

    /* ================= METRIC ================= */

    [data-testid="stMetric"]{
        background:#1E293B;
        padding:15px;
        border-radius:15px;
        border:1px solid #334155;
    }

    [data-testid="stMetric"] *{
        color:white !important;
    }
    </style>
    """, unsafe_allow_html=True)


menu = st.session_state.menu
# ================= HOME =================

if menu == "🏠 Home":

    st.markdown("<br>", unsafe_allow_html=True)

    # ================= Statistik =================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="metric-box">
            <h2>📚</h2>
            <h3>{len(db)}</h3>
            <p>Database Senyawa</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-box">
            <h2>⚗️</h2>
            <h3>{len(data_ph)}</h3>
            <p>Data pH</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-box">
            <h2>🚀</h2>
            <h3>5.0</h3>
            <p>Modern Edition</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ================= FITUR UTAMA =================

    st.markdown("## 🚀 Fitur Utama")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("💧 Buka Menu Larutan", use_container_width=True):
            go_to("💧 Larutan")

        st.markdown("""
        <div style="
            background:linear-gradient(135deg,#60A5FA,#2563EB);
            height:190px;
            padding:25px;
            border-radius:20px;
            color:white;
            margin-bottom:20px;
            box-shadow:0 8px 20px rgba(37,99,235,0.25);
        ">
            <h3>💧 Smart Solution Maker</h3>
            <p>
            Perhitungan larutan otomatis dengan tampilan modern dan langkah pembuatan larutan yang praktis.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("📚 Informasi Kimia", use_container_width=True):
            go_to("📚 Informasi Bahan Kimia")

        st.markdown("""
        <div style="
            background:linear-gradient(135deg,#60A5FA,#2563EB);
            height:190px;
            padding:25px;
            border-radius:20px;
            color:white;
            margin-bottom:20px;
            box-shadow:0 8px 20px rgba(37,99,235,0.25);
        ">
            <h3>📚 Chemical Database</h3>
            <p>
            Menampilkan informasi senyawa kimia lengkap, sifat, bahaya, dan struktur molekul.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        if st.button("⚗️ Kalkulator pH", use_container_width=True):
            go_to("⚗️ pH")

        st.markdown("""
        <div style="
            background:linear-gradient(135deg,#60A5FA,#2563EB);
            height:190px;
            padding:25px;
            border-radius:20px;
            color:white;
            margin-bottom:20px;
            box-shadow:0 8px 20px rgba(37,99,235,0.25);
        ">
            <h3>⚡ Smart pH Calculator</h3>
            <p>
            Menghitung pH larutan asam dan basa secara cepat dan otomatis.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🧪 Analisis Kimia", use_container_width=True):
            go_to("🧪 Analisis Kimia")

        st.markdown("""
        <div style="
            background:linear-gradient(135deg,#60A5FA,#2563EB);
            height:190px;
            padding:25px;
            border-radius:20px;
            color:white;
            margin-bottom:20px;
            box-shadow:0 8px 20px rgba(37,99,235,0.25);
        ">
            <h3>🧪 Chemical Analysis</h3>
            <p>
            Analisis karakteristik senyawa, reaktivitas, keamanan, dan interpretasi kimia.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ================= LIVE SYSTEM MONITOR =================

    st.markdown("## 🚀 Live System Monitor")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            label="🟢 Status",
            value="ONLINE"
        )

    with c2:
        st.metric(
            label="⚡ Response Time",
            value="0.2 s"
        )

    with c3:
        st.metric(
            label="🧪 Database",
            value=f"{len(db)} Senyawa"
        )

    st.info("🔄 Smart Chemical Engine Running")

    st.success("✅ ChemAssist Ultra Ready")
    
# ================= LARUTAN =================

elif menu == "💧 Larutan":

    st.title("💧 Smart Solution Maker")

    senyawa = st.selectbox(
        "Pilih Senyawa",
        list(data_ph.keys()),
        format_func=lambda x: f"{data_ph[x]['nama']} ({x})"
    )

    info = data_ph[senyawa]

    st.info(f"""
🧪 Nama Senyawa : {info['nama']}

📌 Rumus Kimia : {senyawa}

⚖️ Mr : {info['Mr']} g/mol
""")

    metode = st.selectbox(
        "Pilih Jenis Perhitungan",
        ["Pembuatan Larutan", "Pengenceran"]
    )

    # ================= PEMBUATAN LARUTAN =================

    if metode == "Pembuatan Larutan":

        M = st.number_input(
            "Konsentrasi Larutan (M)",
            min_value=0.0,
            value=0.1
        )

        V = st.number_input(
            "Volume Larutan (mL)",
            min_value=0.0,
            value=100.0
        )

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            if st.button(
                "⬅️ Kembali ke Home",
                use_container_width=True
            ):
                st.session_state.menu = "🏠 Home"
                st.rerun()
        
        with col2:
            hitung = st.button(
                "🧪 Hitung Massa Senyawa",
                use_container_width=True
            )

        if hitung:

            with st.spinner("Sedang menghitung..."):
                time.sleep(3)

            massa = (info['Mr'] * M * V) / 1000

            st.success(f"""
✅ Massa senyawa yang diperlukan:

{massa:.4f} gram
""")

            st.markdown(f"""
            <div style='
            background:rgba(255,255,255,0.7);
            padding:28px;
            border-radius:24px;
            border:1px solid #eee6ff;
            box-shadow:0 5px 18px rgba(200,200,255,.15);
            font-family:Segoe UI;
            color:#5b4b8a;
            line-height:2;
            font-size:18px;
            '>

            <h3 style='
            color:#7c6bb3;
            margin-bottom:18px;
            font-weight:700;
            '>
            🧪 Langkah Pembuatan Larutan
            </h3>

            <div style='font-size:17px;'>

            1️⃣ Timbang <b>{massa:.4f} gram</b> {info['nama']}<br>

            2️⃣ Larutkan dengan sedikit akuades<br>

            3️⃣ Masukkan ke labu takar <b>{V} mL</b><br>

            4️⃣ Tambahkan akuades hingga tanda batas<br>

            5️⃣ Homogenkan larutan

            </div>

            </div>
            """, unsafe_allow_html=True)

      # ================= PENGENCERAN =================

    else:

        M1 = st.number_input("Molaritas Awal (M)", 1.0)
        V1 = st.number_input("Volume Awal (mL)", 100.0)
        M2 = st.number_input("Molaritas Akhir (M)", 0.1)

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            if st.button("⬅️ Kembali ke Home"):
                st.session_state.menu = "🏠 Home"
                st.rerun()

        with col2:
            hitung_pengenceran = st.button(
                "💧 Hitung Pengenceran",
                key="btn_pengenceran",
                use_container_width=True
            )

        if hitung_pengenceran:

            if M2 >= M1:
                st.error("Molaritas akhir harus lebih kecil dari molaritas awal.")

            else:

                with st.spinner("Sedang menghitung..."):
                    time.sleep(3)

                V2 = (M1 * V1) / M2
                volume_air = V2 - V1

                st.success(f"""
✅ Volume akhir larutan:
{V2:.2f} mL
""")

                st.info(f"""
💧 Tambahkan sekitar {volume_air:.2f} mL akuades
ke dalam {V1:.2f} mL larutan stok untuk memperoleh
larutan {M2} M.
""")

                st.markdown(f"""
                <div style='
                background:rgba(255,255,255,0.7);
                padding:28px;
                border-radius:24px;
                border:1px solid #eee6ff;
                box-shadow:0 5px 18px rgba(200,200,255,.15);
                font-family:Segoe UI;
                color:#5b4b8a;
                line-height:2;
                font-size:18px;
                '>

                <h3 style='
                color:#7c6bb3;
                margin-bottom:18px;
                font-weight:700;
                '>
                💧 Langkah Pengenceran Larutan
                </h3>

                <div style='font-size:17px;'>

                1️⃣ Siapkan larutan stok {info['nama']} dengan konsentrasi <b>{M1} M</b><br>

                2️⃣ Pipet <b>{V1:.2f} mL</b> larutan stok<br>

                3️⃣ Masukkan ke dalam labu takar<br>

                4️⃣ Tambahkan akuades hingga volume mencapai <b>{V2:.2f} mL</b><br>

                5️⃣ Homogenkan larutan<br>

                6️⃣ Larutan <b>{M2} M</b> siap digunakan

                </div>

                </div>
                """, unsafe_allow_html=True)
                
# ================= PH =================

elif menu == "⚗️ pH":

    st.title("⚗️ Smart pH Calculator")

    senyawa = st.selectbox(
        "Pilih Senyawa",
        list(data_ph.keys()),
        format_func=lambda x: f"{data_ph[x]['nama']} ({x})"
    )

    info = data_ph[senyawa]

    st.info(f"""
🧪 Nama Senyawa : {info['nama']}

📌 Jenis : {info['jenis']}

⚖️ Mr : {info['Mr']} g/mol
""")

    C = st.number_input(
        "Masukkan Konsentrasi (M)",
        min_value=0.0,
        value=0.01
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ================= TOMBOL =================

    col1, col2 = st.columns(2)

    with col1:
            if st.button("⬅️ Kembali ke Home"):
                st.session_state.menu = "🏠 Home"
                st.rerun()

    with col2:
        hitung_ph = st.button(
            "⚗️ Hitung pH",
            key="btn_ph",
            use_container_width=True
        )

    # ================= PERHITUNGAN =================

    if hitung_ph:

        with st.spinner("Sedang menghitung..."):
            time.sleep(3)

        if "Asam kuat" in info["jenis"]:

            ph = -math.log10(C * info["valensi"])

        elif "Basa kuat" in info["jenis"]:

            poh = -math.log10(C * info["valensi"])
            ph = 14 - poh

        elif "Asam lemah" in info["jenis"]:

            H = math.sqrt(info["Ka"] * C)
            ph = -math.log10(H)

        else:

            OH = math.sqrt(info["Kb"] * C)
            poh = -math.log10(OH)
            ph = 14 - poh

        st.markdown("<br>", unsafe_allow_html=True)

        st.metric(
            "📊 Nilai pH",
            f"{ph:.2f}"
        )

        if ph <= 1:
            st.error("🔴 Sangat Asam")

        elif ph <= 3:
            st.warning("🟠 Asam")

        elif ph <= 6:
            st.info("🟡 Asam Lemah")

        elif ph == 7:
            st.success("🟢 Netral")

        elif ph <= 11:
            st.info("🔵 Basa Lemah")

        elif ph <= 13:
            st.warning("🟣 Basa")

        else:
            st.error("⚫ Sangat Basa")

# ================= INFORMASI BAHAN =================

elif menu == "📚 Informasi Bahan Kimia":

    st.title("📚 Informasi Bahan Kimia")

    # ================= SEARCH =================
    cari = st.text_input("🔎 Cari nama atau rumus senyawa")

    hasil = [
        x for x in db
        if cari.lower() in x.lower()
        or cari.lower() in db[x][0].lower()
    ] if cari else list(db.keys())

    # ================= SELECTBOX =================
    pilih = st.selectbox(
        "Pilih Senyawa",
        hasil,
        key="select_senyawa_info"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ================= BUTTON =================
    col1, col2 = st.columns([1, 1])

    with col1:
        home_btn = st.button(
            "🏠 Kembali ke Home",
            key="btn_home_info",
            use_container_width=True
        )

    with col2:
        tampilkan_info = st.button(
            "📖 Tampilkan Informasi",
            key="btn_info",
            use_container_width=True
        )

    # ================= OUTPUT CARD (HARUS DI DALAM MENU) =================
    if tampilkan_info and pilih:

        data = db[pilih]

        jenis = data[1]
        senyawa = pilih

        st.markdown(f"""
        <div style="
            background:#F8FAFC;
            padding:22px;
            border-radius:16px;
            color:#0F172A;
            box-shadow:0 8px 20px rgba(0,0,0,0.12);
            line-height:1.7;
            border:1px solid #E2E8F0;
        ">

        <h3 style="
            margin-bottom:18px;
            color:#1E3A8A;
            border-bottom:2px solid #1E3A8A;
            padding-bottom:8px;
        ">
        🧪 Informasi Senyawa
        </h3>

        <p><b style="color:#1E3A8A;">Nama Senyawa:</b> {data[0]}</p>
        <p><b style="color:#1E3A8A;">Rumus Kimia:</b> {pilih}</p>
        <p><b style="color:#1E3A8A;">Jenis:</b> {data[1]}</p>
        <p><b style="color:#1E3A8A;">Mr:</b> {data[2]}</p>
        <p><b style="color:#1E3A8A;">Bahaya:</b> {data[3]}</p>
        <p><b style="color:#1E3A8A;">Bentuk/Fisik:</b> {data[4]}</p>
        <p><b style="color:#1E3A8A;">Struktur Molekul:</b> {data[5]}</p>

        </div>
        """, unsafe_allow_html=True)

    # ================= NAVIGATION =================
    if home_btn:
        st.session_state.menu = "🏠 Home"
        st.rerun()
        
# ================= ANALISIS KIMIA =================

elif st.session_state.menu == "🧪 Analisis Kimia":

    st.title("🧪 Smart Chemical Analysis")

    senyawa = st.selectbox(
        "Pilih Senyawa",
        list(db.keys())
    )

    st.markdown("<br>", unsafe_allow_html=True)

    tampilkan_analisis = False

    if not st.session_state.analisis_selesai:

        col1, col2 = st.columns(2)

        with col1:
            if st.button(
                "⬅️ Kembali ke Home",
                key="btn_home_analisis",
                use_container_width=True
            ):
                st.session_state.menu = "🏠 Home"
                st.rerun()

        with col2:
            tampilkan_analisis = st.button(
                "🧪 Analisis Senyawa",
                key="btn_analisis",
                use_container_width=True
            )
            
    if tampilkan_analisis:
        st.session_state.analisis_selesai = True

    if st.session_state.analisis_selesai:
        st.success("ANALISIS SELESAI = TRUE")

        data = db[senyawa]
        jenis = data[1]

        st.markdown("<br>", unsafe_allow_html=True)

        # ================= INTERPRETASI =================

        st.subheader("🧪 Interpretasi Kimia")

        if jenis == "Asam kuat":
            interpretasi = "Asam kuat yang terionisasi hampir sempurna dalam air dan menghasilkan ion H⁺ dalam jumlah besar."

        elif jenis == "Asam lemah":
            interpretasi = "Asam lemah yang hanya terionisasi sebagian dalam air."

        elif jenis == "Basa kuat":
            interpretasi = "Basa kuat yang menghasilkan ion OH⁻ dalam jumlah besar."

        elif jenis == "Basa lemah":
            interpretasi = "Basa lemah yang hanya terionisasi sebagian dalam air."

        elif "Garam" in jenis:
            interpretasi = "Senyawa ionik yang tersusun dari kation dan anion."

        elif jenis == "Alkohol":
            interpretasi = "Mengandung gugus hidroksil (-OH) dan umum digunakan sebagai pelarut."

        elif jenis == "Keton":
            interpretasi = "Mengandung gugus karbonil (>C=O)."

        elif jenis == "Aromatik":
            interpretasi = "Mengandung cincin aromatik yang stabil karena resonansi."

        elif jenis == "Karbohidrat":
            interpretasi = "Merupakan sumber energi penting pada sistem biologis."

        elif jenis == "Amida":
            interpretasi = "Mengandung gugus fungsi amida (-CONH₂)."

        elif jenis == "Pelarut":
            interpretasi = "Digunakan untuk melarutkan berbagai senyawa kimia."

        elif jenis == "Oksidator":
            interpretasi = "Mampu mengoksidasi zat lain dengan menerima elektron."

        else:
            interpretasi = "Karakteristik kimia mengikuti gugus fungsi utamanya."

        st.info(interpretasi)
        st.subheader("🔬 Analisis Spesifik Senyawa")

        analisis_spesifik = {

    "HCl":"Asam kuat yang terionisasi sempurna menghasilkan H⁺ dan Cl⁻. Digunakan sebagai titran dan pengatur pH.",

    "H2SO4":"Asam diprotik kuat dengan sifat dehidrasi tinggi. Banyak digunakan dalam analisis dan industri.",

    "HNO3":"Asam kuat sekaligus oksidator yang mampu mengoksidasi berbagai logam.",

    "HF":"Asam lemah yang sangat berbahaya karena dapat menembus jaringan tubuh.",

    "H3BO3":"Asam lemah yang digunakan sebagai antiseptik dan bahan baku industri.",

    "CH3COOH":"Asam organik lemah yang digunakan dalam sintesis organik dan pembuatan buffer.",

    "NaOH":"Basa kuat yang menghasilkan ion OH⁻ dalam jumlah besar dan bersifat korosif.",

    "KOH":"Basa kuat yang digunakan dalam industri sabun dan baterai.",

    "Ca(OH)2":"Basa kuat yang digunakan dalam pengolahan air dan industri konstruksi.",

    "NH3":"Basa lemah yang membentuk ion amonium dalam air dan digunakan dalam industri pupuk.",

    "NH4OH":"Larutan amonia dalam air yang bersifat basa lemah.",

    "NaCl":"Garam netral yang terdisosiasi menjadi ion Na⁺ dan Cl⁻.",

    "KCl":"Sumber ion kalium yang banyak digunakan dalam pupuk dan laboratorium.",

    "AgNO3":"Digunakan dalam analisis argentometri dan pembentukan endapan halida.",

    "CuSO4":"Sumber ion Cu²⁺ yang digunakan dalam analisis kualitatif dan uji biuret.",

    "FeCl3":"Digunakan sebagai pereaksi identifikasi fenol karena membentuk kompleks berwarna.",

    "MgSO4":"Garam magnesium yang digunakan dalam farmasi dan laboratorium.",

    "Na2CO3":"Garam basa yang digunakan untuk meningkatkan pH larutan.",

    "NaHCO3":"Bereaksi dengan asam menghasilkan gas karbon dioksida.",

    "Pb(NO3)2":"Sumber ion Pb²⁺ yang digunakan dalam berbagai analisis kimia.",

    "ZnSO4":"Sumber ion seng yang digunakan dalam industri dan laboratorium.",

    "Na2SO4":"Garam sulfat yang stabil dan mudah larut dalam air.",

    "HgCl2":"Senyawa merkuri yang sangat toksik dan memerlukan penanganan khusus.",

    "NaNO3":"Garam yang mengandung ion nitrat dan digunakan sebagai bahan baku pupuk.",

    "NH4Cl":"Garam amonium yang digunakan dalam buffer dan pupuk.",

    "NH4NO3":"Sumber nitrogen penting dalam industri pupuk.",

    "CaCO3":"Komponen utama batu kapur dan cangkang organisme.",

    "MgCl2":"Sumber ion magnesium yang mudah larut dalam air.",

    "Al2(SO4)3":"Digunakan sebagai koagulan dalam pengolahan air.",

    "FeSO4":"Sumber ion Fe²⁺ yang digunakan dalam farmasi dan analisis.",

    "CuCl2":"Sumber ion Cu²⁺ yang digunakan dalam sintesis dan analisis kimia.",

    "Na3PO4":"Garam fosfat yang digunakan sebagai pengatur pH dan bahan pembersih.",

    "KNO3":"Garam yang mengandung ion kalium dan nitrat serta digunakan sebagai pupuk.",

    "KMnO4":"Oksidator kuat yang digunakan pada titrasi permanganometri.",

    "K2Cr2O7":"Oksidator kuat yang digunakan pada titrasi redoks.",

    "H2O2":"Oksidator yang mudah terurai menjadi air dan oksigen.",

    "NaClO":"Digunakan sebagai pemutih dan desinfektan.",

    "CH3OH":"Alkohol sederhana yang sangat toksik dan mudah terbakar.",

    "C2H5OH":"Alkohol yang banyak digunakan sebagai pelarut dan antiseptik.",

    "Acetone":"Pelarut organik volatil yang mudah menguap dan mudah terbakar.",

    "CH3COCH3":"Nama lain aseton yang banyak digunakan sebagai pelarut.",

    "Benzene":"Senyawa aromatik yang bersifat karsinogenik.",

    "Toluene":"Turunan benzena yang digunakan sebagai pelarut organik.",

    "CHCl3":"Kloroform yang digunakan sebagai pelarut dalam sintesis organik.",

    "CCl4":"Karbon tetraklorida yang bersifat hepatotoksik.",

    "Glucose":"Monosakarida yang merupakan sumber energi utama makhluk hidup.",

    "C6H12O6":"Glukosa merupakan gula sederhana yang mudah larut dalam air.",

    "Sucrose":"Disakarida yang tersusun dari glukosa dan fruktosa.",

    "C12H22O11":"Sukrosa merupakan komponen utama gula pasir.",

    "Urea":"Senyawa amida yang digunakan sebagai bahan baku pupuk.",

    "BaCl2":"Barium klorida digunakan untuk identifikasi ion sulfat.",

    "BaSO4":"Endapan putih yang sering digunakan pada analisis gravimetri.",

    "CaCl2":"Garam yang higroskopis dan sering digunakan sebagai pengering.",

    "NaBr":"Garam bromida yang larut baik dalam air.",

    "KI":"Sumber ion iodida yang digunakan pada iodometri.",

    "I2":"Iodin digunakan sebagai oksidator dan indikator pati.",

    "KIO3":"Kalium iodat merupakan standar primer pada iodometri.",

    "Na2S2O3":"Natrium tiosulfat digunakan sebagai titran pada iodometri.",

    "EDTA":"Agen pengompleks yang digunakan pada titrasi kompleksometri.",

    "NH4SCN":"Amonium tiosianat digunakan pada titrasi Volhard.",

    "K2SO4":"Kalium sulfat digunakan sebagai pupuk dan sumber ion kalium.",

    "Fe2O3":"Oksida besi(III) yang merupakan komponen utama karat.",

    "CuO":"Oksida tembaga hitam yang digunakan pada berbagai sintesis.",

    "ZnO":"Oksida seng yang digunakan dalam kosmetik dan farmasi.",

    "MgO":"Oksida magnesium yang bersifat basa.",

    "AlCl3":"Katalis yang sering digunakan dalam reaksi Friedel-Crafts.",

    "NaF":"Sumber ion fluorida yang digunakan dalam pasta gigi.",

    "KF":"Kalium fluorida sebagai sumber ion fluorida dalam sintesis.",

    "LiCl":"Garam litium yang sangat higroskopis.",

    "Na2B4O7":"Boraks yang digunakan sebagai buffer dan bahan pembersih.",

    "H3PO4":"Asam fosfat yang digunakan dalam industri makanan dan pupuk."
        }

        if senyawa in analisis_spesifik:
            st.success(analisis_spesifik[senyawa])

        else:
            st.info(
                "Analisis spesifik senyawa belum tersedia. Analisis didasarkan pada golongan senyawanya."
            )

        # ================= SAFETY ASSESSMENT =================

        st.subheader("⚠️ Safety Assessment")

        bahaya = data[3]

        if "tinggi" in bahaya.lower():

            st.error(
                "🔴 Risiko Tinggi - Gunakan APD lengkap dan kerjakan di lemari asam."
            )

        elif "sedang" in bahaya.lower():

            st.warning(
                "🟠 Risiko Sedang - Hindari kontak langsung dan gunakan sarung tangan."
            )

        else:

            st.success(
                "🟢 Risiko Rendah - Tetap ikuti prosedur keselamatan laboratorium."
            )

        # ================= KARAKTERISTIK KIMIA =================

        st.subheader("🧬 Karakteristik Kimia")

        sifat = {

    "Asam kuat":[
        "Terionisasi hampir sempurna dalam air",
        "Elektrolit kuat",
        "Bersifat korosif terhadap logam dan jaringan"
    ],

    "Asam lemah":[
        "Terionisasi sebagian dalam air",
        "Konduktivitas listrik sedang",
        "Dapat membentuk larutan buffer"
    ],

    "Basa kuat":[
        "Menghasilkan ion OH⁻ dalam jumlah besar",
        "Elektrolit kuat",
        "Korosif terhadap kulit dan jaringan"
    ],

    "Basa lemah":[
        "Terionisasi sebagian",
        "Konduktivitas sedang",
        "Reaktivitas lebih rendah dibanding basa kuat"
    ],

    "Garam":[
        "Tersusun dari kation dan anion",
        "Dapat terdisosiasi dalam larutan",
        "Beberapa garam dapat mengalami hidrolisis"
    ],

    "Alkohol":[
        "Mengandung gugus hidroksil (-OH)",
        "Mudah menguap",
        "Sebagian besar mudah terbakar"
    ],

    "Keton":[
        "Mengandung gugus karbonil (>C=O)",
        "Bersifat polar",
        "Sering digunakan sebagai pelarut organik"
    ],

    "Aromatik":[
        "Mengandung cincin aromatik",
        "Stabil karena resonansi",
        "Umumnya bersifat nonpolar"
    ],

    "Karbohidrat":[
        "Mengandung gugus hidroksil dan karbonil",
        "Larut dalam air",
        "Merupakan sumber energi biologis"
    ],

    "Amida":[
        "Mengandung gugus -CONH₂",
        "Mampu membentuk ikatan hidrogen",
        "Banyak digunakan dalam sintesis organik"
    ],

    "Pelarut":[
        "Melarutkan berbagai senyawa",
        "Umumnya volatil",
        "Digunakan dalam proses laboratorium"
    ],

    "Oksidator":[
        "Mampu menerima elektron",
        "Mempercepat reaksi oksidasi",
        "Dapat bereaksi kuat dengan bahan organik"
        
            ]
        }

        if jenis in sifat:

            for item in sifat[jenis]:
                st.write("✔️", item)

        else:

            st.info("Karakteristik spesifik belum tersedia.")

       # ================= PREDIKSI =================

        st.subheader("🔬 Prediksi Perilaku Laboratorium")

        if "Asam" in jenis:
            st.info(
                "• Bereaksi dengan basa menghasilkan garam dan air.\n"
                "• Mengubah indikator menjadi merah.\n"
                "• Bersifat donor proton (H⁺)."
            )

        elif "Basa" in jenis:
            st.info(
                "• Bereaksi dengan asam menghasilkan garam dan air.\n"
                "• Mengubah indikator menjadi biru.\n"
                "• Bersifat akseptor proton."
            )

        elif "Garam" in jenis:
            st.info(
                "• Dapat mengalami hidrolisis.\n"
                "• Dapat membentuk endapan dengan ion tertentu.\n"
                "• Meningkatkan konduktivitas larutan."
            )

        else:
            st.info(
                "• Perilaku dipengaruhi gugus fungsi utama.\n"
                "• Digunakan sebagai pereaksi atau pelarut."
    )

        # ================= NFPA =================
        st.subheader("🚨 NFPA Hazard Indicator")

        nfpa = {
            "HCl": (0,3,1),
            "H2SO4": (0,3,2),
            "HNO3": (0,4,2),
            "HF": (0,4,0),
            "H3BO3": (0,1,0),
            "CH3COOH": (2,2,0),
            "NaOH": (0,3,1),
            "KOH": (0,3,1),
            "Ca(OH)2": (0,2,0),
            "NH3": (1,3,0),
            "NH4OH": (1,3,0),
            "NaCl": (0,0,0),
            "KCl": (0,1,0),
            "AgNO3": (0,2,1),
            "CuSO4": (0,2,0),
            "FeCl3": (0,3,1),
            "MgSO4": (0,1,0),
            "Na2CO3": (0,1,0),
            "NaHCO3": (0,1,0),
            "Pb(NO3)2": (0,3,1),
            "ZnSO4": (0,2,0),
            "Na2SO4": (0,0,0),
            "HgCl2": (0,4,0),
            "NaNO3": (0,2,1),
            "NH4Cl": (0,2,0),
            "NH4NO3": (0,2,3),
            "CaCO3": (0,0,0),
            "MgCl2": (0,1,0),
            "Al2(SO4)3": (0,1,0),
            "FeSO4": (0,1,0),
            "CuCl2": (0,2,1),
            "Na3PO4": (0,2,0),
            "KNO3": (0,1,2),
            "KMnO4": (0,2,3),
            "K2Cr2O7": (0,3,3),
            "H2O2": (0,2,2),
            "NaClO": (0,3,1),
            "CH3OH": (3,2,0),
            "C2H5OH": (3,2,0),
            "Acetone": (3,1,0),
            "CH3COCH3": (3,1,0),
            "Benzene": (3,2,0),
            "Toluene": (3,2,0),
            "CHCl3": (0,2,0),
            "CCl4": (0,2,0),
            "Glucose": (1,0,0),
            "C6H12O6": (1,0,0),
            "Sucrose": (1,0,0),
            "C12H22O11": (1,0,0),
            "Urea": (0,1,0),
            "BaCl2": (0,2,0),
            "BaSO4": (0,1,0),
            "CaCl2": (0,1,0),
            "NaBr": (0,1,0),
            "KI": (0,1,0),
            "I2": (0,2,1),
            "KIO3": (0,2,2),
            "Na2S2O3": (0,1,0),
            "EDTA": (0,1,0),
            "NH4SCN": (0,2,1),
            "K2SO4": (0,1,0),
            "Fe2O3": (0,1,0),
            "CuO": (0,1,0),
            "ZnO": (0,1,0),
            "MgO": (0,1,0),
            "AlCl3": (0,3,1),
            "NaF": (0,2,0),
            "KF": (0,2,0),
            "LiCl": (0,2,0),
            "Na2B4O7": (0,1,0),
            "H3PO4": (0,2,0)
        }

        def interpretasi_nfpa(nilai):
            if nilai == 0:
                return "Sangat Rendah"
            elif nilai == 1:
                return "Rendah"
            elif nilai == 2:
                return "Sedang"
            elif nilai == 3:
                return "Tinggi"
            elif nilai == 4:
                return "Sangat Tinggi"
            return "-"

        if senyawa in nfpa:

            f, h, r = nfpa[senyawa]

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric("🔥 Flammability", f, interpretasi_nfpa(f))

            with c2:
                st.metric("☣️ Health", h, interpretasi_nfpa(h))

            with c3:
                st.metric("⚛️ Reactivity", r, interpretasi_nfpa(r))

        else:
            st.info("Data NFPA belum tersedia.")

        # ================= KESIMPULAN =================
        st.subheader("📋 Kesimpulan")

        kesimpulan = f"""
{data[0]} merupakan senyawa golongan {data[1].lower()}
dengan massa molekul relatif {data[2]}.
"""

        if senyawa in nfpa:

            f, h, r = nfpa[senyawa]

            kesimpulan += f"""
Berdasarkan karakteristik kimianya, senyawa ini termasuk
golongan {data[1].lower()} yang memiliki sifat dan perilaku
khas dalam berbagai reaksi kimia.

Data NFPA menunjukkan tingkat kemudahan terbakar
(Flammability) sebesar {f}, tingkat bahaya kesehatan
(Health Hazard) sebesar {h}, dan tingkat reaktivitas
(Reactivity) sebesar {r}.
"""

            if h >= 3:
                kesimpulan += """
Senyawa ini memiliki risiko kesehatan yang tinggi sehingga
paparan langsung harus dihindari.
"""

            elif h == 2:
                kesimpulan += """
Senyawa ini memiliki risiko kesehatan sedang.
"""

            else:
                kesimpulan += """
Risiko kesehatan relatif rendah.
"""

            if f >= 3:
                kesimpulan += """
Senyawa mudah terbakar.
"""

            elif f == 2:
                kesimpulan += """
Senyawa memiliki potensi terbakar.
"""

            if r >= 2:
                kesimpulan += """
Reaktivitas cukup tinggi sehingga perlu kehati-hatian.
"""

        else:
            kesimpulan += f"""
Berdasarkan data yang tersedia, senyawa ini memiliki tingkat
bahaya {data[3].lower()}.
"""

        st.success(kesimpulan)

        st.markdown("<br>", unsafe_allow_html=True)

        if st.session_state.analisis_selesai:

            if st.button("⬅️ Kembali ke Home", key="home_analisis"):

                st.session_state.analisis_selesai = False
                st.session_state.menu = "🏠 Home"

                st.rerun()
    
# ================= TENTANG =================

if menu == "ℹ️ Tentang":

    st.title("ℹ️ Tentang Aplikasi")

    st.markdown("""
    <div style="
        background:#1E293B;
        padding:20px;
        border-radius:15px;
        color:white;
        box-shadow:0 6px 15px rgba(0,0,0,0.3);
    ">

    <h2>🧪 ChemAssist Pro</h2>

    <p>
    Aplikasi laboratorium kimia interaktif berbasis Python dan Streamlit.
    </p>

    <h3>🚀 Fitur Utama</h3>

    <ul>
        <li>Smart Solution Maker</li>
        <li>Smart pH Calculator</li>
        <li>Informasi Bahan Kimia</li>
        <li>Smart Chemical Analysis</li>
    </ul>

    <h3>👨‍💻 Teknologi</h3>

    <ul>
        <li>Python</li>
        <li>Streamlit</li>
    </ul>

    <h3>🎓 Dikembangkan Untuk</h3>

    <p>
    Praktikum dan pembelajaran kimia analitik,
    kimia dasar, serta perhitungan laboratorium.
    </p>

    <h3>👥 Creator Team</h3>

    <ul>
        <li><b>Adlina Dhiva Tsaniyah</b> (2560555)</li>
        <li><b>Davina Faiza Laksono</b> (2560605)</li>
        <li><b>Rachel Rafa Rashika</b> (2560738)</li>
        <li><b>Tantri Nirwana Bandiani</b> (2560795)</li>
    </ul>

    <h3>📌 Versi</h3>

    <p><b>ChemAssist Ultra v5.0</b></p>

    </div>
    """, unsafe_allow_html=True)
