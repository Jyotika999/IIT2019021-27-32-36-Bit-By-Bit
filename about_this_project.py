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
            background: #E55D87;  /* fallback for old browsers */
background: -webkit-linear-gradient(to right, #5FC3E4, #E55D87);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #5FC3E4, #E55D87); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

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

    # st.title('ABOUT OUR SOFTWARE ')
    st.markdown("<h1 style='text-align: center; color: #7b113a;'>ABOUT THE SOFTWARE</h1>",
                unsafe_allow_html=True)
    # st.write('ADD MORE DETAILS ABOUT WHAT OUR PROJECT CAN DO')
    st.write('Our software is made for the sole purpose of contributing to the medical field. It provides analysis and visualization of the previous trends of hepatitis disease seen in patients of different age, gender and various other attributes like intake of antivirals, steroid etc. It detects changes and gives pop up notifications in the previous trends. It also displays correlation matrix for various attributes.\n\n\n\nThis app is a collaboration work of Jyotika, Vidushi, Aarushi and Medha from IIIT Allahabad.')
