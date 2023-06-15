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
    st.markdown("<h1 style='text-align: center;'>Prediksi Saham</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        input1 = st.text_input("Input 1")
    
    with col2:
        input2 = st.text_input("Input 2")
    
    with col3:
        input3 = st.text_input("Input 3")
    
    # Tambahkan konten untuk halaman Implementation di sini
