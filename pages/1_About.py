import streamlit as st
from PIL import Image, ImageOps

st.set_page_config(page_title="About", page_icon=":material/info:")

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

# Logo
image = Image.open('../alzheimers-detection-website/Logo/Logo_round.png')
st.logo(image, )

# Header image
#st.image('https://aboutimi.com/wp-content/uploads/2021/06/Brain.jpeg')

#Title
st.markdown("<h1 style='text-align: center; color: black;'>About this Project</h1>", unsafe_allow_html=True)

# Sub-Header
st.subheader("Learn more about the background of this project to detect alzheimer's disease in an early stage")




st.markdown(
    """
    This project utilizes transfer learning with the VGG-19 model to classify MRI images of the brain.
    The model aims to accurately identify specific features or conditions present in the central axial slice of brain MRI scans.
    The model predicts three classes: Non-demented, very mild dementia, and mild dementia.
    ### Model
    The model uses the VGG-19 architecture with pre-trained weights from ImageNet. The top layers of VGG-19 are fine-tuned to adapt to the MRI classification task.

    **Model Performace**
    - Loss: 0.756
    - Accuracy: 0.685
    - Recall: 0.659
    - Precision: 0.711

    ### Want to learn more?
    - Check out our [github repo](https://github.com/murasovl/alzheimers-detection)
    - Explore the [Alzheimer's Dataset](https://www.kaggle.com/datasets/tourist55/alzheimers-dataset-4-class-of-images)
"""
)

#Group picture
st.markdown('''### The Team''')
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12 = st.columns(12)
image = Image.open('Group/group_pic2.JPG')
image = ImageOps.exif_transpose(image)
st.image(image, width=500)
