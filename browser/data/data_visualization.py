# Neste módulo, você pode definir funções para criar visualizações, como gráficos, usando os dados carregados.

import plotly.express as px

def create_visualization(data):
    # Crie visualizações dos dados usando Plotly Express ou outras bibliotecas de visualização
    # Exemplo:
    fig = px.scatter(data, x='Year', y='Total Deaths', title='Total Deaths Over Time')
    return fig
