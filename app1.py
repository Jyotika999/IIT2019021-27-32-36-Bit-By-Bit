# prac.py
# import streamlit as st
# def app():
#     st.title('APP1')
#     st.write('Welcome to app1')

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import numpy as np
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

    main_bg = "back.png"
    main_bg_ext = "back.png"


    df = pd.read_csv("hepatitis.csv")
    df_split = np.array_split(df, 30)
    attribute_name = st.sidebar.selectbox("SELECT ATTRIBUTE", ("age", "sex", "steroid", "antivirals", "fatigue", "malaise", "anorexia", "liver_big", "liver_firm", "spleen_palable", "spiders", "ascites","varices","bilirubin","alk_phosphate","sgot","albumin","protime","histology"))
    st.title("Histogram Plot for " + attribute_name);

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
    st.write("X-axis: " + attribute_name + " groups")
    st.write("Y-axis: number of people")

    st.subheader("For Chunks")
    fig1, ax1 = plt.subplots()
    df_split[0].hist(
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
    st.write("X-axis: " + attribute_name + " groups")
    st.write("Y-axis: percentage of people")

    fig2, ax2 = plt.subplots()
    df_split[1].hist(
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
    st.write("X-axis: " + attribute_name + " groups")
    st.write("Y-axis: percentage of people")

    fig3, ax3 = plt.subplots()
    df_split[2].hist(
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
    st.write("X-axis: " + attribute_name + " groups")
    st.write("Y-axis: percentage of people")

    fig4, ax4 = plt.subplots()
    df_split[3].hist(
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
    st.write("X-axis: " + attribute_name + " groups")
    st.write("Y-axis: percentage of people")

    fig5, ax5 = plt.subplots()
    df_split[4].hist(
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
    st.write("X-axis: " + attribute_name + " groups")
    st.write("Y-axis: percentage of people")


    # changing background color
    st.markdown(
        f"""
               <style>
               .reportview-container {{
                   background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
               }}

               </style>
               """,
        unsafe_allow_html=True
    )

