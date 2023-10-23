# Cancer Data Analysis

Este é um projeto de análise de dados sobre câncer. Ele envolve a análise de um conjunto de dados contendo informações sobre diferentes tipos de câncer e suas taxas de mortalidade em vários países. O projeto inclui a limpeza, exploração e visualização dos dados para obter insights e responder a algumas perguntas-chave.

## Visão Geral do Projeto

Este projeto é dividido nas seguintes etapas principais:

1. **Coleta de Dados**: O conjunto de dados foi obtido de [fonte dos dados] e carregado em um DataFrame do Python usando a biblioteca pandas.

2. **Limpeza de Dados**: Foram realizadas etapas de limpeza de dados para lidar com valores ausentes, dados incorretos e formatação.

3. **Análise Exploratória de Dados (EDA)**: Foram geradas estatísticas descritivas e visualizações para entender melhor os dados e identificar tendências.

4. **Perguntas-Chave**:
   - Quais são os 10 países com a maior taxa de mortalidade por câncer?
   - Quais tipos de câncer têm as taxas de mortalidade mais altas em média?
   - Existe uma tendência de aumento ou diminuição nas taxas de câncer ao longo dos anos?
   - Existem diferenças significativas nas taxas de câncer entre diferentes regiões geográficas?

5. **Visualização de Dados**: Foram criados gráficos para comunicar os resultados da análise.

## Requisitos

Para executar este projeto, você precisará das seguintes bibliotecas Python:

- pandas
- streamlit
- plotly.express

Você pode instalá-los via pip:

```bash
pip install pandas 
pip install streamlit
pip intall plotly-express

rodar na web:

cd /ds_cancer/browser/
streamlit run app.py  

