import streamlit as st
import pandas as pd
from temperature_converter import (
    celsius_to_others,
    fahrenheit_to_others,
    kelvin_to_others
)

st.set_page_config(page_title="Temperature Converter")

# ---------- Style ----------
st.markdown("""
<style>
.main-title {text-align:center;font-size:40px;font-weight:bold;color:#ff4b4b;}
.subtext {text-align:center;color:grey;margin-bottom:30px;}
.result-box {background:black;
    color:white;
    padding:15px;
    border-radius:10px;
    margin:8px 0;
    font-size:18px;}
}
footer {text-align:center;margin-top:30px;color:grey;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title"> Smart Temperature Converter</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Convert between Celsius, Fahrenheit & Kelvin instantly</div>', unsafe_allow_html=True)

# ---------- Session State ----------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------- Inputs ----------
col1, col2 = st.columns(2)
with col1:
    temp = st.number_input("Enter Temperature", value=0.0)
with col2:
    unit = st.selectbox("Select Unit", ["Celsius", "Fahrenheit", "Kelvin"])

# ---------- Conversion ----------
if st.button(" Convert"):
    if unit == "Celsius":
        f, k = celsius_to_others(temp)
        result = f"{temp} °C → {f:.2f} °F, {k:.2f} K"
        st.markdown(f'<div class="result-box"> {f:.2f} °F</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-box"> {k:.2f} K</div>', unsafe_allow_html=True)

    elif unit == "Fahrenheit":
        c, k = fahrenheit_to_others(temp)
        result = f"{temp} °F → {c:.2f} °C, {k:.2f} K"
        st.markdown(f'<div class="result-box"> {c:.2f} °C</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-box"> {k:.2f} K</div>', unsafe_allow_html=True)

    else:
        c, f = kelvin_to_others(temp)
        result = f"{temp} K → {c:.2f} °C, {f:.2f} °F"
        st.markdown(f'<div class="result-box"> {c:.2f} °C</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-box"> {f:.2f} °F</div>', unsafe_allow_html=True)

    st.session_state.history.append(result)

# ---------- History ----------
if st.session_state.history:
    st.subheader("Conversion History")

    for item in reversed(st.session_state.history[-5:]):
        st.write("•", item)

    df = pd.DataFrame(st.session_state.history, columns=["Conversion"])

    st.download_button(
        label="Download History",
        data=df.to_csv(index=False),
        file_name="conversion_history.csv",
        mime="text/csv",
    )

    if st.button("Clear History"):
        st.session_state.history = []

# ---------- Footer ----------
st.markdown("<footer>Built with by Harshitha SH</footer>", unsafe_allow_html=True)

