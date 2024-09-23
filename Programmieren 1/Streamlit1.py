import streamlit as st 
import pandas as pd
import numpy as np

section = st.sidebar.radio("Which section?",
                            ("Klassenliste", "Slider", "Chart", "Button", "Placeholder"))



if section == "Klassenliste":
    data = {
    'Vorname': ['Anna', 'Ben', 'Clara', 'David', 'Eva', 'Felix', 'Greta', 'Hans', 'Isabella', 'Jonas'],
    'Nachname': ['Müller', 'Schmidt', 'Schneider', 'Fischer', 'Weber', 'Meyer', 'Wagner', 'Becker', 'Hofmann', 'Schulz']
    }

    df = pd.DataFrame(data)
    st.title("Klassenliste")
    st.write(data) 
            
elif section == "Slider":
    st.title("Slider")
    slider_value = st.slider('Wähle einen Wert', 0, 100, 50)
    st.write(f'Der aktuelle Wert ist: {slider_value}')
    
    
elif section == "Chart":
    st.title("Chart")
    zahlen = np.random.randint(1, 100, 10)
    df = pd.DataFrame(zahlen, columns=['Zahlen'])
    st.write(st.slider("Simple Slider", 1, 4, (0)))
    st.write('Hier ist die Liste mit 10 Zahlenwerten:')
    st.dataframe(df)
    st.write('Hier ist ein Chart der Zahlenwerte:')
    st.line_chart(df)

elif section == "Button":
    st.title("Button")
    st.write(f'Aktueller Zählerstand: {st.session_state.counter}')
if 'counter' not in st.session_state:
    st.session_state.counter = 0
if st.button('Zähler erhöhen'):
    st.session_state.counter += 9
if st.button('Zähler zurücksetzen'):
    st.session_state.counter = 0
    st.write(f'Aktueller Zählerstand: {st.session_state.counter}')

elif section == "Placeholder":
    st.title("Placeholder mit Klassennamen")
    data = {
    'Vorname': ['Anna', 'Ben', 'Clara', 'David', 'Eva', 'Felix', 'Greta', 'Hans', 'Isabella', 'Jonas'],
    }
    df = pd.DataFrame(data)
    placeholder = st.empty()
    placeholder.write('Hier ist die Klassenliste:')
    placeholder.dataframe(df)
    


