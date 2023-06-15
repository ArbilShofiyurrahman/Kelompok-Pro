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
  st.write("tes")

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
