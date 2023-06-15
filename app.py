import streamlit as st

# Konfigurasi tampilan navbar
st.set_page_config(
    page_title="Streamlit Navbar",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Menampilkan navbar di bagian atas (top center) halaman
st.markdown(
    """
    <style>
    .navbar {
        display: flex;
        justify-content: center;
        padding: 1rem;
        background-color: #f0f0f0;
        margin-bottom: 1rem;
    }
    .navbar a {
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Konten halaman "Data"
if "Data" in st.session_state and st.session_state["Data"]:
    st.header("Halaman Data")
else:
    st.session_state["Data"] = False

# Konten halaman "Preprocessing Data"
if "Preprocessing" in st.session_state and st.session_state["Preprocessing"]:
    st.header("Halaman Preprocessing Data")
else:
    st.session_state["Preprocessing"] = False

# Konten halaman "Modelling"
if "Modelling" in st.session_state and st.session_state["Modelling"]:
    st.header("Halaman Modelling")
else:
    st.session_state["Modelling"] = False

# Konten halaman "Implementation"
if "Implementation" in st.session_state and st.session_state["Implementation"]:
    st.header("Halaman Implementation")
else:
    st.session_state["Implementation"] = False

# Tampilkan navbar
if st.button("Data"):
    st.session_state["Data"] = True
    st.session_state["Preprocessing"] = False
    st.session_state["Modelling"] = False
    st.session_state["Implementation"] = False

if st.button("Preprocessing Data"):
    st.session_state["Data"] = False
    st.session_state["Preprocessing"] = True
    st.session_state["Modelling"] = False
    st.session_state["Implementation"] = False

if st.button("Modelling"):
    st.session_state["Data"] = False
    st.session_state["Preprocessing"] = False
    st.session_state["Modelling"] = True
    st.session_state["Implementation"] = False

if st.button("Implementation"):
    st.session_state["Data"] = False
    st.session_state["Preprocessing"] = False
    st.session_state["Modelling"] = False
    st.session_state["Implementation"] = True
