import streamlit as st

st.set_page_config(page_title="Temperature Converter", page_icon="🌡️")

st.title("🌡️ Temperature Converter")

st.write("Convert temperatures between Celsius, Fahrenheit, and Kelvin.")

# User input
temperature = st.number_input("Enter Temperature Value:", value=0.0)

unit = st.selectbox(
    "Select Unit:",
    ("Celsius", "Fahrenheit", "Kelvin")
)

def convert_temperature(temp, unit):
    if unit == "Celsius":
        c = temp
        f = (temp * 9/5) + 32
        k = temp + 273.15
    elif unit == "Fahrenheit":
        c = (temp - 32) * 5/9
        f = temp
        k = c + 273.15
    else:  # Kelvin
        c = temp - 273.15
        f = (c * 9/5) + 32
        k = temp
    
    return c, f, k

if st.button("Convert"):
    c, f, k = convert_temperature(temperature, unit)

    st.success("Converted Values:")
    st.w
