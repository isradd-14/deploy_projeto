import streamlit as st

# --- CONFIGURAÇÕES GERAIS ---
st.set_page_config(page_title="FIAP - Challenge HP 2025", page_icon="💡", layout="centered")
logo_path = "hp_logo3.svg"
col1, col2, col3 = st.columns([0.5, 0.6, 0.15])
with col2:
    st.image(str(logo_path), width=120) 
# --- LOGO E TÍTULO ---
st.markdown("""
    <div style="text-align:center;">
        <h1 style="color:white; margin-top: 10px;">FIAP - Challenge HP 2025</h1>
        <h3 style="color:lightgray; font-weight:normal;">
            Classificação Inteligente de Produtos Piratas em Marketplaces
        </h3>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- DESCRIÇÃO DO PROJETO ---
st.markdown(
"""<div style="text-align:justify; font-size:17px; line-height:1.6; color:#dcdcdc;">
<p>Este projeto foi desenvolvido como parte do <b>Challenge FIAP - HP 2025</b>, com o objetivo de criar um <b>classificador de produtos piratas</b> em marketplaces utilizando técnicas de <b>Inteligência Artificial</b>.</p>
<p>A solução proposta analisa informações de produtos, vendedores e descrições de anúncios para identificar padrões que indiquem possíveis falsificações ou produtos não originais.</p>
<p>Por meio de modelos de Machine Learning e IA generativa, o sistema é capaz de <b>atribuir níveis de risco</b> a cada item e auxiliar a equipe da HP na tomada de decisão e monitoramento de marketplaces.</p>
</div>""",
    unsafe_allow_html=True
)

st.markdown("---")

# --- EQUIPE OU RODAPÉ OPCIONAL ---
st.markdown("""
    <div style="text-align:center; font-size:15px; color:gray;">
        <p><i>Desenvolvido por validAI • Challenge HP 2025</i></p>
    </div>
""", unsafe_allow_html=True)
