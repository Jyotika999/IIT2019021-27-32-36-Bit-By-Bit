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

    main_bg = "back.png"
    main_bg_ext = "back.png"

    st.markdown("<h1 style='text-align: center; color: #7b113a;'>Change in Trends and Values</h1>",
                unsafe_allow_html=True)
    st.subheader('About')
    st.write('On the test data when a change is encountered which does not follow the regular flow in the pattern'
             ', it shows the pop up message accordingly')

    dx = pd.read_csv('hepatitis.csv')
    df = pd.DataFrame(
        dx,
        columns=['class', 'age', 'sex']
    )

    c = alt.Chart(df).mark_circle().encode(
        x='class', y='age', size='sex', color='sex', tooltip=['class', 'age', 'sex'])

    st.altair_chart(c, use_container_width=True)

    df1 = pd.DataFrame(
        dx,
        columns=['alk_phosphate', 'albumin', 'class']
    )

    c = alt.Chart(df1).mark_circle().encode(
        x='alk_phosphate', y='albumin', size='class', color='class', tooltip=['alk_phosphate', 'albumin', 'class'])

    st.altair_chart(c, use_container_width=True)

    df2 = pd.DataFrame(
        dx,
        columns=['sgot', 'protime', 'class']
    )

    c = alt.Chart(df2).mark_circle().encode(
        x='sgot', y='protime', size='class', color='class', tooltip=['sgot', 'protime', 'class'])

    st.altair_chart(c, use_container_width=True)

    df3 = pd.DataFrame(
        dx,
        columns=['protime', 'bilirubin', 'class']
    )

    c = alt.Chart(df3).mark_circle().encode(
        x='protime', y='bilirubin', size='class', color='class', tooltip=['protime', 'bilirubin', 'class'])

    st.altair_chart(c, use_container_width=True)

    st.markdown(
        f"""
                  <style>
                  .reportview-container {{
                      background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
                  }}

                  </style>
                  """,
        unsafe_allow_html=True
    )