import streamlit as st

st.header (':blue[ini adalah aplikasi kalkulator pejumlahan]')
st.subheader ('silahkan masukan angka yang mau di hitung! :sunglasses:')

number1 = st.number_input('masukan bilangan pertama')
st.write(f'bilangan pertama adalah {number1}')

number2 = st.number_input('masukkan bilangan kedua')
st.write(f'bilangan kedua adalah {number2}')

if st.button('hitung pejumlahan'):
    hasil = number1+number2
    st.success(f'hasil dari perjumlahan dari {number1} ditambah {number2} adalah {hasil}')
else:
    st.write('silahkan masukkan tombol "hitung" jika ingin melakukan pejumlahan')

