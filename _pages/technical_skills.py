from streamlit_pills import pills
import json
# Function to load a JSON file

with open(r'data/technical_skills.json') as file:
    description = json.load(file)

right_column, left_column = st.columns([2, 1])
with right_column:
    st.title("Skills Técnicas")
    skills = [
    "Oracle Fusion Financials",
    "Oracle Fusion HCM",
    "Oracle Integration Cloud (OIC)",
    "Visual Builder Cloud Service (VBCS)",
    "Oracle Cloud Infrastructure (OCI)",
    "Oracle Digital Assistant",
    "Oracle Blockchain Platform",
    "Oracle Gen AI",
    "Python",
    "Javascript",
    "SQL",
    "PL/SQL",
    "SaaS",
    "PaaS",
    "Arquitetura Cloud Native",
    "CI/CD",
    "ALM (Application Lifecycle Management)",
    "Metodologias Ágeis",
    "VBS (Visual Builder Studio)",
    "BI Publisher",
    "Integração de Dados",
    "Análise de Dados",
    "IA Generativa",
    "LLMs (Large Language Models)",
    "Langchain",
    "Langsmith",
    "Bancos de Dados Vetoriais",
    "Machine Learning",
    "SSO (Single Sign-On)",
    "MFA (Autenticação Multifator)",
    "API (Interface de Programação de Aplicações)",
    "REST API",
    "SOAP",
    "sFTP (Protocolo Seguro de Transferência de Arquivos)",
    "UX/UI Design",
    "Node.js",
    "Express.js",
    "MongoDB",
    "DynamoDB",
    "NoSQL",
    "OTBI (Oracle Transactional Business Intelligence)",
    "Java",
    "Desenvolvimento Mobile",
    "Docker",
    "APEX (Oracle Application Express)",
    ".NET",
    "C#",
    "Kotlin",
    "Swift",
    "Embeddings",
    "Prompt Engineering",
    "Streamlit",
    "Gradio",
    "Soluções Multimodais",
    "AWS Bedrock",
    "Retool",
    "FastAPI",
    "GCP - Google Cloud Platform"
  ]
    selected = pills("Selecione uma categoria", skills)
with left_column:
    st.title("Detalhes")
    for skill in description["skills"]:
        if selected==skill["name"]:
            st.markdown(skill["description"])