import streamlit as st
import requests
from PIL import Image


st.markdown('''
Website first draft
''')

uploaded_image = st.file_uploader("Upload a MRI scan", type='jpg',
                 accept_multiple_files=False,
                 key=None,
                 help=None,
                 on_change=None,
                 args=None,
                 kwargs=None,
                 disabled=False,
                 label_visibility="visible")



if uploaded_image is not None:

    # When the user clicks the 'Predict' button
    if st.button("Predict"):
        files = {"img": uploaded_image.getvalue()}
        response = requests.post("https://alzheimers-api-g5wnkiowzq-ew.a.run.app/upload_image", files=files)

        if response.status_code == 200:
            st.write(response.json())
        else:
            st.write("Error:", response.text)

    #show the uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption='Your uploaded MRI Scan.', use_column_width=True)
    ##
