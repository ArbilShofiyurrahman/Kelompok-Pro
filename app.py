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
     # Tambahkan pilihan model
    model_option = st.selectbox("Pilih Model", ("Naive Bayes", "KNN"))

    if model_option == "Naive Bayes":
        st.write("Anda memilih model Naive Bayes")
        # Tambahkan konten untuk model Naive Bayes di sini

    elif model_option == "KNN":
        st.write("Anda memilih model KNN")
        # Tambahkan konten untuk model KNN di sini

elif selected_page == "Implementation":
    st.header("Implementation Page")
    st.markdown("<h1 style='text-align: center;'>Prediksi Saham</h1>", unsafe_allow_html=True)
    
    # Membuat layout kolom secara vertikal menggunakan Flexbox
    st.markdown(
        """
        <style>
        .flex-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Tambahkan konten kolom input 1
    with st.markdown("<div class='flex-container'>"):
        st.write("Kolom Input 1")
        # Tambahkan konten kolom input 1 di sini
        input1 = st.text_input("Input 1:")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Tambahkan konten kolom input 2
    with st.markdown("<div class='flex-container'>"):
        st.write("Kolom Input 2")
        # Tambahkan konten kolom input 2 di sini
        input2 = st.text_input("Input 2:")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Tambahkan konten kolom input 3
    with st.markdown("<div class='flex-container'>"):
        st.write("Kolom Input 3")
        # Tambahkan konten kolom input 3 di sini
        input3 = st.text_input("Input 3:")
    st.markdown("</div>", unsafe_allow_html=True)
     # Tambahkan tombol "Hasil Prediksi"
    st.button("Hasil Prediksi")
