# change detection and pop up

import numpy as np
import pandas as pd
import streamlit as st
import base64
import altair as alt


def app():
    st.header('Change in Trends and Values')
    st.subheader('About')
    st.write('On the test data when a change is encountered which does not follow the regular flow in th pattern'
             'this show the pop up message accordingly')

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

    st.markdown("""
        <style>
        body {
            color: #F5F5F5;
            background-color: #b19cd9;
        }
        </style>
            """, unsafe_allow_html=True)
