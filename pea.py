import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard PEA Brasil",
    layout="wide"
)

st.title("📊 Dashboard - População Economicamente Ativa no Brasil")
st.subheader("Projeções do mercado de trabalho brasileiro")

# ----------------------------
# 1. População por década
# ----------------------------
pop_data = pd.DataFrame({
    "Ano": [2020, 2030, 2040, 2050],
    "População (milhões)": [211.75, 215, 220, 215]
})

st.header("1️⃣ População Brasileira por Década")

fig_pop = px.line(
    pop_data,
    x="Ano",
    y="População (milhões)",
    markers=True,
    title="Evolução da população brasileira"
)

st.plotly_chart(fig_pop, use_container_width=True)

# ----------------------------
# 2. PEA por setor
# ----------------------------
st.header("2️⃣ Distribuição da PEA por setor econômico")

pea_data = pd.DataFrame({
    "Ano": [2020, 2030, 2040, 2050],
    "Primário": [20, 10, 8, 8],
    "Secundário": [24, 20, 17, 12],
    "Terciário": [56, 70, 75, 80]
})

pea_melt = pea_data.melt(
    id_vars="Ano",
    var_name="Setor",
    value_name="Percentual"
)

fig_pea = px.bar(
    pea_melt,
    x="Ano",
    y="Percentual",
    color="Setor",
    barmode="stack",
    title="Distribuição da População Economicamente Ativa"
)

st.plotly_chart(fig_pea, use_container_width=True)

# ----------------------------
# 3. Áreas promissoras
# ----------------------------
st.header("3️⃣ Áreas promissoras por setor")

areas_data = pd.DataFrame({
    "Área": [
        "Pecuária e Carne",
        "Soja e Milho",
        "Setor Florestal",
        "Exportações",
        "Indústria Extrativa",
        "Agroindústria",
        "Tecnologia da Informação",
        "Serviços Técnico-Profissionais"
    ],
    "Crescimento (%)": [
        12.48,
        11.7,
        29.1,
        30,
        7,
        16,
        84.4,
        59.8
    ]
})

fig_areas = px.bar(
    areas_data,
    x="Área",
    y="Crescimento (%)",
    color="Crescimento (%)",
    title="Áreas mais promissoras"
)

st.plotly_chart(fig_areas, use_container_width=True)

# ----------------------------
# 4. Impacto da IA
# ----------------------------
st.header("4️⃣ Impacto da Inteligência Artificial")

st.info("""
A IA tende a reduzir trabalhos manuais e repetitivos,
mas cria oportunidades em tecnologia, engenharia,
arquitetura e inovação.
""")

# ----------------------------
# 5. Conclusão
# ----------------------------
st.header("5️⃣ Conclusão")

st.success("""
O futuro do mercado de trabalho brasileiro será cada vez
mais voltado para tecnologia, sustentabilidade e inovação.
""")