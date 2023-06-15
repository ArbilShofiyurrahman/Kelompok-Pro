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
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="navbar">
        <a href="#" style="padding: 0 1rem;">Data</a>
        <a href="#" style="padding: 0 1rem;">Preprocessing Data</a>
        <a href="#" style="padding: 0 1rem;">Modelling</a>
        <a href="#" style="padding: 0 1rem;">Implementation</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Tambahkan konten di bawah navbar
st.header("Halaman Utama")
