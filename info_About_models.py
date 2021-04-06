# homepage.py
import streamlit as st
import base64
import warnings
warnings.filterwarnings("ignore")
from PIL import Image


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

    main_bg = "images/back.png"
    main_bg_ext = "images/back.png"

    side_bg = "images/back.png"
    side_bg_ext = "images/back.png"

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
    st.markdown("<h1 style='text-align: center; color: #7b113a;'>Models Used</h1>",
                unsafe_allow_html=True)

    st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # st.title('Models used:')
    # st.write('add info about three models we have used for prediction')
    st.subheader('**KNN Model:** ')
    img = Image.open("images/knn.png")
    st.image(img, width=700, caption='Hepatitis Virus')
    st.markdown('<p class="big-font">The k-nearest neighbors (KNN) algorithm is a simple, easy-to-implement supervised machine learning algorithm that can be used to solve both classification and regression problems. Steps involed are:</p>', unsafe_allow_html=True)

    st.write('\n')

    st.markdown('<p class = "big-font">Load the data, Initialize K to your chosen number of neighbors, For each example in the data, Calculate the distance between the query example and the current example from the data, Add the distance and the index of the example to an ordered collection,  Sort the ordered collection of distances and indices from smallest to largest (in ascending order) by the distances, Pick the first K entries from the sorted collection, Get the labels of the selected K entries, If regression, return the mean of the K labels, If classification, return the mode of the K labels.</p>', unsafe_allow_html=True)
    st.write('\n')


    st.subheader('**SVM Model:** ')
    img = Image.open("images/SVM.png")
    st.image(img, width=700, caption='SVM')
    st.markdown('<p class="big-font">Support Vector Machine” (SVM) is a supervised machine learning algorithm which can be used for both classification or regression challenges. However,  it is mostly used in classification problems. In the SVM algorithm, we plot each data item as a point in n-dimensional space (where n is number of features you have) with the value of each feature being the value of a particular coordinate. Then, we perform classification by finding the hyper-plane that differentiates the two classes very well.</p>', unsafe_allow_html=True)
    st.write('\n')

    st.subheader('**Naive Bayes Model:** ')
    img = Image.open("images/NB.jpg")
    st.image(img, width=700, caption='Naive bayes')
    st.markdown('<p class="big-font">It is a classification technique based on Bayes’ Theorem with an assumption of independence among predictors. In simple terms, a Naive Bayes classifier assumes that the presence of a particular feature in a class is unrelated to the presence of any other feature.Naive Bayes model is easy to build and particularly useful for very large data sets. Along with simplicity, Naive Bayes is known to outperform even highly sophisticated classification methods</p>', unsafe_allow_html=True)