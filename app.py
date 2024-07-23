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

#Output style
st.markdown("""
<style>
.big-font {font-size:300px !important;}
</style>
""",
unsafe_allow_html=True)

#Logo
image = Image.open('Logo/Logo_round.png')
st.logo(image, )

#Title
st.markdown("<h1 style='text-align: center; color: white;'>Alzheimer's Detection Tool</h1>", unsafe_allow_html=True)


#Upload Button
uploaded_image = st.file_uploader("Upload MRI scan", type='jpg',
                 accept_multiple_files=False,
                 disabled=False,
                 label_visibility="collapsed")

#devide website in three columns
columns = st.columns(5)
c = st.columns(3)
col1, col2, col3,col4, col5 = st.columns(5)

if uploaded_image is not None:

    # When the user clicks the 'Predict' button
    if columns[2].button("Get diagnosis"):
        files = {"img": uploaded_image.getvalue()}
        response = requests.post("https://alzheimers-api-g5wnkiowzq-ew.a.run.app/upload_image", files=files)

        if response.status_code == 200:
            #get predicton
            response_json = response.json()
            data_series = pd.Series([response_json['mild'], response_json['none'], response_json['very_mild']], index=["Risk of Alzheimer's Disease (stage: mild)", "Healthy", "Risk of Alzheimer's Disease (stage: very mild)"])
            data_df = pd.DataFrame(data_series, columns=['Probability'])
            data_df = data_df.sort_values(by='Probability', ascending=False)
            index_of_max = data_df['Probability'].idxmax()
            #Prediction output
            columns[2].markdown(f'<p style="font-size:18px;"><strong>{index_of_max}</strong></p>', unsafe_allow_html=True)
            with st.expander("Click for information about probability:"):
                st.write(data_df)
            #with st.expander("Click for information about probability:"):
                #st.write('Probability distribution')
                #st.write(f'Healthy: {data_df.loc['Healthy', 'Probability']}')
            with st.expander("Click for information about diagnosis"):
                st.warning('Warning')
                st.write('Text about diagnosis')
            #st.bar_chart(data_series)

        else:
            st.write("Error:", response.text)

    #show the uploaded image
    col1, col2, col3,col4, col5 = st.columns(5)

    with col1:
        st.write(' ')

    with col2:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded MRI Scan.', width=400)

    with col3:
        st.write(' ')
