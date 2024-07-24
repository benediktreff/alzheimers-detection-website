import streamlit as st
import requests
from PIL import Image
import pandas as pd

st.set_page_config(page_title="Diagnosis", page_icon=":material/neurology:")

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
st.logo(image)
logo_css = """
<style>
  div[data-testid="stSidebarHeader"] > img,
  div[data-testid="collapsedControl"] > img
  {height: 2rem;width: auto;
</style>
"""
st.markdown(logo_css, unsafe_allow_html=True)

#Title
st.markdown("<h1 style='text-align: center; color: white;'>Alzheimer's Detection Tool</h1>", unsafe_allow_html=True)

#Upload Button
uploaded_image = st.file_uploader("Upload MRI scan", type='jpg',
                 accept_multiple_files=False,
                 disabled=False,
                 label_visibility="collapsed")

#devide website in columns
columns = st.columns(5)
c = st.columns(3)



if uploaded_image is not None:
    # When the user clicks the 'Predict' button
    if columns[2].button("Get diagnosis"):
        files = {"img": uploaded_image.getvalue()}
        response = requests.post("https://alzheimers-api-g5wnkiowzq-ew.a.run.app/upload_image", files=files)

        if response.status_code == 200:
            #get predicton
            response_json = response.json()
            data_series = pd.Series([round(response_json['mild'],3)*100, round(response_json['none'],3)*100, round(response_json['very_mild'],3)*100], index=["Risk of Alzheimer's Disease (stage: mild)", "Healthy", "Risk of Alzheimer's Disease (stage: very mild)"])
            #Create output DataFrame
            data_df = pd.DataFrame(data_series, columns=['Probability (%)'])
            data_df = data_df.sort_values(by='Probability (%)', ascending=False)
            index_of_max = data_df['Probability (%)'].idxmax()
            #Diagnosis output
            st.markdown(f"""
            <div style="border: 1px solid black; padding: 8px; background-color: #f0f0f0; border-radius: 3px;">
                <h1 style="text-align: center; font-size: 18px;">Diagnosis: {index_of_max}</h1>
            </div>
            """,unsafe_allow_html=True)
            st.markdown('')
            st.markdown('')
            st.markdown('')
            #Expander DataFrame
            with st.expander("Details about probability distribution"):
                st.write(data_df)
            #Expander Explanations
            with st.expander("Details about diagnosis"):
                st.warning("**Disclaimer:** This model has been developed as a tool to assist doctors. Any diagnosis should not be made without consultation with a qualified medical professional.")
                if index_of_max == 'Healthy':
                    st.write(f"With an accuracy of {str(response_json['none']*100)[:5]}%, it is recommended to refer the patient to a specialist in neurology or psychiatry to confirm that Alzheimer's disease can be excluded from the diagnosis.")
                if index_of_max == "Risk of Alzheimer's Disease (stage: mild)":
                    st.write(f"The model predicts mild dementia with an accuracy of {str(response_json['mild']*100)[:5]}%. It is urged to refer the patient to a specialist in neurology or psychiatry to confirm the illness and the stage. Since the model has been trained to predict the three stages (Non-demented, Very Mild Dementia, Mild Dementia), it is important to be aware that the actual stage might also be moderate or even more advanced.")
                if index_of_max == "Risk of Alzheimer's Disease (stage: very mild)":
                    st.write(f"The model predicts very mild dementia with an accuracy of {str(response_json['very_mild']*100)[:5]}%. It is advised to consult a specialist in neurology or psychiatry to confirm the stage of dementia. While the model is trained to predict this stage, further medical evaluation is necessary to determine the precise condition.")

        else:
            st.write("Error:", response.text)

    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
    with col4:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded MRI Scan.', width=250)

#SHAPLEY VALUES:

    try:
        url = "https://alzheimers-api-g5wnkiowzq-ew.a.run.app/shap"
        files = {"img": uploaded_image.getvalue()}
        res = requests.post(url, files=files)
        if res.status_code == 200:
            #if columns[2].button("Get explanation"): # das sieht richtig schlecht aus
            with st.expander("Get explanation"):
                st.image(res.content, caption="Shapley explaination.")
        else:
            st.write("Error:", res.text)
    except Exception as e:
        st.error(f"An error occurred: {e}")