import streamlit as st
import requests
from PIL import Image


st.markdown('''
Website first draft
''')

uploaded_image = st.file_uploader("Upload a MRI scan", type=None,
                 accept_multiple_files=False,
                 key=None,
                 help=None,
                 on_change=None,
                 args=None,
                 kwargs=None,
                 disabled=False,
                 label_visibility="visible")



if uploaded_image is not None:

    #show the uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    ##

    bytes_data = uploaded_image.read()
    alzheimers_url = 'https://alzheimers-api-g5wnkiowzq-ew.a.run.app/docs#/default/receive_image_upload_image_post'
    response = requests.post(alzheimers_url, files={"file": bytes_data})

    prediction = response.json()
    #mild = prediction['mild']
    #very_mild = prediction['very_mild']
    #none = prediction['none']

    #st.write(f"Prop. mild: {mild}")

    st.write(prediction)
