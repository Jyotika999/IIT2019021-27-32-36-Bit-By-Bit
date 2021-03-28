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
    df = pd.read_csv("hepatitis.csv")

    attribute_name = st.sidebar.selectbox("SELECT ATTRIBUTE", ("age", "sex", "steroid"))
    st.title("Histogram Plot for " + attribute_name);

    fig, ax = plt.subplots()
    df.hist(
        bins=8,
        column=attribute_name,
        grid=False,
        figsize=(8, 8),
        color="#86bf91",
        zorder=1,
        rwidth=0.7,
        ax=ax,
    )
    st.write(fig)
    st.write("X-axis: " + attribute_name + " groups")
    st.write("Y-axis: number of people")
    # changing background color
    st.markdown("""
    <style>
    body {
        color: 	#F5F5F5;
        background-color: #b19cd9;
    }
    </style>
        """, unsafe_allow_html=True)

    if st.checkbox("Show correlation matrix"):
        st.write(sns.heatmap(df.corr()))
        st.pyplot()
