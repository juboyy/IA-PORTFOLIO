# Define the left and right columns
right_column, left_column = st.columns([1, 2])
with right_column:
    st.markdown("<br>", unsafe_allow_html=True)
    st.image(r"images/profile.png", use_column_width=True)

with left_column:
    st.title("Sobre mim")
    st.markdown(
        "<div style='text-align: justify'>"
        "Olá! Sou o João Rafael, entusiasta em tecnologia, blockchain e IA. Com um extenso histórico em TI, adoro enfrentar desafios e descobrir soluções inovadoras."
        "<br>"
        "Amo trabalhar em equipe e sempre me diverti com a comunidade e clubes de desenvolvedores. Manter a calma sob pressão e prestar atenção aos pequenos detalhes me ajuda a entregar resultados de qualidade sempre."
        "<br>"
        "Tecnologia e IA são minhas paixões, e estou constantemente explorando maneiras de aprimorar operações tecnológicas e soluções inteligentes de IA. 🕵️‍♂️ Meu objetivo é contribuir para o desenvolvimento de tecnologias seguras e inovadoras que façam a diferença."
        "<br>"
        "Quando não estou envolvido com tecnologia, você me encontrará jogando futebol ⚽, fazendo trilhas ⛰️, malhando na academia 💪 ou desfrutando de boa comida🍴. Acredito em manter um equilíbrio saudável entre trabalho e vida para me manter inspirado."
        "<br>"
        "Obrigado por visitar meu portfólio! Vamos nos conectar e explorar juntos o emocionante mundo da tecnologia🚀"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div style='text-align: justify'>"
        "<br>"
        "<a href='https://www.linkedin.com/in/jo%C3%A3o-soares-716400229/'><img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' width='40'></a>"
        "&nbsp;&nbsp;&nbsp;&nbsp;"
        "<a href='https://github.com/juboyy'><img src='https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg' width='40'></a>"
        "&nbsp;&nbsp;&nbsp;&nbsp;"
        "<a href='mailto:finess.org@gmail.com'><img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png' width='40'></a>"
        "</div>",
        unsafe_allow_html=True,
    )
