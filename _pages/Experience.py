import reveal_slides as rs

sample_markdown = r"""
# EXPERIÊNCIA NA INDÚSTRIA
Breve visão geral da minha experiência até o momento.
---

## Ninecon
`Oracle Cloud Technical Consultant`
</br>
`Jan 2022 - Presente`
<div style='text-align: justify'><b>
<li>Atuo como consultor especializado em soluções Oracle Cloud, com foco em integração, automação e suporte a clientes globais de diferentes setores.</li><br>
</b>
</div>
Tecnologias Utilizadas
--
<b>Tecnologias Utilizadas</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style='text-align: justify'>
OIC, VBCS, BIP, Fusion, OCI, SLA, BI Publisher, PL/SQL, ALM, Metodologias Agile, ERP, HCM, CRM
</div>
---

## Oracle
`Sr. Cloud Application Specialist | Architect`
</br>
`Jan-Maio 2024`
<div style='text-align: justify'><b>
<li>Liderança técnica em projetos de desenvolvimento de aplicativos móveis utilizando VBCS, com foco em segurança, migração e arquitetura em nuvem.</li><br>
</b>
</div>
Tecnologias Utilizadas
--
<b>Tecnologias Utilizadas</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style='text-align: justify'>
VBCS, SSO, MFA, Javascript, OCI, IDCS, PaaS, SaaS, SOA, REST API, Visual Builder Cloud Service
</div>
---

## Deloitte
`Sr. Cloud Technical Consultant | Application Specialist`
</br>
`Ago 2023 - Mar 2024`
<div style='text-align: justify'><b>
<li>Consultoria técnica em projetos de integração de sistemas utilizando tecnologias Oracle Cloud, com foco em automação, suporte e entrega de soluções robustas.</li><br>
</b>
</div>
Tecnologias Utilizadas
--
<b>Tecnologias Utilizadas</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style='text-align: justify'>
sFTP, API, SOAP, EssJobs, FBDI, OCI, REST API, SOA, ERP, HCM, CRM
</div>
---

## FedEx
`Sr. Oracle Cloud Engineer | Integration Specialist`
</br>
`Ago 2023 - Mar 2024`
<div style='text-align: justify'><b>
<li>Engenheiro de integração especializado em Oracle Cloud, atuando em projetos de automação, suporte e implementação de sistemas ERP.</li><br>
</b>
</div>
Tecnologias Utilizadas
--
<b>Tecnologias Utilizadas</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style='text-align: justify'>
sFTP, API, SOAP, EssJobs, FBDI
</div>
---

## Núclea
`Sr. Oracle Cloud Engineer | Integration Specialist`
</br>
`Dez 2023 - Fev 2024`
<div style='text-align: justify'><b>
<li>Consultoria técnica em projetos de integração e automação utilizando Oracle Cloud, com foco em soluções de infraestrutura crítica para o setor bancário.</li><br>
</b>
</div>
Tecnologias Utilizadas
--
<b>Tecnologias Utilizadas</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style='text-align: justify'>
UCM, EssJobs, FBDI, Oracle Cloud
</div>
---

## NTT DATA
`Sr. Oracle Technical Consultant | Application Specialist`
</br>
`Jan 2023 - Jan 2024`
<div style='text-align: justify'><b>
<li>Consultor técnico em projetos de desenvolvimento e integração de sistemas Oracle, com foco em VBCS, automação e suporte a clientes internacionais.</li><br>
</b>
</div>
Tecnologias Utilizadas
--
<b>Tecnologias Utilizadas</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style='text-align: justify'>
VBCS, API, SOAP, EssJobs, FBDI, ALM, VBS, Javascript, UX/UI
</div>
---

## Ocyan
`Sr. Oracle Cloud Consultant | Application Specialist`
</br>
`Jan 2023 - Dez 2023`
<div style='text-align: justify'><b>
<li>Consultoria especializada em Oracle Cloud, atuando no desenvolvimento, integração e suporte de sistemas, com foco em VBCS, automação e metodologias ágeis.</li><br>
</b>
</div>
Tecnologias Utilizadas
--
<b>Tecnologias Utilizadas</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style='text-align: justify'>
VBCS, API, SOAP, EssJobs, FBDI, PL/SQL, BI Publisher, sFTP, GMUD
</div>
---

## Odontoprev
`Oracle Cloud Migration Developer`
</br>
`Jan 2022 - Jan 2023`
<div style='text-align: justify'><b>
<li>Desenvolvedor especializado em migração de sistemas para Oracle Cloud, com foco em VBCS e integrações, garantindo a melhor experiência para o usuário.</li><br>
</b>
</div>
Tecnologias Utilizadas
--
<b>Tecnologias Utilizadas</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style='text-align: justify'>
VBCS, API, SOAP, Javascript, Node.js
</div>
---

## MGSOARES Prog.
`Oracle Financial Consultant`
</br>
`Jan 2021 - Ago 2021`
<div style='text-align: justify'><b>
<li>Consultoria em soluções financeiras Oracle, atuando no suporte a processos de configuração, pagamento, relatórios e análise contábil.</li><br>
</b>
</div>
Tecnologias Utilizadas
--
<b>Tecnologias Utilizadas</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style='text-align: justify'>
Oracle Account Payables Cloud, Oracle Expenses Cloud
</div>
---

## Receita Federal
`Especialista em Suporte de TI`
</br>
`Jan 2020 - Fev 2021`
<div style='text-align: justify'><b>
<li>Suporte técnico em ambiente de TI, com foco em hardware, redes e atendimento ao usuário.</li><br>
</b>
</div>
Tecnologias Utilizadas
--
<b>Tecnologias Utilizadas</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style='text-align: justify'>
Suporte de Hardware, Redes de Computadores, Redes LAN-WAN
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
