aimport streamlit as st

st.title("zizaaum")
st.write(
    "pacar Song Kang 💋🔥."
)
st.header("pacar aku")
st.image("53c845ff78166a2610d9f4173c7dae36.jpg")

st.tittle("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis Sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
