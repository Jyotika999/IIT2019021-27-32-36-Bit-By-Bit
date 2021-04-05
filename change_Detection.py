# change detection and pop up

import numpy as np
import pandas as pd
import streamlit as st
import base64
import altair as alt


def app():
    @st.cache(allow_output_mutation=True)
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    menu1 = ["age", "sex", "steroid", "antivirals", "fatigue", "malaise", "anorexia", "liver_big", "liver_firm",
            "spleen_palable", "spiders", "ascites", "varices", "bilirubin", "alk_phosphate", "sgot", "albumin",
            "protime", "histology"]

    menu2 = ["sex","age", "steroid", "antivirals", "fatigue", "malaise", "anorexia", "liver_big", "liver_firm", "spleen_palable", "spiders", "ascites","varices","bilirubin","alk_phosphate","sgot","albumin","protime","histology"]
    choice1 = st.sidebar.selectbox("Attribute 1", menu1)
    choice2 = st.sidebar.selectbox("Attribute 2", menu2)

    st.markdown("<h1 style='text-align: center; color: #7b113a;'>Change in Trends and Values</h1>",
                unsafe_allow_html=True)
    st.subheader('About')
    st.write('Changes in attribute corresponding to the other attributes and corresponding to the live and '
             'death percentages. Select the attribute among which the changes are required to be seen from '
             'the side menu 1st attribute refers to attribute corresponding to the X-axis, and similarly '
             '2nd attribute refers to the attribute corresponding to the Y-axis ')

    dx = pd.read_csv('hepatitis.csv')
    df = pd.DataFrame(
        dx,
        columns=[choice1, choice2, 'class']
    )

    c = alt.Chart(df).mark_circle().encode(
        x=choice1, y=choice2, size='class', color='class', tooltip=[choice1, choice2, 'class'])

    st.altair_chart(c, use_container_width=True)

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