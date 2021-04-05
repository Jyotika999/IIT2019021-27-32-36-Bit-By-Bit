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

import plotly.figure_factory as ff
import warnings

warnings.filterwarnings("ignore")


def app():
    # Add histogram data
    df = pd.read_csv("hepatitis.csv")
    #x1 = df["class"].tolist()
    #x2 = df["age"].tolist()
    #x3 = df["sex"].tolist()

    # Group data together
    #hist_data = [x1, x2, x3]
    #group_labels = ['percentage', 'age', 'sex']

    # Create distplot with custom bin_size
#    fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])

    # Plot!
    #st.plotly_chart(fig, use_container_width=True)

    # st.set_option('deprecation.showPlotGlobalUse', False)
    st.title("Hepatitis Dataset Correlation Matrix")
    st.write(sns.heatmap(df.corr()))
    st.pyplot()
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