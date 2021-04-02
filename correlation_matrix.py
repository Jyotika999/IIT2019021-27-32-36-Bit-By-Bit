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


    #Add histogram data
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2

    #Group data together
    hist_data = [x1, x2, x3]
    group_labels = ['Group 1', 'Group 2', 'Group 3']

    # Create distplot with custom bin_size
    fig = ff.create_distplot(hist_data, group_labels, bin_size = [.1, .25, .5])

    # Plot!
    st.plotly_chart(fig, use_container_width=True)
    df = pd.read_csv("hepatitis.csv")


    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title("Hepatitis Dataset Correlation Matrix")
    st.write(sns.heatmap(df.corr()))
    st.pyplot()




