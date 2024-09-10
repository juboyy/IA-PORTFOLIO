import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Portfólio do João",
    page_icon="desktop_computer",
    layout="wide",
    initial_sidebar_state="auto",
)
with st.sidebar:
    choose = option_menu(
        "João Rafael",
        [
            "Speky",
            "Sobre Mim",
            "Experiência",
            "Habilidades Técnicas",
            "Educação",
            "Conquistas",
            "Contato",
        ],
        icons=[
            "robot",
            "person fill",
            "clock history",
            "tools",
            "book half",
            "clipboard",
            "trophy fill",
            "heart",
            "pencil square",
            "envelope",
        ],
        menu_icon="mortarboard",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#0D1117"},
            "icon": {"color": "darkorange", "font-size": "20px"},
            "nav-link": {
                "font-size": "17px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#1F2937",
            },
            "nav-link-selected": {"background-color": "#A41117"},
        },
    )
    st.markdown(
    "<div style='text-align: center;'>"
    "<a href='https://www.linkedin.com/in/jo%C3%A3o-soares-716400229/'><img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' width='40'></a>"
    "&nbsp;&nbsp;&nbsp;&nbsp;"
    "<a href='https://github.com/'><img src='https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg' width='40'></a>"
    "&nbsp;&nbsp;&nbsp;&nbsp;"
    "<a href='mailto:finess.org@gmail.com'><img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png' width='40'></a>"
    "</div>",
    unsafe_allow_html=True,
)

pages = {
    "Speky": "_pages/home.py",
    "Sobre Mim": "_pages/About_Me.py",
    "Experiência": "_pages/Experience.py",
    "Habilidades Técnicas": "_pages/technical_skills.py",
    "Educação": "_pages/Education.py",
    "Conquistas": "_pages/Achivements.py",
    "Contato": "_pages/Contact.py",
}

# Carrega dinamicamente a página selecionada
page_file = pages.get(choose)
if page_file:
    with open(page_file, encoding="utf-8") as file:
        exec(file.read())
