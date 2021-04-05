# homepage.py
import streamlit as st
import base64
import warnings
warnings.filterwarnings("ignore")


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
    st.markdown("<h1 style='text-align: center; color: #7b113a;'>Models Used:</h1>",
                unsafe_allow_html=True)
    # st.title('Models used:')
    # st.write('add info about three models we have used for prediction')
    st.write('Decision Tree Model: A decision tree is a machine learning algorithm that partitions the data into subsets.'
             'The partitioning process starts with a binary split and continues until no further splits can be made.' 
             'Various branches of variable length are formed. The several steps involved are: Splitting, Pruning and Tree Selection.')
    st.write('\n')
    st.write('KNN Model: The k-nearest neighbors (KNN) algorithm is a simple, easy-to-implement supervised machine learning algorithm' ''
             'that can be used to solve both classification and regression problems. Steps involed are:')
    st.write('Load the data, Initialize K to your chosen number of neighbors, For each example in the data,' 
             'Calculate the distance between the query example and the current example from the data, Add the distance' 
             'and the index of the example to an ordered collection,  Sort the ordered collection of distances and indices' 
             'from smallest to largest (in ascending order) by the distances, Pick the first K entries from the sorted collection,' 
             'Get the labels of the selected K entries, If regression, return the mean of the K labels, If classification, return the mode of the K labels.')
    st.write('\n')
    st.write('Logistic Regression: Logistic Regression is a Machine Learning algorithm which is used for the classification problems,' 
             'it is a predictive analysis algorithm and based on the concept of probability.')