import streamlit as st

# Custom CSS für die Sidebar
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        padding: 10px;
    }
    .sidebar .sidebar-content h2 {
        color: #4CAF50;
    }
    .sidebar .sidebar-content .radio {
        padding: 5px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar für Raumauswahl
with st.sidebar:
    st.title("Raumsteuerung")
    st.subheader("Wählen Sie einen Raum aus:")
    section = st.radio('', ('Schlafzimmer', 'Küche', 'WC'))

# Code für Schlafzimmer
if section == 'Schlafzimmer':
    st.header("Raumtemperaturregler Schlafzimmer")

    if "show_slider_raum3" not in st.session_state:
        st.session_state.show_slider_raum3 = True

    def toggle_slider_raum3():
        st.session_state.show_slider_raum3 = not st.session_state.show_slider_raum3

    st.button("Raumregler Schlafzimmer ein/ausblenden", on_click=toggle_slider_raum3)

    if st.session_state.show_slider_raum3:
        if "temperatur_raum3" not in st.session_state:
            st.session_state.temperatur_raum3 = 20
        temperatur_raum3 = st.slider(
            "Stellen Sie die gewünschte Raumtemperatur ein",
            min_value=16,
            max_value=28,
            value=st.session_state.temperatur_raum3,
            step=1,
            key='slider_raum3'
        )
        st.session_state.temperatur_raum3 = temperatur_raum3
        st.write(f"Die aktuelle eingestellte Temperatur beträgt: {temperatur_raum3} °C")
    else:
        st.write("Der Raumregler für das Schlafzimmer ist ausgeblendet.")

    st.header('Beleuchtung Schlafzimmer')

    if 'button1' not in st.session_state:
        st.session_state.button1 = False

    def click_button1():
        st.session_state.button1 = not st.session_state.button1

    st.button('Lampe Ein/Aus', on_click=click_button1)

    if st.session_state.button1:
        st.write('Lampe Aus')
        st.image('path/to/lampe_aus.jpg')
    else:
        st.write('Lampe Ein')
        st.image('path/to/lampe_ein.jpg')

# Code für Küche
if section == 'Küche':
    st.header("Raumtemperaturregler Küche")

    if "show_slider_raum2" not in st.session_state:
        st.session_state.show_slider_raum2 = True

    def toggle_slider_raum2():
        st.session_state.show_slider_raum2 = not st.session_state.show_slider_raum2

    st.button("Raumregler Küche ein/ausblenden", on_click=toggle_slider_raum2)

    if st.session_state.show_slider_raum2:
        if "temperatur_raum2" not in st.session_state:
            st.session_state.temperatur_raum2 = 20
        temperatur_raum2 = st.slider(
            "Stellen Sie die gewünschte Raumtemperatur ein",
            min_value=16,
            max_value=28,
            value=st.session_state.temperatur_raum2,
            step=1,
            key='slider_raum2'
        )
        st.session_state.temperatur_raum2 = temperatur_raum2
        st.write(f"Die aktuelle eingestellte Temperatur beträgt: {temperatur_raum2} °C")
    else:
        st.write("Der Raumregler für die Küche ist ausgeblendet.")

    st.header('Beleuchtung Küche')

    if 'button2' not in st.session_state:
        st.session_state.button2 = False

    def click_button2():
        st.session_state.button2 = not st.session_state.button2

    st.button('Lampe Ein/Aus', on_click=click_button2)

    if st.session_state.button2:
        st.write('Lampe Aus')
        st.image('path/to/lampe_aus.jpg')
    else:
        st.write('Lampe Ein')
        st.image('path/to/lampe_ein.jpg')

# Code für WC
if section == 'WC':
    st.header("Raumtemperaturregler WC")

    if "show_slider_raum1" not in st.session_state:
        st.session_state.show_slider_raum1 = True

    def toggle_slider_raum1():
        st.session_state.show_slider_raum1 = not st.session_state.show_slider_raum1

    st.button("Raumregler WC ein/ausblenden", on_click=toggle_slider_raum1)

    if st.session_state.show_slider_raum1:
        if "temperatur_raum1" not in st.session_state:
            st.session_state.temperatur_raum1 = 20
        temperatur_raum1 = st.slider(
            "Stellen Sie die gewünschte Raumtemperatur ein",
            min_value=16,
            max_value=28,
            value=st.session_state.temperatur_raum1,
            step=1,
            key='slider_raum1'
        )
        st.session_state.temperatur_raum1 = temperatur_raum1
        st.write(f"Die aktuelle eingestellte Temperatur beträgt: {temperatur_raum1} °C")
    else:
        st.write("Der Raumregler für das WC ist ausgeblendet.")

    st.header('Beleuchtung WC')

    if 'button3' not in st.session_state:
        st.session_state.button3 = False

    def click_button3():
        st.session_state.button3 = not st.session_state.button3

    st.button('Lampe Ein/Aus', on_click=click_button3)

    if st.session_state.button3:
        st.write('Lampe Aus')
        st.image('path/to/lampe_aus.jpg')
    else:
        st.write('Lampe Ein')
        st.image('path/to/lampe_ein.jpg')


    