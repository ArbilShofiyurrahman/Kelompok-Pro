import streamlit as st
import pandas as pd

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
    
    # Tambahkan pilihan preprocessing
    preprocessing_option = st.selectbox("Pilih Preprocessing", ("MinMaxScaler", "Reduksi Dimensi"))

    if preprocessing_option == "MinMaxScaler":
        st.write("Anda memilih MinMaxScaler")
        # Tambahkan konten untuk MinMaxScaler di sini
        
        # Simulasikan hasil preprocessing dengan tabel 3x3
        df_minmax = pd.DataFrame({
            'Fitur': ['Fitur 1', 'Fitur 2', 'Fitur 3'],
            'Hasil 1': [0.1, 0.2, 0.3],
            'Hasil 2': [0.4, 0.5, 0.6],
            'Hasil 3': [0.7, 0.8, 0.9]
        })
        st.subheader("Hasil Preprocessing MinMaxScaler")
        st.dataframe(df_minmax)

    elif preprocessing_option == "Reduksi Dimensi":
        st.write("Anda memilih Reduksi Dimensi")
        # Tambahkan konten untuk Reduksi Dimensi di sini
        
        # Simulasikan hasil preprocessing dengan tabel 3x3
        df_dimensi = pd.DataFrame({
            'Fitur': ['Fitur 1', 'Fitur 2', 'Fitur 3'],
            'Hasil 1': [1, 2, 3],
            'Hasil 2': [4, 5, 6],
            'Hasil 3': [7, 8, 9]
        })
        st.subheader("Hasil Preprocessing Reduksi Dimensi")
        st.dataframe(df_dimensi)

elif selected_page == "Modelling":
    st.header("Modelling Page")
    
    # Tambahkan pilihan model
    model_option = st.selectbox("Pilih Model", ("Naive Bayes", "KNN"))

    if model_option == "Naive Bayes":
        st.write("Anda memilih model Naive Bayes")
        # Tambahkan konten untuk model Naive Bayes di sini
        
        # Simulasikan penghitungan akurasi Naive Bayes
        accuracy = 0.85  # Contoh nilai akurasi
        
        st.write("Hasil Akurasi Naive Bayes: {:.2f}".format(accuracy))

    elif model_option == "KNN":
        st.write("Anda memilih model KNN")
        # Tambahkan konten untuk model KNN di sini
        
        # Simulasikan penghitungan akurasi KNN
        accuracy = 0.92  # Contoh nilai akurasi
        
        st.write("Hasil Akurasi KNN: {:.2f}".format(accuracy))
