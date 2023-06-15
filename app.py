import streamlit as st

# Konfigurasi tampilan navbar
st.set_page_config(
    page_title="Streamlit Navbar",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Menampilkan navbar
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio(
    "Go to",
    ("Data", "Preprocessing Data", "Modelling", "Implementation")
)

# Tampilkan konten sesuai dengan halaman yang dipilih
if selected_page == "Data":
    st.header("Data Page")
    # Tambahkan konten untuk halaman Data di sini

elif selected_page == "Preprocessing Data":
    st.header("Preprocessing Data Page")
    # Tambahkan konten untuk halaman Preprocessing Data di sini

elif selected_page == "Modelling":
    st.header("Modelling Page")
    # Tambahkan konten untuk halaman Modelling di sini

elif selected_page == "Implementation":
    st.header("Implementation Page")
    # Tambahkan konten untuk halaman Implementation di sini
