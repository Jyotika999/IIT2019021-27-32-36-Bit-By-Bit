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

    df = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c']
    )

    c = alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

    st.altair_chart(c, use_container_width=True)

    st.markdown("""
        <style>
        body {
            color: #F5F5F5;
            background-color: #b19cd9;
        }
        </style>
            """, unsafe_allow_html=True)
