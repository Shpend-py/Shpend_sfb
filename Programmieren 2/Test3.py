import streamlit as st


col1 = "Bild 1.jpg"
col2 = "Bild 2.jpg"
col3 = "Bild 3.jpg"
col4 = "Bild 4.jpg"
col5 = "Bild 5.jpeg"
col6 = "Bild 6.jpeg"



col1, col2, col3 = st.columns(3)

with col1:
    st.header("eye")
    st.image("Bild 1.jpg")

with col2:
    st.header("eiffel tower")
    st.image("Bild 2.jpg")

with col3:
    st.header("River")
    st.image("Bild 3.jpg")

col4, col5, col6 = st.columns(3)
    
with col4:
    st.header("eagle")
    st.image("Bild 4.jpg")

with col5:
    st.header("lionmix")
    st.image("Bild 5.jpeg")

with col6:
    st.header("AstroCat")
    st.image("Bild 6.jpeg")
    