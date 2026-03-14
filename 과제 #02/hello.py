import streamlit as st

st.title("Enter your name")

name = st.text_input("Name")

if st.button("Submit"):
    if name:
        st.success(f"Hello {name}! 🎉")
        st.balloons()
    else:
        st.warning("Please enter your name")