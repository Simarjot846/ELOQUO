import streamlit as st

st.title("✅ Streamlit Working!")
st.write("If you see this, Streamlit setup is correct.")

if st.button("Click me"):
    st.success("Button click works!")
