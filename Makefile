install_requirements:
	@Pip install -r requirements.txt

streamlit:
	-@streamlit run Diagnosis.py
