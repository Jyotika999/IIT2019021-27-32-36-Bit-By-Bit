
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import numpy
import seaborn as sns
import tkinter
import base64
import warnings
warnings.filterwarnings("ignore")
import streamlit.components.v1 as components

def app():


    @st.cache(allow_output_mutation=True)
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

        # bootstrap 4 collapse example

    df = pd.read_csv("hepatitis.csv")

    fig = plt.figure(figsize=(12, 18))
    for i in range(len(df.columns)):
        fig.add_subplot(9, 4, i + 1)
        sns.distplot(df.iloc[:, i].dropna(), rug=True, hist=True, label='UW', kde_kws={'bw': 0.1})
        plt.xlabel(df.columns[i])
    plt.tight_layout()
    plt.show()
    components.html(
        """
      <h1 style='text-align: center; color: #7b113a;'> Density of each attribute </h1>
        """
    )


    st.pyplot(fig)


    col1, col2, col3 = st.beta_columns(3)

    with col1:

        st.image("https://static.streamlit.io/examples/owl.jpg")

    with col2:

        st.image("https://static.streamlit.io/examples/owl.jpg")

    with col3:

        st.image("https://static.streamlit.io/examples/owl.jpg")






    # main_bg = "back.png"
    # main_bg_ext = "back.png"

    st.markdown(
        """
        <style>
        .reportview-container {
            background: rgb(29,218,73);
background: linear-gradient(90deg, rgba(29,218,73,1) 0%, rgba(0,212,255,1) 100%);
        }
       .sidebar .sidebar-content {
            
        }
        </style>
        """,
        unsafe_allow_html=True
    )