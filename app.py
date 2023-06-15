import pandas as pd
import pickle
import streamlit as st

# load the model from disk
model = pickle.load(open('knn_model.pkl', 'rb'))
model2 = pickle.load(open('naive_bayes_model.pkl', 'rb'))

st.set_page_config(
    page_title="Prediksi Nilai Saham Bank BCA",
    page_icon="👋",
)

st.title("")
st.sidebar.success("Pilih Halaman Yang Ingin Anda Tuju.")

st.title("Prediksi Nilai Saham Bank BCA")

tab1, tab2, tab3, tab4 = st.tabs(["Data", "Preprocessing Data", "Modeling", "Implementasi"])

with tab1:
  # Deskripsi data saham BBCA
   st.markdown("### Deskripsi Data Saham BBCA")
   st.markdown("1. Asal Data:")
   st.markdown("   Saya telah mengambil data harga saham PT Bank Central Asia Tbk (BBCA) dari sumber yang terpercaya, yaitu Yahoo Finance.")
   st.markdown("2. Tipe Data:")
   st.markdown("   Data harga saham BBCA merupakan tipe data float, yang digunakan untuk merepresentasikan angka desimal atau pecahan.")
   st.markdown("3. Tentang Data:")
   st.markdown("   Data ini mencakup informasi dan statistik terkait harga saham BBCA selama periode tertentu. Anda dapat melakukan analisis lebih lanjut terhadap data ini, seperti menghitung rata-rata harga saham, mengidentifikasi perubahan persentase, dan melakukan perhitungan lainnya yang relevan untuk analisis pasar dan investasi.")



with tab2:
   st.write("Reduksi Dimensi")
   
   st.write("MinMax Scaller")
   
    
with tab3:
   st.write("Metode KNN")
   
   st.write("Metode Naive Bayes")
   

with tab4:
    # Define the prediction function
    def predict(Open, High, Low, Close, Volume):
        prediction = model.predict(pd.DataFrame([[Open, High, Low, Close, Volume]], columns = ['"Open, High, Low, Close, Volume"',]))
        return prediction

    def predict2(Open, High, Low, Close, Volume):
        prediction2 = model2.predict2(pd.DataFrame([[Open, High, Low, Close, Volume]], columns = ['"Open, High, Low, Close, Volume"',]))
        return prediction2
    
    st.header('Jawablah Semua Pertanyaan Berikut :')

    Open = st.selectbox('open', ['Setuju', 'Tidak Setuju'])
    High = st.selectbox('high', ['Setuju', 'Tidak Setuju'])
    Low = st.selectbox('low', ['Setuju', 'Tidak Setuju'])
    Close = st.selectbox('close', ['Setuju', 'Tidak Setuju'])
    Volume = st.selectbox('vol', ['Iya Tahu', 'Tidak Tahu'])

    if st.button('Prediksi'):
        prediksi = predict(Open, High, Low, Close, Volume)
        prediksi2 = predict2(Open, High, Low, Close, Volume)
        st.success(f'Prediksi harga open KNN: {prediksi}')
        st.success(f'Prediksi harga open Menggunakan Naive Bayes: {prediksi2}')
