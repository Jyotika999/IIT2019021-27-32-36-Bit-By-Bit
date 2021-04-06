
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

    df = pd.read_csv("Dataset/hepatitis.csv")
    attribute_name = st.sidebar.selectbox("SELECT ATTRIBUTE", (
        "age", "sex", "steroid", "antivirals", "fatigue", "malaise", "anorexia", "liver_big", "liver_firm",
        "spleen_palable", "spiders", "ascites", "varices", "bilirubin", "alk_phosphate", "sgot", "albumin", "protime",
        "histology"))
    st.title("Histogram Plot for " + attribute_name);
    st.write("the entire data set is divided into chunks of 30 rows and they ar analysed and visualised here "
             "individually as well as compared to the other parts of the chunks and the overall data set. Choose the"
             "attributes from the side bar drop down menu and the plots for mean variance and standard deviation are "
             "generated and their individual distribution over the data set can be visualised.")

    n = 30
    stdev = []
    varn = []
    meanx =[]
    final = [df[i * n:(i + 1) * n] for i in range((len(df) + n - 1) // n)]
    st.subheader("**ENTIRE DATA SET**")
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
    plt.xlabel(attribute_name)
    plt.ylabel("number of people")
    st.write(fig)
    col1, col2 = st.beta_columns(2)
    # st.write("X-axis: " + attribute_name + "Y-axis: number of people")
    col1.write("**Mean: **" + str(stat.mean(df[attribute_name])))
    col2.write(" **Variance: **" + str(stat.variance(df[attribute_name])))
    col1.write("** Standard Deviation:** " + str(stat.stdev(df[attribute_name])))
    stdev.append(stat.stdev(df[attribute_name]))
    varn.append(stat.variance(df[attribute_name]))
    meanx.append(stat.mean(df[attribute_name]))

    st.subheader("**FOR CHUNKS**")
    st.write("From here onwards the divided data set is being taken into account and their individual analysis is "
             "being done the attribute selection criteria is same in all the cases for all the generated graphs.")
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
    plt.xlabel(attribute_name)
    plt.ylabel("number of people")
    st.write(fig1)
    col1, col2 = st.beta_columns(2)
    # st.write("X-axis: " + attribute_name + "Y-axis: number of people")
    col1.write("**Mean:** " + str(stat.mean(final[0][attribute_name])))
    col2.write(" **Variance:** " + str(stat.variance(final[0][attribute_name])))
    col1.write(" **Standard Deviation: **" + str(stat.stdev(final[0][attribute_name])))
    stdev.append(stat.stdev(final[0][attribute_name]))
    varn.append(stat.variance(final[0][attribute_name]))
    meanx.append(stat.mean(final[0][attribute_name]))

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
    plt.xlabel(attribute_name)
    plt.ylabel("number of people")
    st.write(fig2)
    col1, col2 = st.beta_columns(2)
    # st.write("X-axis: " + attribute_name + "Y-axis: number of people")
    col1.write("**Mean: **" + str(stat.mean(final[1][attribute_name])))
    col2.write(" **Variance:** " + str(stat.variance(final[1][attribute_name])))
    col1.write(" **Standard Deviation:** " + str(stat.stdev(final[1][attribute_name])))
    stdev.append(stat.stdev(final[1][attribute_name]))
    varn.append(stat.variance(final[1][attribute_name]))
    meanx.append(stat.mean(final[1][attribute_name]))

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
    plt.xlabel(attribute_name)
    plt.ylabel("number of people")
    st.write(fig3)
    col1, col2 = st.beta_columns(2)
    # st.write("X-axis: " + attribute_name + "Y-axis: number of people")
    col1.write("**Mean:** " + str(stat.mean(final[2][attribute_name])))
    col2.write(" **Variance:** " + str(stat.variance(final[2][attribute_name])))
    col1.write(" **Standard Deviation:** " + str(stat.stdev(final[2][attribute_name])))
    stdev.append(stat.stdev(final[2][attribute_name]))
    varn.append(stat.variance(final[2][attribute_name]))
    meanx.append(stat.mean(final[2][attribute_name]))

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
    plt.xlabel(attribute_name)
    plt.ylabel("number of people")
    st.write(fig4)
    col1, col2 = st.beta_columns(2)
    # st.write("X-axis: " + attribute_name + "Y-axis: number of people")
    col1.write("**Mean: **" + str(stat.mean(final[3][attribute_name])))
    col2.write(" **Variance:** " + str(stat.variance(final[3][attribute_name])))
    col1.write(" **Standard Deviation:** " + str(stat.stdev(final[3][attribute_name])))
    stdev.append(stat.stdev(final[3][attribute_name]))
    varn.append(stat.variance(final[3][attribute_name]))
    meanx.append(stat.mean(final[3][attribute_name]))

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
    plt.xlabel(attribute_name)
    plt.ylabel("number of people")
    st.write(fig5)
    col1, col2 = st.beta_columns(2)
    # st.write("X-axis: " + attribute_name + "Y-axis: number of people")
    col1.write("**Mean: **" + str(stat.mean(final[4][attribute_name])))
    col2.write(" **Variance:** " + str(stat.variance(final[4][attribute_name])))
    col1.write(" **Standard Deviation:** " + str(stat.stdev(final[4][attribute_name])))
    stdev.append(stat.stdev(final[4][attribute_name]))
    varn.append(stat.variance(final[4][attribute_name]))
    meanx.append(stat.mean(final[4][attribute_name]))

    st.subheader("**Standard Deviation And Mean Plot**")
    st.write("Here we analyse the mean and standard deviation of chunks corresponding to the entire data set.")
    arri = np.array([1, 2, 3, 4, 5, 6])
    fig6 = plt.figure()
    plt.plot(arri, stdev, label="SD")
    plt.plot(arri, meanx, label="Mean")
    leg = plt.legend()
    plt.xlabel("Chunks Number")
    plt.ylabel("Y-axis")
    plt.show()
    st.write(fig6)

    st.subheader("**Variance Plot**")
    st.write("Here we analyse the Variance of chunks corresponding to the entire data set.")
    fig7 = plt.figure()
    plt.plot(arri, varn, label="Variance")
    leg = plt.legend()
    plt.xlabel("Chunks Number")
    plt.ylabel("Y-axis")
    plt.show()
    st.write(fig7)

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
