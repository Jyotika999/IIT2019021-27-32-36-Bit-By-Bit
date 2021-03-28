# homepage.py

import streamlit as st
import base64


def app():

    #st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")[image]

    # uploaded_file = st.file_uploader("safety.jpg", type="jpg")
    #
    # if uploaded_file is not None:
    #     # Convert the file to an opencv image.
    #     file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    #     opencv_image = cv2.imdecode(file_bytes, 1)
    #
    #     # Now do something with the image! For example, let's display it:
    #     st.image(opencv_image, channels="BGR")

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

    main_bg = "back.png"
    main_bg_ext = "back.png"

    side_bg = "back.png"
    side_bg_ext = "back.png"

    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
        }}
       .sidebar .sidebar-content {{
            background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
        <style>
        .sidebar .sidebar-content {

        color: #35b7aa;
        background-color: #35b7aa;
    }
        </style>
            """, unsafe_allow_html=True)

    st.title('HEPATITIS DATASET ANALYSIS AND VISUALISATION ')
    st.subheader('About Hepatitis')
    st.write(
        'Viral hepatitis is liver inflammation due to a viral infection.It may present in acute form '
        'as a recent infection with relatively rapid onset, or in chronic form.'
        'Hepatitis viruses are the most common cause of hepatitis in the world but other infections, toxic '
        'substances (e.g. alcohol, certain drugs), and autoimmune diseases can also cause hepatitis.')

    col1, mid, col2 = st.beta_columns([10, 8, 20])
    with col1:
        st.image('images/hepatitis1.jpg', width=320)
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
        st.image('images/hepatitisB.jpg', width=320)
    with col1:
        st.write('There are 5 main hepatitis viruses, referred to as types A, B, C, D and E. These 5 types are of '
                 'greatest concern because of the burden of illness and death they cause and the potential for '
                 'outbreaks and epidemic spread. In particular, types B and C lead to chronic disease in hundreds'
                 'of millions of people and, together, are the most common cause of liver cirrhosis and cancer.')

    st.subheader('About This app')
    st.write('This applications aims at analysing the various trends in hepatitis viruses along with their analysis '
             'and visualisation and EDA analysis. You can also check the possibilities of survival and death of a '
             'patient by inputing various values of some necessary fields. This application intends to help in '
             'prediction and plotting correlation matrix along with graphical analysis of data over the past trends, '
             'in hepatitis patients. It also detects drastic changes in the changing trends of the models.')
