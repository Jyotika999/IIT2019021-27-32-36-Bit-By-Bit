# homepage.py

import streamlit as st
import base64


def app():



    @st.cache(allow_output_mutation=True)
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    # def set_png_as_page_bg(png_file):
    #     bin_str = get_base64_of_bin_file(png_file)
    #     page_bg_img = '''
    #     <style>
    #     body {
    #     background-image: url("data:image/png;base64,%s");
    #     background-size: cover;
    #     }
    #     </style>
    #     ''' % bin_str
    #
    #     st.markdown(page_bg_img, unsafe_allow_html=True)
    #     return
    #
    # set_png_as_page_bg('imag1.png')

    main_bg = "images/back.png"
    main_bg_ext = "images/back.png"



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

    st.markdown("<h1 style='text-align: center; color: #7b113a;'>HEPATITIS DATASET ANALYSIS AND VISUALISATION </h1>", unsafe_allow_html=True)
    st.subheader('**ABOUT HEPATITIS**')
    st.write(
        'Viral hepatitis is liver inflammation due to a viral infection.It may present in acute form '
        'as a recent infection with relatively rapid onset, or in chronic form.'
        'Hepatitis viruses are the most common cause of hepatitis in the world but other infections, toxic '
        'substances (e.g. alcohol, certain drugs), and autoimmune diseases can also cause hepatitis.')

    col1, mid, col2 = st.beta_columns([10, 8, 20])
    with col1:
        st.image('images/bacteria.png', width=320)
    with col2:
        st.write('There are 5 main hepatitis viruses, referred to as types A, B, C, D and E. These 5 types are of '
                 'greatest concern because of the burden of illness and death they cause and the potential for '
                 'outbreaks and epidemic spread. In particular, types B and C lead to chronic disease in hundreds'
                 'of millions of people and, together, are the most common cause of liver cirrhosis and cancer.')
    st.write(
        'Viral hepatitis is liver inflammation due to a viral infection.It may present in acute form '
        'as a recent infection with relatively rapid onset, or in chronic form.'
        'Hepatitis viruses are the most common cause of hepatitis in the world but other infections, toxic '
        'substances (e.g. alcohol, certain drugs), and autoimmune diseases can also cause hepatitis.')

    col1, mid, col2 = st.beta_columns([20, 1, 20])
    with col2:
        st.image('images/virus.png', width=320)
    with col1:
        st.write('There are 5 main hepatitis viruses, referred to as types A, B, C, D and E. These 5 types are of '
                 'greatest concern because of the burden of illness and death they cause and the potential for '
                 'outbreaks and epidemic spread. In particular, types B and C lead to chronic disease in hundreds'
                 'of millions of people and, together, are the most common cause of liver cirrhosis and cancer.')

    st.subheader('**ABOUT THIS APP**')
    st.write('This applications aims at analysing the various trends in hepatitis viruses along with their analysis '
             'and visualisation and EDA analysis. You can also check the possibilities of survival and death of a '
             'patient by inputing various values of some necessary fields. This application intends to help in '
             'prediction and plotting correlation matrix along with graphical analysis of data over the past trends, '
             'in hepatitis patients. It also detects drastic changes in the changing trends of the models.\n\n\n'
             'Our software is made for the sole purpose of contributing to the medical field. It provides analysis '
             'and visualization of the previous trends of hepatitis disease seen in patients of different age, gender '
             'and various other attributes like intake of antivirals, steroid etc. It detects changes and gives pop up '
             'notifications in the previous trends. It also displays correlation matrix for various attributes.')
