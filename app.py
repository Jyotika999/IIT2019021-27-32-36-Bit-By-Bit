#app.py

#app.py
import app1
import app2
import homepage
import change_Detection
import about_this_project
import info_About_models
#import EDAusingPandasProfiling
import streamlit as st



PAGES = {
    "HomePage": homepage,
    "prac.py chlalo ": app1,
    "EDA.py chlalo": app2,
    "CHANGE DETECTION.py chlaayo": change_Detection,
    "ABOUT OUR SOFTWARE": about_this_project,
    "INFO ABOUT MODELS": info_About_models
    #"EDA ANALYSIS USING PANDAS PROFILING": EDAusingPandasProfiling,
}
st.sidebar.title('HOME PAGE CONTENTS ')

selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()