# 🧠 FIAP - Challenge HP 2025

### Classificação Inteligente de Produtos Piratas em Marketplaces

------------------------------------------------------------------------

## 📘 Descrição do Projeto

Este projeto foi desenvolvido como parte do **Challenge FIAP - HP
2025**, com o objetivo de criar uma **Inteligência Artificial capaz de
identificar produtos piratas em marketplaces** como o Mercado Livre.

A solução utiliza técnicas de **Machine Learning**, **Análise de Dados**
e **Streamlit** para disponibilizar uma interface interativa que
permite:

-   Identificar **padrões de falsificação** em anúncios.\
-   Analisar **vendedores e produtos suspeitos**.\
-   Gerar **relatórios visuais** e **tabelas consolidadas**.\
-   **Auxiliar a equipe da HP** no monitoramento de produtos não
    originais.

------------------------------------------------------------------------

## 🚀 Principais Funcionalidades

-   **Dashboard Interativo (Streamlit)**\
    Interface moderna com métricas e tabelas dinâmicas.

-   **Classificação de Risco**\
    Cada produto é classificado em níveis de suspeita:

    -   🟢 Baixa Suspeita\
    -   🟠 Média Suspeita\
    -   🔴 Alta Suspeita\
    -   ⚫ Pirata\
    -   ⚪ Original

-   **Filtros Avançados**

    -   Por classificação de risco\
    -   Por vendedor\
    -   Por faixa de *score* de suspeita

-   **Visualizações Inteligentes**

    -   Distribuição por classificação\
    -   Relação entre preço, score e desvio de preço\
    -   Top 10 vendedores por score médio\
    -   Análises de faturamento estimado

-   **Exportação de Dados**

    -   Download de subconjuntos filtrados em formato `.csv`.

------------------------------------------------------------------------

## 🧩 Estrutura do Projeto

    📂 projeto-hp-challenge-2025
    ├── Pagina_Inicial.py        # Página inicial com a descrição e identidade visual
    ├── mercado_livre.py         # Dashboard principal de análise dos produtos
    ├── Plus_Amazon.py           # Dashboard secundário, o nosso foco foi o Meli, mas também fizemos a Amazon como um plus
    ├── Próximos_Passos.py       # Aba contendo os nossos próximos passos
    ├── dataset_meli.csv         # Base de dados analisada (entrada principal)
    ├── hp_logo3.svg             # Logotipo da HP exibido na interface
    ├── requirements.txt         # Dependências do projeto
    └── README.md                # Documentação

------------------------------------------------------------------------

## 🧱 Tecnologias Utilizadas

  -----------------------------------------------------------------------
  Categoria                          Tecnologias
  ---------------------------------- ------------------------------------
  **Frontend**                       Streamlit, HTML/CSS embutido

  **Data Science**                   Pandas, NumPy, Plotly, Graph Objects

  **Machine Learning                 Modelos de classificação e análise
  (pré-processamento e score)**      de risco (treinados externamente)

  **Outros**                         Python 3.10+, datetime, warnings
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## ⚙️ Instalação e Execução

### 1️⃣ Clonar o repositório

``` bash
git clone https://github.com/SEU_USUARIO/projeto-hp-challenge-2025.git
cd projeto-hp-challenge-2025
```

### 2️⃣ Criar um ambiente virtual (opcional, mas recomendado)

``` bash
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate    # (Windows)
```

### 3️⃣ Instalar as dependências

Instale utilizando
``` bash
pip install -r requirements.txt
```

### 4️⃣ Executar o projeto

**Página inicial (apresentação):**

``` bash
streamlit run Pagina_Inicial.py
```

------------------------------------------------------------------------

## 🧮 Lógica de Funcionamento

1.  O sistema lê a base `dataset_meli.csv` e **padroniza as colunas**.\
2.  Calcula métricas derivadas:
    -   Desvio de preço entre preço real e sugerido;\
    -   Faturamento estimado;\
    -   Média de score por vendedor.\
3.  Classifica os produtos segundo o **modelo de IA** previamente
    treinado.\
4.  Exibe os resultados na interface Streamlit com gráficos e filtros
    dinâmicos.\
5.  Permite **download de subconjuntos filtrados** para auditoria ou
    relatórios.

------------------------------------------------------------------------

## 📈 Exemplo de Visualizações

-   **Distribuição de Classificação** (gráfico de pizza)\
-   **Relação Preço x Score de Suspeita** (scatter plot)\
-   **Desvio de Preço vs Score de Risco**\
-   **Top 10 Vendedores mais suspeitos**\
-   **Métricas gerais**: Total de produtos, média de score, desvio médio
    de preço

------------------------------------------------------------------------

## 👩‍💻 Equipe

**validAI** -- Grupo participante do **Challenge FIAP - HP 2025**

  Nome               
  ------------------ --------------------------------------------
* Danilo Ramalho Silva | RM: 555183
* Israel Dalcin Alves Diniz | RM: 554668
* João Vitor Pires da Silva | RM: 556213
* Matheus Hungaro | RM: 555677
* Pablo Menezes Barreto | RM: 556389
* Tiago Toshio Kumagai Gibo | 556984

------------------------------------------------------------------------

## 🏆 Resultados e Impacto

O projeto demonstra o **potencial da Inteligência Artificial aplicada à
proteção de marcas**, oferecendo uma ferramenta para **detecção
automática de produtos falsificados** e **suporte à decisão
estratégica** em grandes marketplaces.

------------------------------------------------------------------------

## 📄 Licença

Este projeto foi desenvolvido exclusivamente para fins acadêmicos no
**Challenge FIAP - HP 2025** em parceria com a **HP Brasil**.\
Não é destinado a uso comercial.
