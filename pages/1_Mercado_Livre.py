import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Classificação de Produtos - Meli", layout="wide")

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

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .high-risk {
        color: #d62728;
        font-weight: bold;
    }
    .medium-risk {
        color: #ff7f0e;
        font-weight: bold;
    }
    .low-risk {
        color: #2ca02c;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Carrega e processa os dados do CSV"""
    try:
        # Carrega o CSV com separador ';'
        df = pd.read_csv('dataset_meli.csv', sep=';', encoding='utf-8')
        df = df[['title', 'condition', 'price', 'suggested_price',
         'score_suspeita', 'sold', 'review_rating', 'seller_name', 'url',
         'classificacao', 'created_at', 'motivos']]
        df = df.rename(columns={
        'title': 'Produto',
        'condition': 'Condição',
        'price': 'Preço',
        'suggested_price': 'Preço Sugerido',
        'score_suspeita': 'Score de Suspeita',
        'sold': 'Vendidos',
        'review_rating': 'Avaliação',
        'seller_name': 'Seller',
        'classificacao': 'Classificação',
        'created_at': 'Data',
        'motivos': 'Motivos'
    })
        # Dicionário de mapeamento
        map_classificacao = {
            'BAIXA SUSPEITA': 'Baixa Suspeita',
            'MÉDIA SUSPEITA': 'Média Suspeita',
            'ALTA SUSPEITA': 'Alta Suspeita',
            'PIRATA': 'Pirata',
            'PROVAVELMENTE ORIGINAL': 'Original'
        }

        # Aplicar a substituição no DataFrame
        df['Classificação'] = df['Classificação'].replace(map_classificacao)    


        # Limpa e converte colunas numéricas
        df['Preço'] = pd.to_numeric(df['Preço'], errors='coerce')
        df['Preço Sugerido'] = pd.to_numeric(df['Preço Sugerido'], errors='coerce')
        df['Score de Suspeita'] = pd.to_numeric(df['Score de Suspeita'], errors='coerce')
        
        # Converte desvio de preço para numérico
        df['Desvio preço'] = ((df['Preço'] - df['Preço Sugerido']) / df['Preço Sugerido']) + 1
        df['Desvio preço'] = df['Desvio preço'].round(2)

        # Calcula o faturamento
        df['~Faturamento (R$)'] = df['Preço'] * df['Vendidos']
        
        df['~Faturamento (R$)'] = df['~Faturamento (R$)'].round(2)
        df['Preço Sugerido'] = df['Preço Sugerido'].round(2)
        df['Preço'] = df['Preço'].round(2)
        

        # Converte datas
        df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
        
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame()

def create_overview_metrics(df):
    """Cria métricas de visão geral"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total de Produtos",
            value=f"{len(df):,}",
            delta=None
        )
    
    with col2:
        high_risk = len(df[df['Classificação'] == 'Pirata'])
        st.metric(
            label="Produtos Piratas",
            value=f"{high_risk:,}",
        )
    
    with col3:
        avg_score = df['Score de Suspeita'].mean()
        st.metric(
            label="Score Médio de Suspeita",
            value=f"{avg_score:.1f}",
            delta=None
        )
    
    with col4:
        avg_deviation = df['Desvio preço'].mean()
        st.metric(
            label="Desvio Médio de Preço",
            value=f"{avg_deviation:.1f}",
            delta=None
        )

def create_classification_chart(df):
    """Cria gráfico de classificação de risco"""
    classification_counts = df['Classificação'].value_counts()
    
    fig = px.pie(
        values=classification_counts.values,
        names=classification_counts.index,
        title="Distribuição por Classificação de Risco",
        color_discrete_map={
            'BAIXA SUSPEITA': '#2ca02c',
            'MÉDIA SUSPEITA': '#ff7f0e', 
            'ALTA SUSPEITA': '#d62728',
            'PIRATA': '#8b0000'
        }
    )
    
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(height=550)
    
    return fig

def create_classification_chart2(df):
    """Cria gráfico de condition"""
    classification_counts = df['Condição'].value_counts()
    
    fig = px.pie(
        values=classification_counts.values,
        names=classification_counts.index,
        title="Distribuição por Classificação de Risco",
        color_discrete_map={
            'Recondicionado': '#2ca02c',
            'Novo': '#ff7f0e', 
        }
    )
    
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(height=550)
    
    return fig

def create_price_analysis(df):
    """Cria análise de preços"""
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Preço vs Score de Suspeita', 'Distribuição de Desvios de Preço', 
                       'Preço vs Preço Sugerido', 'Score de Suspeita por Vendedor'),
        specs=[[{"type": "scatter"}, {"type": "histogram"}],
               [{"type": "scatter"}, {"type": "bar"}]]
    )
    
    # Scatter: Preço vs Score
    fig.add_trace(
        go.Scatter(
            x=df['Preço'],
            y=df['Score de Suspeita'],
            mode='markers',
            marker=dict(
                color=df['Score de Suspeita'],
                colorscale='RdYlGn_r',
                size=8,
                opacity=0.7
            ),
            text=df['Produto'],
            hovertemplate='<b>%{text}</b><br>Preço: R$ %{x}<br>Score: %{y}<extra></extra>',
            name='Produtos'
        ),
        row=1, col=1
    )
    
    # Histograma: Desvios de preço
    fig.add_trace(
        go.Histogram(
            x=df['Desvio preço'],
            nbinsx=30,
            name='Desvios de Preço',
            marker_color='lightblue'
        ),
        row=1, col=2
    )
    
    # Scatter: Preço vs Preço Sugerido
    fig.add_trace(
        go.Scatter(
            x=df['Preço Sugerido'],
            y=df['Preço'],
            mode='markers',
            marker=dict(
                color=df['Score de Suspeita'],
                colorscale='RdYlGn_r',
                size=8,
                opacity=0.7
            ),
            name='Preço vs Sugerido'
        ),
        row=2, col=1
    )
    
    # Bar: Score por vendedor (top 10)
    top_sellers = df.groupby('Seller')['Score de Suspeita'].mean().sort_values(ascending=False).head(10)
    fig.add_trace(
        go.Bar(
            x=top_sellers.index,
            y=top_sellers.values,
            name='Score por Vendedor',
            marker_color='orange'
        ),
        row=2, col=2
    )
    
    fig.update_layout(height=800, showlegend=False)
    return fig

def create_seller_analysis(df):
    """Cria análise de vendedores"""
    
    # Agrupa por seller
    seller_stats = df.groupby('Seller').agg({
        'Classificação': lambda x: (x == 'Pirata').sum(),
        'Score de Suspeita': ['count', 'mean'],        # Média e quantidade de produtos
        'Vendidos': 'sum',                               # Total de vendas
        '~Faturamento (R$)': 'sum',                        # Faturamento total
        'url': 'first'                               # URL do primeiro produto do seller
    }).round(2)
    
    # Renomeia colunas
    seller_stats.columns = [
        'Produtos_Piratas', 'Total_Produtos', 'Score_Médio',
        'Total_Vendas', 'Faturamento_Total', 'URL_Produto'
    ]
    
    # Taxa de pirataria
    seller_stats['Taxa_Pirataria'] = (
        seller_stats['Produtos_Piratas'] / seller_stats['Total_Produtos']
    )
    
    # Ordena pelo score médio
    seller_stats = seller_stats.sort_values('Score_Médio', ascending=False)
    
    return seller_stats

# def create_insights(df):
#     """Gera insights automáticos"""
#     insights = []
    
#     # Insight 1: Taxa geral de pirataria
#     total_piratas = len(df[df['classificacao'] == 'PIRATA'])
#     taxa_pirataria = (total_piratas / len(df)) * 100
#     insights.append(f"🔍 **Taxa de Pirataria Geral**: {taxa_pirataria:.1f}% dos produtos analisados são classificados como piratas")
    
#     # Insight 2: Vendedor com maior risco
#     seller_risk = df.groupby('seller_name')['score_suspeita'].mean().sort_values(ascending=False)
#     top_risk_seller = seller_risk.index[0]
#     top_risk_score = seller_risk.iloc[0]
#     insights.append(f"⚠️ **Vendedor de Maior Risco**: {top_risk_seller} com score médio de {top_risk_score:.1f}")
    
#     # Insight 3: Desvio de preço médio
#     avg_price_deviation = df['desvio_preco_num'].mean()
#     insights.append(f"💰 **Desvio Médio de Preço**: {avg_price_deviation:.1f}% em relação ao preço sugerido")
    
#     # Insight 4: Produtos mais suspeitos
#     high_suspicion = df[df['score_suspeita'] >= 80]
#     insights.append(f"🚨 **Produtos de Alta Suspeita**: {len(high_suspicion)} produtos com score ≥ 80")
    
#     # Insight 5: Análise temporal
#     if 'created_at' in df.columns and not df['created_at'].isna().all():
#         df['month'] = df['created_at'].dt.to_period('M')
#         monthly_piracy = df.groupby('month')['classificacao'].apply(lambda x: (x == 'PIRATA').sum())
#         if len(monthly_piracy) > 1:
#             trend = "crescimento" if monthly_piracy.iloc[-1] > monthly_piracy.iloc[0] else "redução"
#             insights.append(f"📈 **Tendência Temporal**: {trend} na detecção de produtos piratas")
    
#     return insights

def main():
    
    # Carrega os dados
    df = load_data()
    
    if df.empty:
        st.error("Não foi possível carregar os dados. Verifique se o arquivo 'resultado_analise.csv' existe.")
        return
    
    # Sidebar com filtros
    st.sidebar.header("🔧 Filtros")
    
    # Filtro por classificação
    classificacoes = ['Todas'] + list(df['Classificação'].unique())
    selected_classification = st.sidebar.selectbox("Classificação", classificacoes)
    
    # Filtro por score de suspeita
    min_score, max_score = st.sidebar.slider(
        "Score de Suspeita",
        min_value=int(df['Score de Suspeita'].min()),
        max_value=int(df['Score de Suspeita'].max()),
        value=(int(df['Score de Suspeita'].min()), int(df['Score de Suspeita'].max()))
    )
    
    # Filtro por vendedor
    vendedores = ['Todos'] + sorted(df['Seller'].unique().tolist())
    selected_seller = st.sidebar.selectbox("Vendedor", vendedores)
    
    # Aplicar filtros
    filtered_df = df.copy()
    
    if selected_classification != 'Todas':
        filtered_df = filtered_df[filtered_df['Classificação'] == selected_classification]
    
    filtered_df = filtered_df[
        (filtered_df['Score de Suspeita'] >= min_score) & 
        (filtered_df['Score de Suspeita'] <= max_score)
    ]
    
    if selected_seller != 'Todos':
        filtered_df = filtered_df[filtered_df['Seller'] == selected_seller]
    
    # --- 🔖 CRIAÇÃO DAS ABAS ---
    aba1, aba2 = st.tabs(["Relatórios Gráficos", "Consolidado"])
    
    # =========================
    # 📈 ABA 1 – RELATÓRIOS GRÁFICOS
    # =========================
    # CSS para aumentar o tamanho do texto das abas
    with aba1:
        st.header("Visão Geral")
        create_overview_metrics(filtered_df)
        st.markdown("---")

        # Análise de vendedores
        st.header("Análise de Vendedores")
        col1 = st.columns(1)[0]
        with col1:
            st.subheader("Top 10 Vendedores por Score de Risco")
            seller_analysis = create_seller_analysis(filtered_df)
            st.dataframe(seller_analysis.head(10), use_container_width=True, column_config={"URL_Produto": st.column_config.LinkColumn("URL Exemplo", display_text="🔗 Abrir", width=100)})

        # Insights automáticos
        # st.header("💡 Insights Automáticos")
        # insights = create_insights(filtered_df)
        # for insight in insights:
        #     st.info(insight)
    
    # =========================
    # 📋 ABA 2 – CONSOLIDADO
    # =========================
    with aba2:
        st.header("Dados Consolidados")
        st.markdown("Visualize e exporte a base de dados filtrada abaixo.")
        
        columns_to_show = st.multiselect(
            "Selecione as colunas para exibir:",
            options=filtered_df.columns,
            default=['Produto', 'Seller', 'Preço', 'Preço Sugerido', 'Desvio preço', 'Avaliação','Classificação', 'Vendidos','~Faturamento (R$)', 'Score de Suspeita', 'url']
        )
        
        if columns_to_show:
                st.dataframe(
                    filtered_df[columns_to_show].sort_values('Score de Suspeita', ascending=False),                    
                    use_container_width=True,
                    height=450,
                    column_config={"url": st.column_config.LinkColumn("URL", display_text="🔗 Abrir", width=100),
                    "Produto": st.column_config.TextColumn("Produto", max_chars=30, width=300)}
                )
        
        csv = filtered_df.to_csv(index=False, sep=';')
        st.download_button(
            label="📥 Download dos Dados Filtrados (CSV)",
            data=csv,
            file_name=f"dados_filtrados_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main()
