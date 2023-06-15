import pandas as pd
import pickle
import streamlit as st

# load the model from disk
model = pickle.load(open('knn_model.pkl', 'rb'))
model2 = pickle.load(open('naive_bayes_model.pkl', 'rb'))

st.set_page_config(
    page_title="Prediksi Harga Saham Bank BCA",
    page_icon="👋",
)


st.title("")
st.sidebar.success("Pilih Halaman Yang Ingin Anda Tuju.")

st.title("Prediksi Harga Saham Bank BCA")

tab1, tab2, tab3, tab4 = st.tabs(["Data", "Preprocessing Data", "Modeling", "Implementasi"])

with tab1:
   st.markdown("### Deskripsi Data Saham BBCA")
   st.image("data.jpeg")
    # Deskripsi data saham BBCA
   
   st.markdown("1. Asal Data:")
   st.markdown("   Saya telah mengambil data harga saham PT Bank Central Asia Tbk (BBCA) dari sumber yang terpercaya, yaitu Yahoo Finance.")
   st.markdown("2. Tipe Data:")
   st.markdown("   Data harga saham BBCA merupakan tipe data float, yang digunakan untuk merepresentasikan angka desimal atau pecahan.")
   st.markdown("3. Tentang Data:")
   st.markdown("   Data ini mencakup informasi dan statistik terkait harga saham BBCA selama periode tertentu. Anda dapat melakukan analisis lebih lanjut terhadap data ini, seperti menghitung rata-rata harga saham, mengidentifikasi perubahan persentase, dan melakukan perhitungan lainnya yang relevan untuk analisis pasar dan investasi.")


with tab2:
   st.write("Reduksi Dimensi")
   st.image("ReduksiDimensi.jpeg")
   st.write("MinMax Scaller")
   st.image("MMScaler.jpeg")
    
with tab3:
   st.write("Metode KNN")
   st.image("AkurasiKNN.jpeg")
   st.write("Metode Naive Bayes")
   st.image("AkurasiNB.jpeg")

with tab4:
    # Define the prediction function
    def predict(Close, High, Low, Volume):
        prediction = model.predict(pd.DataFrame([[Close, High, Low, Volume]], columns = ["Close", "High", "Low", "Volume"]))
        return prediction

    def predict2(Close, High, Low, Volume):
        prediction2 = model2.predict(pd.DataFrame([[Close, High, Low, Volume]], columns = ["Close", "High", "Low", "Volume"]))
        return prediction2
    
    st.header('Jawablah Semua Pertanyaan Berikut :')

    Close = st.number_input("Harga penutupan saham pada suatu periode waktu", key="Close", value= 8550)
    High = st.number_input("Harga tertinggi saham dalam periode waktu tersebut", key="High", value= 8600)
    Low = st.number_input("Harga terendah saham dalam periode waktu tersebut", key="Low", value= 8500)
    Volume = st.number_input("Volume perdagangan saham dalam suatu periode waktu.", key="Volume", value= 10653900)

    if st.button('Prediksi'):
        prediksi = predict(Close, High, Low, Volume)
        prediksi2 = predict2(Close, High, Low, Volume)
        st.success(f'Prediksi harga pembukaan KNN: {prediksi}')
        st.success(f'Prediksi harga pembukaan Menggunakan Naive Bayes: {prediksi2}')
