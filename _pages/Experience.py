import reveal_slides as rs

sample_markdown = r"""
# EXPERIÊNCIA NA INDÚSTRIA
Breve visão geral da minha experiência até o momento.
---

## Oracle (Brazil)
`Sr. Oracle Cloud Developer`
</br>
`Jan 2015 - Dec 2021`
<div style='text-align: justify'><b>
<li>Liderança técnica em projetos de desenvolvimento de aplicativos móveis utilizando VBCS, com foco em segurança, migração e arquitetura em nuvem. Desenvolvi soluções de transporte para o Oracle Transportation Management (OTM), integrando módulos de gestão de transporte, pedidos e sourcing.</li><br>
</b>
</div>
Tecnologias Utilizadas
--
<b>Tecnologias Utilizadas</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style='text-align: justify'>
OCI, VBCS, OIC, OTBI, SSO, MFA, IAM, Figma, Redwood Apps, Time and Labor, OTM, DevOps, VBS, Git, CI/CD
</div>
---

## Oracle (Brazil)
`Sr. Oracle Cloud Specialist Developer`
</br>
`Jan 2022 - Present`
<div style='text-align: justify'><b>
<li>Atuo como consultor especializado em soluções Oracle Cloud, com foco em integração, automação e suporte a clientes globais de diferentes setores. Desenvolvi soluções móveis para HCM e arquiteturas de segurança, incluindo SSO e MFA.</li><br>
</b>
</div>
Tecnologias Utilizadas
--
<b>Tecnologias Utilizadas</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style='text-align: justify'>
OIC, VBCS, BIP, Fusion, OCI, SSO, MFA, IAM, PL/SQL, OTBI, Redwood Apps, Time and Labor, OTM, CI/CD, Git, DevOps
</div>
---

## Oracle (Brazil)
`Sr. Oracle Cloud Engineer | Integration Specialist`
</br>
`Jul 2021 - Present`
<div style='text-align: justify'><b>
<li>Engenheiro de integração especializado em Oracle Cloud, automatizando processos de ERP globais, com foco em alta performance e confiabilidade nas operações internacionais.</li><br>
</b>
</div>
Tecnologias Utilizadas
--
<b>Tecnologias Utilizadas</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style='text-align: justify'>
sFTP, API, SOAP, EssJobs, FBDI, OIC, EDM, MFT, ERP, BI, PO, AP
</div>
---

## Oracle (Brazil)
`Sr. Oracle Cloud Engineer | Integration Specialist`
</br>
`Mar 2023 - Jun 2023`
<div style='text-align: justify'><b>
<li>Consultoria técnica em projetos de integração e automação utilizando Oracle Cloud, com foco em soluções de infraestrutura crítica para o setor bancário.</li><br>
</b>
</div>
Tecnologias Utilizadas
--
<b>Tecnologias Utilizadas</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style='text-align: justify'>
OIC, EDM, Oracle Fusion SaaS, Subscription Management, Budgetary Control, BI
</div>
---

## Oracle (Japan)
`Sr. Oracle Technical Consultant | Application Specialist`
</br>
`Nov 2020 - Jun 2021`
<div style='text-align: justify'><b>
<li>Consultor técnico em projetos de desenvolvimento e integração de sistemas Oracle, com foco em VBCS, automação e suporte a clientes internacionais, incluindo módulos financeiros como AP e GL.</li><br>
</b>
</div>
Tecnologias Utilizadas
--
<b>Tecnologias Utilizadas</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style='text-align: justify'>
VBCS, API, SOAP, EssJobs, FBDI, ALM, VBS, Javascript, ERP, BI
</div>
---

## Oracle (Brazil)
`Sr. Oracle Cloud Consultant | Application Specialist`
</br>
`Jun 2022 - Present`
<div style='text-align: justify'><b>
<li>Consultoria especializada em Oracle Cloud, atuando no desenvolvimento, integração e suporte de sistemas, com foco em VBCS, automação e metodologias ágeis. Desenvolvi um sistema de interação por QR Code para gestão de contêineres.</li><br>
</b>
</div>
Tecnologias Utilizadas
--
<b>Tecnologias Utilizadas</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style='text-align: justify'>
VBCS, API, SOAP, EssJobs, FBDI, PL/SQL, BI Publisher, sFTP, GMUD
</div>
"""

st.title("Experiências")
currState = rs.slides(
    sample_markdown,
    theme="dracula",
    height=800,
    config={
        "transition": "slide",
        "width": 1100,
        "height": 1100,
        "center": True,
        "margin": 0.10,
        "scale_range": [0.1, 3.0],
    },
    initial_state={
        "indexf": -1,
    },
    markdown_props={"data-separator-vertical": "^--$"},
    key="foo",
)
