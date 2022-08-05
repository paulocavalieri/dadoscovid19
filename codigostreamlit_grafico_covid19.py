# -*- coding: utf-8 -*-
"""codigostreamlit_grafico_covid19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T4vEDfTaoYs1cRDGjYe-4QdUZuy6gMt2
"""

import pandas as pd
import plotly.express as px
import streamlit as st

# LENDO O DATASET
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# MELHORANDO O NOME DAS COLUNAS DA TABELA
df = df.rename(columns={'newDeaths': 'novos óbitos', 'newCases': 'novos casos', 'deaths': 'Total de óbitos', 'totalCases': 'Total de casos'})

# MELHORANDO O NOME DE 'TOTAL' PARA 'BRASIL'
df['state'] = df['state'].replace(['TOTAL'], 'Brasil')

# SELEÇÃO DO ESTADO
estados = list(df['state'].unique())
state = st.sidebar.selectbox('Selecione o Estado ou Brasil', estados)

# SELEÇÃO DA COLUNA
colunas = ['Novos Óbitos', 'Novos Casos', 'Total de óbitos', 'Total de casos']
column = st.sidebar.selectbox('Selecione tipo de informação', colunas)

# SELEÇÃO DAS LINHAS QUE PERTENCEM AO ESTADO
df = df[df['state'] == state]

# CONFIGURANDO OS EIXOS DO GRÁFICO (quais serão as informações de cada eixo)
fig = px.line(df, x='date', y=column, title=column + ' - ' + state)

# CONFIGURANDO O LAYOUT DO GRÁFICO (nome dos eixos e centralização)
fig.update_layout(xaxis_title='Data', yaxis_title=column.upper(), title={'x':0.5})

# ESCREVENDO INFORMAÇÕES DA APLICAÇÃO
st.title('DADOS COVID-19 BRASIL')
st.write('Essa aplicação permite que o usuário acesse, por meio de gráficos, números relativos à pandemia de COVID-19 no Brasil a partir de março de 2020')

# IMPRIMINDO O GRÁFICO USANDO A BIBLIOTECA PLOTLY
st.plotly_chart(fig, use_container_width=True)

st.caption('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')
