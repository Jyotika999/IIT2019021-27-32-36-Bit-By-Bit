# app.py

# app.py
import app1
import app2
import homepage
import change_Detection
import about_this_project
import info_About_models
# import EDUsingPandasProfiling
import streamlit as st

PAGES = {
    "Home": homepage,
    "Visualisation ": app1,
    "EDA analysis": app2,
    "Detect Changes": change_Detection,
    "About Models": info_About_models,
    "About Us": about_this_project
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
st.sidebar.image('images/hepatitis2.jpg', width=210)
st.sidebar.title('HOME PAGE CONTENTS ')
selection = st.sidebar.radio("CONTENTS: ", list(PAGES.keys()))
page = PAGES[selection]
page.app()
