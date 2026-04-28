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
    title="Distribuição da População Economicamente Ativa",
    color_discrete_map={"Primário": "#87CEEB", "Secundário": "#1E3A8A", "Terciário": "#FF1493"}
)

st.plotly_chart(fig_pea, use_container_width=True)

# Definir paleta de cores para os setores
cores_setores = {
    "Primário": "#87CEEB",      # Azul claro
    "Secundário": "#1E3A8A",    # Azul escuro
    "Terciário": "#FF1493"      # Rosa intenso
}

# Gráficos de pizza por ano
pie_2020_data = pd.DataFrame({
    "setor": ["Primário", "Secundário", "Terciário"],
    "valor": [20, 24, 56]
})

pie_2050_data = pd.DataFrame({
    "setor": ["Primário", "Secundário", "Terciário"],
    "valor": [8, 12, 80]
})

# Cores na ordem correta
cores_sequencia = ["#87CEEB", "#1E3A8A", "#FF1493"]

col1, col2 = st.columns(2)

with col1:
    fig_pie_2020 = px.pie(
        pie_2020_data,
        values="valor",
        names="setor",
        title="Distribuição de PEA - 2020",
        category_orders={"setor": ["Primário", "Secundário", "Terciário"]}
    )
    fig_pie_2020.update_traces(marker=dict(colors=cores_sequencia, line=dict(color='#1a1a1a', width=1)))
    st.plotly_chart(fig_pie_2020, use_container_width=True)

with col2:
    fig_pie_2050 = px.pie(
        pie_2050_data,
        values="valor",
        names="setor",
        title="Distribuição de PEA - 2050",
        category_orders={"setor": ["Primário", "Secundário", "Terciário"]}
    )
    fig_pie_2050.update_traces(marker=dict(colors=cores_sequencia, line=dict(color='#1a1a1a', width=1)))
    st.plotly_chart(fig_pie_2050, use_container_width=True)

# ----------------------------
# 3. Áreas promissoras
# ----------------------------
st.header("3️⃣ Áreas promissoras por setor")

areas_data = pd.DataFrame({
    "area": [
        "Pecuária e Carne",
        "Soja e Milho",
        "Setor Florestal",
        "Exportações",
        "Indústria Extrativa",
        "Agroindústria",
        "Máquinas e Equipamentos",
        "Indústria da Tecnologia",
        "Construção Civil",
        "Tecnologia da Informação",
        "Serviços Técnico-Profissionais",
        "Transporte terrestre",
        "Serviços (Geral)",
        "Terceiro Setor"
    ],
    "crescimento": [
        12.48,
        11.7,
        29.1,
        30,
        7,
        16,
        5,
        6.5,
        1.3,
        84.4,
        59.8,
        43.5,
        2.8,
        16.8
    ],
    "setor": [
        "Primário",
        "Primário",
        "Primário",
        "Primário",
        "Secundário",
        "Secundário",
        "Secundário",
        "Secundário",
        "Secundário",
        "Terciário",
        "Terciário",
        "Terciário",
        "Terciário",
        "Terciário"
    ]
})

# Gráfico geral com cores por setor
fig_areas = px.bar(
    areas_data,
    x="area",
    y="crescimento",
    color="setor",
    title="Áreas mais promissoras por setor econômico",
    labels={"area": "Área", "crescimento": "Crescimento (%)"},
    color_discrete_map=cores_setores
)

fig_areas.update_xaxes(tickangle=-45)
st.plotly_chart(fig_areas, use_container_width=True)

# Gráfico separado por setor
st.subheader("Distribuição de áreas por setor:")

col1, col2, col3 = st.columns(3)

# Primário
areas_primario = areas_data[areas_data["setor"] == "Primário"]
with col1:
    fig_prim = px.bar(
        areas_primario,
        y="area",
        x="crescimento",
        title="Setor Primário",
        orientation="h"
    )
    fig_prim.update_traces(marker_color=cores_setores["Primário"])
    st.plotly_chart(fig_prim, use_container_width=True)

# Secundário
areas_secundario = areas_data[areas_data["setor"] == "Secundário"]
with col2:
    fig_sec = px.bar(
        areas_secundario,
        y="area",
        x="crescimento",
        title="Setor Secundário",
        orientation="h"
    )
    fig_sec.update_traces(marker_color=cores_setores["Secundário"])
    st.plotly_chart(fig_sec, use_container_width=True)

# Terciário
areas_terciario = areas_data[areas_data["setor"] == "Terciário"]
with col3:
    fig_terc = px.bar(
        areas_terciario,
        y="area",
        x="crescimento",
        title="Setor Terciário",
        orientation="h"
    )
    fig_terc.update_traces(marker_color=cores_setores["Terciário"])
    st.plotly_chart(fig_terc, use_container_width=True)

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