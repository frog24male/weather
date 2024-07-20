import streamlit as st

st.title("Weather Forecast")
place=st.text_input("City Name")
days=st.slider("Forecast Days",min_value=1 , max_value=5)
option=st.selectbox("Select data to view",('Temperature','Rain'))

st.subheader(f"{option} for next {days} days in {place}")
