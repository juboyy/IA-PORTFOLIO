import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
st.title("Conquistas")
Rage_badge = """

"""
Hope_Badge = """"""
Keyholders_badge = """"""
Azure_fundamentals = """"""

# Seção Certificações
st.header("📜 Certificações")

# Criando um dataframe para as certificações
certifications_data = {
    "Provedor": ["Oracle", "AWS", "Oracle", "Oracle", "Oracle", "Oracle", "Oracle", "Oracle"],
    "Stack": ["OCI Generative AI Certified Professional", "Project Planning for Multicloud Solutions", "Oracle Cloud Certified Integration Specialist", "OCI Certified Application Integration Professional", "OCI Certified Digital Assistant Professional", "Certified Solution Engineer for Digital Assistant and Machine Learning", "Oracle Autonomous Database Specialist", "Oracle Blockchain Platform"],
    "Concedido": ["2024", "N/A", "2022", "2023", "N/A", "N/A", "N/A", "N/A"],
    "Expiração": ["2025", "N/A", "N/A", "2024", "N/A", "N/A", "N/A", "N/A"]
}

certifications_df = pd.DataFrame(certifications_data)
st.table(certifications_df)
#Badge Section
st.header("🏅Badges")
col1, col2, col3, col4 = st.columns(4)

with col1:
    components.html(Rage_badge, height=270, width=165)
with col2:
    components.html(Hope_Badge, height=270, width=165)
with col3:
    components.html(Keyholders_badge, height=270, width=165)
with col4:
    components.html(Azure_fundamentals, height=270, width=165)
