import streamlit as st
import pandas as pd

# 🧭 Configurações da página
st.set_page_config(page_title="Próximos passos", layout="wide")

# 📘 Header com logo e título
logo_path = "hp_logo3.svg"
col1, col2, col3 = st.columns([0.6, 0.5, 0.25])
with col2:
    st.image(str(logo_path), width=120) 
st.markdown("""
    <div style="text-align:center;">
        <h1 style="color:white;">Próximos passos</h1>
    </div>
""", unsafe_allow_html=True)

import streamlit as st

def task_card(title, description, owner=None, priority="Média", done=False):
    cols = st.columns([8, 1, 1])
    with cols[0]:
        st.markdown(f"### {title}")
        st.write(description)
        if owner:
            st.caption(f"Responsável: **{owner}**  • Prioridade: **{priority}**")
    with cols[1]:
        st.checkbox("Concluído", value=done, key=f"chk_{title}")

st.markdown("---")

# Overview em uma linha
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Backlog", "4 itens")
with col2:
    st.metric("Prioridade Alta", "2")
with col3:
    st.metric("Em Progresso", "1")

st.markdown("## Roadmap & Ações recomendadas")
st.info("Observação: para captura de comentários e scraping, priorizar APIs oficiais e conformidade legal. Evitar burlar mecanismos anti-bot.")

# Task 1
task_card(
    "Capturar comentários e análise de sentimento",
    """
    - Coletar reviews para enriquecer features (sentimento, tópicos, entidades).
    - Preferir APIs oficiais; se for scraping, seguir robots.txt, rate limits e consultar jurídico.
    - Ferramentas: Playwright (quando permitido), APIs, modelos transformer para sentiment/NER.
    """,
    owner="ValidAI & HP",
    priority="Alta",
    done=False
)

st.markdown("---")

task_card(
    "Integração de coleta de dados com interface visual",
    """
    - Integrar a camada de coleta de dados (web scraping ou APIs) com a interface visual, garantindo que a HP tenha total controle e autonomia sobre o processo
    """,
    owner="ValidAI",
    priority="Alta",
    done=False
)

st.markdown("---")

# Task 2
task_card(
    "Expandir gama de produtos (além do 667)",
    """
    - Automatizar ETL e validação.
    - Ferramentas: Prefect/Airflow.
    """,
    owner="ValidAI",
    priority="Alta",
    done=False
)

st.markdown("---")

# Task 3
task_card(
    "Expandir marketplaces (Shopee, Temu, Magalu, etc.)",
    """
    - Priorizar marketplaces com APIs públicas.
    - Padronizar schema de ingestão (price, sold, seller_id, url, rating).
    """,
    owner="ValidAI",
    priority="Média",
    done=False
)

st.markdown("---")

# Task 4
task_card(
    "Criar 'carrinho' via site para facilitar compra de produtos suspeitos",
    """
    - Flow: identificar -> adicionar ao carrinho -> redirecionamento URLs -> compra Mktplace
    - Arquitetura sugerida: FastAPI backend + front em React/Streamlit.
    """,
    owner="ValidAI",
    priority="Média",
    done=False
)

st.markdown("---")

# Task 4
task_card(
    "Criar análises gráficas mais robustas",
    """
    - Desenvolver dashboards mensais detalhados com métricas como: faturamento dos maiores infratores, quantidade de produtos piratas, evolução temporal e comparativos entre categorias ou sellers.
    - Arquitetura sugerida: frontend em React ou Streamlit, integrando visualizações interativas com Plotly/Chart.js para exploração dinâmica dos dados.
    """,
    owner="ValidAI",
    priority="Média",
    done=False
)
