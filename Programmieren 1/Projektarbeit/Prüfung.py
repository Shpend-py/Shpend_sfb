import streamlit as st

# Titel der Anwendung
st.title("Raumtemperaturregler")

# Beschreibung
st.write("""
Diese Anwendung simuliert einen Raumtemperaturregler. 
Verwenden Sie den Schieberegler, um die Temperatur einzustellen.
""")

# Schieberegler für die Temperatur
temperatur = st.slider("Stellen Sie die gewünschte Raumtemperatur ein", 
                       min_value=10, 
                       max_value=30, 
                       value=20, 
                       step=1)

# Anzeige der aktuellen Temperatur
st.write(f"Die aktuelle eingestellte Temperatur beträgt: {temperatur} °C")

# Optionale Erweiterung: Darstellung der Temperaturhistorie
if "temperatur_historie" not in st.session_state:
    st.session_state.temperatur_historie = []

st.session_state.temperatur_historie.append(temperatur)

# Historie anzeigen
st.line_chart(st.session_state.temperatur_historie)

# Hinweis zur Anwendung
st.info("Diese Anwendung ist eine Simulation und dient nur Demonstrationszwecken.")
