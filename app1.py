# prac.py
# import streamlit as st
# def app():
#     st.title('APP1')
#     st.write('Welcome to app1')

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import numpy
import seaborn as sns
import tkinter
import base64

def app():
    st.title("Hepatitis")
    st.write("")

    df = pd.read_csv("hepatitis.csv")

    attribute_name = st.sidebar.selectbox("Select attribute", ("age", "sex", "steroid"))

    fig, ax = plt.subplots()
    df.hist(
        bins=8,
        column=attribute_name,
        grid=False,
        figsize=(8, 8),
        color="#86bf91",
        zorder=2,
        rwidth=0.9,
        ax=ax,
    )
    st.write(fig)

    # changing background color
    st.markdown("""
    <style>
    body {
        color: #fff;
        background-color: #35b7aa;
    }
    </style>
        """, unsafe_allow_html=True)

    if st.checkbox("Show correlation matrix"):
        st.write(sns.heatmap(df.corr()))
        st.pyplot()


