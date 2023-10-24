# Este módulo pode ser responsável por carregar e pré-processar os dados do seu arquivo CSV.
# data_loader.py

import pandas as pd

def load_data(file_path, colunas_cancer):
    # Realiza a leitura dos dados
    df = pd.read_csv(file_path)

    # Converta a coluna 'YEAR' em texto (string) e, em seguida, retire as vírgulas
    df['YEAR'] = df['YEAR'].astype(str).str.replace(',', '')

    # Remova os espaços nos nomes das colunas e, em seguida, converta as colunas de câncer para números inteiros
    df.columns = df.columns.str.strip()
    df[colunas_cancer] = df[colunas_cancer].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

    return df
