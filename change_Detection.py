# change detection and pop up

import numpy as np
import pandas as pd
import streamlit as st
import base64
import altair as alt

def app():


    st.header('HEPATITIS ANALSYSIS BLA BLA BLA BLA BLA BLA ')
    st.subheader('BLA BLA BLA BLA BLA BLA BLA ')


    df = pd.DataFrame(
        np.random.randn(200,3),
        columns= ['a', 'b', 'c']
    )

    c = alt.Chart(df).mark_circle().encode(
    x = 'a', y = 'b', size = 'c', color = 'c', tooltip = ['a', 'b', 'c'])

    st.altair_chart(c, use_container_width=True)

    st.markdown("""
        <style>
        body {
            color: blue;
            background-color: #FFFF00;
        }
        </style>
            """, unsafe_allow_html=True)