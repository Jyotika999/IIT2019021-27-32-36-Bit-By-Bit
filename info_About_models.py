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

    st.title('info about models')
    st.write('add info about three models we have used for prediction')
