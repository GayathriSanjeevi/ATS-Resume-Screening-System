import streamlit as st
def display(skills):
    for i in skills:
        st.write("*",i.upper())