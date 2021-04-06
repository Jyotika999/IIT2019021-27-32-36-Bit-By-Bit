import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')
import streamlit as st
import seaborn as sns
import joblib
import os
import lime
import lime.lime_tabular


def app():
    feature_names_best = ['age', 'sex', 'steroid', 'antivirals', 'fatigue', 'spiders', 'ascites', 'varices',
                          'bilirubin', 'alk_phosphate', 'sgot', 'albumin', 'protime', 'histology']
    gender_dict = {"male": 1, "female": 2}
    feature_dict = {"No": 1, "Yes": 2}

    def get_value(val, my_dict):
        for key, value in my_dict.items():
            if val == key:
                return value

    def get_key(val, my_dict):
        for key, value in my_dict.items():
            if val == key:
                return key

    def get_fvalue(val):
        feature_dict = {"No": 1, "Yes": 2}
        for key, value in feature_dict.items():
            if val == key:
                return value

    # Load ML Models
    def load_model(model_file):
        loaded_model = joblib.load(open(os.path.join(model_file), "rb"))
        return loaded_model

    st.title("Mortality Prediction")
    st.subheader("Predictive Analysis")

    age = st.number_input("Age", 7, 80)
    sex = st.radio("Sex", tuple(gender_dict.keys()))
    steroid = st.radio("Do You Take Steroids?", tuple(feature_dict.keys()))
    antivirals = st.radio("Do You Take Antivirals?", tuple(feature_dict.keys()))
    fatigue = st.radio("Do You Have Fatigue", tuple(feature_dict.keys()))
    spiders = st.radio("Presence of Spider Naevi", tuple(feature_dict.keys()))
    ascites = st.selectbox("Ascitis", tuple(feature_dict.keys()))
    varices = st.selectbox("Presence of Varices", tuple(feature_dict.keys()))
    bilirubin = st.number_input("bilirubin Content", 0.0, 8.0)
    alk_phosphate = st.number_input("Alkaline Phosphate Content", 0.0, 296.0)
    sgot = st.number_input("Sgot", 0.0, 648.0)
    albumin = st.number_input("Albumin", 0.0, 6.4)
    protime = st.number_input("Prothrombin Time", 0.0, 100.0)
    histology = st.selectbox("Histology", tuple(feature_dict.keys()))

    feature_list = [age, get_value(sex, gender_dict), get_fvalue(steroid), get_fvalue(antivirals), get_fvalue(fatigue),
                    get_fvalue(spiders), get_fvalue(ascites), get_fvalue(varices), bilirubin, alk_phosphate, sgot,
                    albumin, int(protime), get_fvalue(histology)]
    st.write(len(feature_list))
    result = {"age": age, "sex": sex, "steroid": steroid, "antivirals": antivirals, "fatigue": fatigue,
              "spiders": spiders, "ascites": ascites, "varices": varices, "bilirubin": bilirubin,
              "alk_phosphate": alk_phosphate, "sgot": sgot, "albumin": albumin, "protime": protime,
              "histolog": histology}
    st.json(result)
    single_sample = np.array(feature_list).reshape(1, -1)

    model_choice = st.selectbox("Select Model", ["LR", "KNN", "DecisionTree"])

    if st.button("Predict"):
        if model_choice == "KNN":
            loaded_model = load_model("model/knn_hepB_model.pkl")
            prediction = loaded_model.predict(single_sample)
            pred_prob = loaded_model.predict_proba(single_sample)
        elif model_choice == "DecisionTree":
            loaded_model = load_model("model/decision_tree_clf_hepB_model.pkl")
            prediction = loaded_model.predict(single_sample)
            pred_prob = loaded_model.predict_proba(single_sample)
        else:
            loaded_model = load_model("model/logistic_regression_hepB_model.pkl")
            prediction = loaded_model.predict(single_sample)
            pred_prob = loaded_model.predict_proba(single_sample)

        # st.write(prediction)
        # prediction_label = {"Die":1,"Live":2}
        # final_result = get_key(prediction.prediction_label)
        if prediction == 1:
            st.warning("Patient Dies")
            pred_probability_score = {"Die": pred_prob[0][0] * 100, "Live": pred_prob[0][1] * 100}
            st.subheader("Prediction Probability Score using {}".format(model_choice))
            st.json(pred_probability_score)
            st.subheader("Prescriptive Analytics")
        else:
            st.success("Patient Lives")
            pred_probability_score = {"Die": pred_prob[0][0] * 100, "Live": pred_prob[0][1] * 100}
            st.subheader("Prediction Probability Score using {}".format(model_choice))
            st.json(pred_probability_score)

    if st.checkbox("Interpret"):
        if model_choice == "KNN":
            loaded_model = load_model("model/knn_hepB_model.pkl")

        elif model_choice == "DecisionTree":
            loaded_model = load_model("model/decision_tree_clf_hepB_model.pkl")

        else:
            loaded_model = load_model("model/logistic_regression_hepB_model.pkl")

            # loaded_model = load_model("models/logistic_regression_model.pkl")
            # 1 Die and 2 Live
            df = pd.read_csv("Dataset/hepatitis.csv")
            x = df[['age', 'sex', 'steroid', 'antivirals', 'fatigue', 'spiders', 'ascites', 'varices', 'bilirubin',
                    'alk_phosphate', 'sgot', 'albumin', 'protime', 'histology']]
            feature_names = ['age', 'sex', 'steroid', 'antivirals', 'fatigue', 'spiders', 'ascites', 'varices',
                             'bilirubin', 'alk_phosphate', 'sgot', 'albumin', 'protime', 'histology']
            class_names = ['Die(1)', 'Live(2)']
            explainer = lime.lime_tabular.LimeTabularExplainer(x.values, feature_names=feature_names,
                                                               class_names=class_names, discretize_continuous=True)
            # The Explainer Instance
            exp = explainer.explain_instance(np.array(feature_list), loaded_model.predict_proba, num_features=13,
                                             top_labels=1)
            exp.show_in_notebook(show_table=True, show_all=False)
            # exp.save_to_file('lime_oi.html')
            st.write(exp.as_list())
            new_exp = exp.as_list()
            label_limits = [i[0] for i in new_exp]
            # st.write(label_limits)
            label_scores = [i[1] for i in new_exp]
            plt.barh(label_limits, label_scores)
            st.pyplot()
            plt.figure(figsize=(20, 10))
            fig = exp.as_pyplot_figure()
            st.pyplot()

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
