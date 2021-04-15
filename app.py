# app.py

# app.py
import app1
import app2
import homepage
import predict
import change_Detection
import about_this_project
import info_About_models
import correlation_matrix
import density_of_each_attr
import html_profiling
# import EDUsingPandasProfiling
import streamlit as st
import time


# Spinner
with st.spinner("Waiting .."):
	time.sleep(5)



PAGES = {
    "Home": homepage,
    "Data Visualisation ": app1,
    #"EDA analysis": app2,
    "Change Detection on attributes": change_Detection,
    #"Correlation matrix": correlation_matrix,
    "Density of attributes": density_of_each_attr,
    "Profiling of Dataset": html_profiling,
    "Mortality Prediction": predict,
    "Models used": info_About_models,
    "About Team: Bit By Bit": about_this_project,


}
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #008B8B;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.sidebar.image('images/liver-care.png', width=210)
st.sidebar.title('Hepatitis Analysis ')
selection = st.sidebar.radio("CONTENTS: ", list(PAGES.keys()))
page = PAGES[selection]
page.app()
