from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import streamlit as st


pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)


# @app.route("/")
def welcome():
    return "Welcome All"


# @app.route("/predict", methods=["Get"])
def predict_note_authentication():
    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values

    """
    variance = request.args.get("variance")
    skewness = request.args.get("skewness")
    curtosis = request.args.get("curtosis")
    entropy = request.args.get("entropy")
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return "Hello The answer is" + str(prediction)


# @app.route("/predict_file", methods=["POST"])
def predict_note_file():
    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true

    responses:
        200:
            description: The output values

    """
    df_test = pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction = classifier.predict(df_test)

    return str(list(prediction))


def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:centerl"> Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    variance = st.text_input("Variance", "Type here")
    skewness = st.text_input("Skewness", "Type here")
    curtosis = st.text_input("Curtosis", "Type here")
    entropy = st.text_input("entropy", "Type here")
    result = ""

    if st.button("Predict"):
        result = predict_note_authentication(variance, skewness, curtosis, entropy)

    st.success("The output is {}".format(result))

    if st.button("About"):
        st.text("Lets learn")
        sr.text("Built with Streamlit")


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8000)
    main()


#  streamlit run appStreamlit.py
