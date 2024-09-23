import streamlit as st
from time import sleep
from random import randint

def read_sensor():
    sleep(0.4)
    return randint(1, 10)

for i in range(20):
    sensor = read_sensor()
    st.write(f'Sensor data: {sensor}')

place = st.empty()

for i in range(20):
    sensor = read_sensor()
    place.write(f'Sensor data: {sensor}')
    
place2 = st.empty()
data= []
for i in range(20):
    sensor = read_sensor()
    data.append(sensor)
    place2.line_chart(data)
    
place2.write('Done')
