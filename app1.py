# prac.py
# import streamlit as st
# def app():
#     st.title('APP1')
#     st.write('Welcome to app1')

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import numpy as np
import statistics as stat
import seaborn as sns
import tkinter
import base64
import streamlit.components.v1 as components

import warnings

warnings.filterwarnings("ignore")


def app():
    @st.cache(allow_output_mutation=True)
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    df = pd.read_csv("hepatitis.csv")
    attribute_name = st.sidebar.selectbox("SELECT ATTRIBUTE", (
    "age", "sex", "steroid", "antivirals", "fatigue", "malaise", "anorexia", "liver_big", "liver_firm",
    "spleen_palable", "spiders", "ascites", "varices", "bilirubin", "alk_phosphate", "sgot", "albumin", "protime",
    "histology"))
    st.title("Histogram Plot for " + attribute_name);

    n = 30
    final = [df[i * n:(i + 1) * n] for i in range((len(df) + n - 1) // n)]
    st.subheader("Entire Data Set")
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
    col1, col2 = st.beta_columns(2)
    col1.write("X-axis: " + attribute_name )
    col2.write("Y-axis: number of people")
    #st.write("X-axis: " + attribute_name + "Y-axis: number of people")
    col1.write("Mean: " + str(stat.mean(df[attribute_name])))
    col2.write(" Variance: " + str(stat.variance(df[attribute_name])))
    col1.write(" Standard Deviation: "+str(stat.stdev(df[attribute_name])))

    st.subheader("For Chunks")
    fig1, ax1 = plt.subplots()
    final[0].hist(
        bins=8,
        column=attribute_name,
        grid=False,
        figsize=(8, 8),
        color="#576675",
        zorder=1,
        rwidth=0.7,
        ax=ax1,
    )
    st.write(fig1)
    col1, col2 = st.beta_columns(2)
    col1.write("X-axis: " + attribute_name)
    col2.write("Y-axis: number of people")
    # st.write("X-axis: " + attribute_name + "Y-axis: number of people")
    col1.write("Mean: " + str(stat.mean(final[0][attribute_name])))
    col2.write(" Variance: " + str(stat.variance(final[0][attribute_name])))
    col1.write(" Standard Deviation: " + str(stat.stdev(final[0][attribute_name])))

    fig2, ax2 = plt.subplots()
    final[1].hist(
        bins=8,
        column=attribute_name,
        grid=False,
        figsize=(8, 8),
        color="#ff9636",
        zorder=1,
        rwidth=0.7,
        ax=ax2,
    )
    st.write(fig2)
    col1, col2 = st.beta_columns(2)
    col1.write("X-axis: " + attribute_name)
    col2.write("Y-axis: number of people")
    # st.write("X-axis: " + attribute_name + "Y-axis: number of people")
    col1.write("Mean: " + str(stat.mean(final[1][attribute_name])))
    col2.write(" Variance: " + str(stat.variance(final[1][attribute_name])))
    col1.write(" Standard Deviation: " + str(stat.stdev(final[1][attribute_name])))

    fig3, ax3 = plt.subplots()
    final[2].hist(
        bins=8,
        column=attribute_name,
        grid=False,
        figsize=(8, 8),
        color="#687bbe",
        zorder=1,
        rwidth=0.7,
        ax=ax3,
    )
    st.write(fig3)
    col1, col2 = st.beta_columns(2)
    col1.write("X-axis: " + attribute_name)
    col2.write("Y-axis: number of people")
    # st.write("X-axis: " + attribute_name + "Y-axis: number of people")
    col1.write("Mean: " + str(stat.mean(final[2][attribute_name])))
    col2.write(" Variance: " + str(stat.variance(final[2][attribute_name])))
    col1.write(" Standard Deviation: " + str(stat.stdev(final[2][attribute_name])))

    fig4, ax4 = plt.subplots()
    final[3].hist(
        bins=8,
        column=attribute_name,
        grid=False,
        figsize=(8, 8),
        color="#daa520",
        zorder=1,
        rwidth=0.7,
        ax=ax4,
    )
    st.write(fig4)
    col1, col2 = st.beta_columns(2)
    col1.write("X-axis: " + attribute_name)
    col2.write("Y-axis: number of people")
    # st.write("X-axis: " + attribute_name + "Y-axis: number of people")
    col1.write("Mean: " + str(stat.mean(final[3][attribute_name])))
    col2.write(" Variance: " + str(stat.variance(final[3][attribute_name])))
    col1.write(" Standard Deviation: " + str(stat.stdev(final[3][attribute_name])))

    fig5, ax5 = plt.subplots()
    final[4].hist(
        bins=8,
        column=attribute_name,
        grid=False,
        figsize=(8, 8),
        color="#800080",
        yrot=2,
        zorder=1,
        rwidth=0.7,
        ax=ax5,
    )
    st.write(fig5)
    col1, col2 = st.beta_columns(2)
    col1.write("X-axis: " + attribute_name)
    col2.write("Y-axis: number of people")
    # st.write("X-axis: " + attribute_name + "Y-axis: number of people")
    col1.write("Mean: " + str(stat.mean(final[4][attribute_name])))
    col2.write(" Variance: " + str(stat.variance(final[4][attribute_name])))
    col1.write(" Standard Deviation: " + str(stat.stdev(final[4][attribute_name])))

    # changing background color
    st.markdown(
        f"""
               <style>
               .reportview-container {{
                   background: #E55D87;  /* fallback for old browsers */
background: -webkit-linear-gradient(to right, #5FC3E4, #E55D87);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #5FC3E4, #E55D87); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

               }}

               </style>
               """,
        unsafe_allow_html=True
    )
