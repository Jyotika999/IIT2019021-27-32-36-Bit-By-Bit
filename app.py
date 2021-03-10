#app.py

#app.py
import app1
import app2
import homepage
import change_Detection
#import EDAusingPandasProfiling
import streamlit as st



PAGES = {
    "HomePage": homepage,
    "prac.py chlalo ": app1,
    "EDA.py chlalo": app2,
    "CHANGE DETECTION.py chlaayo": change_Detection,
    #"EDA ANALYSIS USING PANDAS PROFILING": EDAusingPandasProfiling,
}
st.sidebar.title('HOME PAGE CONTENTS ')

selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()