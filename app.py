# app.py

# app.py
import app1
import app2
import homepage
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

# from PIL import Image
# img = Image.open("images/bacteria.png")
# st.image(img,width=500,caption='Streamlit Images')


PAGES = {
    "Home": homepage,
    "Visualisation ": app1,
    "EDA analysis": app2,
    "Detect Changes": change_Detection,
    "About Models": info_About_models,
    "Correlation matrix": correlation_matrix,
    "About Us": about_this_project,
    "testing with html": density_of_each_attr,
    "MIXTURE OF HTML, CSS, JS, STREAMLIT": html_profiling

    # "EDA ANALYSIS USING PANDAS PROFILING": EDAusingPandasProfiling,
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
st.sidebar.title('Welcome ')
selection = st.sidebar.radio("CONTENTS: ", list(PAGES.keys()))
page = PAGES[selection]
page.app()
