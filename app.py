import streamlit as st
import requests
from PIL import Image
import pandas as pd

#Background
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://ivinsutah.gov/wp-content/uploads/2016/05/professional-backgrounds-for-websites3-2.jpg');
        background-size: cover;  /* Adjust as needed */
        background-repeat: no-repeat;}.css-18e3th9 {
        color: #000;  /* Change text color for main content */}.css-1v3fvcr {
        border: 2px solid #000;  /* Add border to specific elements */}</style>
    """,
    unsafe_allow_html=True)

#Logo
image = Image.open('Logo/Logo_round.png')
st.logo(image, )

#Title
st.markdown("<h1 style='text-align: center; color: white;'>Alzheimer's Detection Tool</h1>", unsafe_allow_html=True)

#Style upload Button (does not work yet)
st.markdown(
    """
    <style>
    .stFileUpload > label {display: inline-block;
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 5px;
        cursor: pointer;}
    .stFileUpload > label:hover {background-color: #45a049;}
    .stFileUpload > div {display: none;}
    </style>
    """,
    unsafe_allow_html=True)

#Upload Button
uploaded_image = st.file_uploader("Upload MRI scan", type='jpg',
                 accept_multiple_files=False,
                 disabled=False,
                 label_visibility="collapsed")

#devide website in two columns
columns = st.columns(2)

if uploaded_image is not None:

    # When the user clicks the 'Predict' button
    if st.button("Get diagnosis"):
        files = {"img": uploaded_image.getvalue()}
        response = requests.post("https://alzheimers-api-g5wnkiowzq-ew.a.run.app/upload_image", files=files)

        if response.status_code == 200:
            #get predicton
            response_json = response.json()
            data_series = pd.Series([response_json['mild'], response_json['none'], response_json['very_mild']], index=["Mild Alzheimer's", "No Alzheimer's", "Very mild Alzheimer's"])
            data_df = pd.DataFrame(data_series, columns=['Probability'])
            data_df = data_df.sort_values(by='Probability', ascending=False)
            index_of_max = data_df['Probability'].idxmax()
            #Prediction output
            columns[1].write(f'**Diagnosis:  {index_of_max}**')
            with st.expander("Click for detailed information"): ### does not work yet
                columns[1].write(data_df)
            #columns[1].bar_chart(data_series)

        else:
            columns[1].st.write("Error:", response.text)

    #show the uploaded image
    image = Image.open(uploaded_image)
    columns[0].image(image, caption='Uploaded MRI Scan.', use_column_width=True, width=10)
    ##
