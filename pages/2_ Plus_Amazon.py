import streamlit as st
import pandas as pd

# 🧭 Configurações da página
st.set_page_config(page_title="Classificação de Produtos", layout="wide")

# 📘 Header com logo e título
logo_path = "hp_logo3.svg"
col1, col2, col3 = st.columns([0.6, 0.5, 0.25])
with col2:
    st.image(str(logo_path), width=120) 
st.markdown("""
    <div style="text-align:center;">
        <h1 style="color:white;">Painel de Classificação de Produtos</h1>
    </div>
""", unsafe_allow_html=True)

# CSS para botões do mesmo tamanho e centralizados
st.markdown("""
    <style>
    div.stButton > button {
        width: 145px;  /* largura fixa */
        height: 40px;  /* altura fixa */
        margin: 0 auto; /* centraliza */
        display: block;
        font-size: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# # Botões lado a lado centralizados
# col1, col2, col3 = st.columns([1.15, 1.5, 1])  # espaço à esquerda e direita

# with col2:
#     col_a, col_b = st.columns(2)
#     with col_a:
#         if st.button("🟡 Mercado Livre"):
#             st.session_state["marketplace"] = "mercado_livre"
#     with col_b:
#         if st.button("🟠 Amazon"):
#             st.session_state["marketplace"] = "amazon"


st.markdown("---")
df = pd.read_csv("dataset_hp - Amazon.csv")

# Define colunas relevantes
colunas = [
    "title", "Price (substituido)", "preco_sugerido",
    "diferenca_percentual", "rating", "seller",
    "ai_prediction", "risk_score", "risk_level", "url"
]

# 🔹 CSS personalizado para tabela
st.markdown("""
<style>
    .dataframe {
        width: 100%;
        margin: 0 auto;
        table-layout: fixed;
        border-collapse: collapse;
    }
    tr:nth-child(even) {background-color: #2e2e2e;}
    tr:nth-child(odd) {background-color: #1e1e1e;}
    th {
        background-color: #0e1117;
        color: white;
        font-size: 14px;
        text-align: left;
    }
    td {
        color: white;
        font-size: 12px;
        text-align: left;
    }
    button {
        background-color: #262730;
        color: white;
        border: none;
        padding: 6px 14px;
        border-radius: 5px;
        cursor: pointer;
    }
    button:hover {
        background-color: #444;
    }
</style>
""", unsafe_allow_html=True)

# 🔹 Filtrar e ordenar dados
alto_risco = df[df["risk_score"] >= 4][colunas].sort_values(by="risk_score", ascending=False).reset_index(drop=True)
baixo_risco = df[df["risk_score"] <= 3][colunas].sort_values(by="risk_score", ascending=False).reset_index(drop=True)
alto_risco.columns = ['Produto', 'Preço', 'Preço Catálogo', 'Diferença Relativa', 'Rating', 'Vendedor', 'Predição AI', 'Risco Score', 'Risco level', 'URL']
baixo_risco.columns = ['Produto', 'Preço', 'Preço Catálogo', 'Diferença Relativa', 'Rating', 'Vendedor', 'Predição AI', 'Risco Score', 'Risco level', 'URL']
# Seção 1 — Alto Risco
st.header("Produtos de Alto Risco")
st.dataframe(alto_risco, use_container_width=True, column_config={"URL": st.column_config.LinkColumn("URL", display_text="🔗 Abrir", width=100)})

st.markdown("---")

# Seção 2 — Médio/Baixo Risco
st.header("Produtos de Médio/Baixo Risco")
st.dataframe(baixo_risco, use_container_width=True, column_config={"URL": st.column_config.LinkColumn("URL", display_text="🔗 Abrir", width=100)})
