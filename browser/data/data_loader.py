# Este módulo pode ser responsável por carregar e pré-processar os dados do seu arquivo CSV.

import pandas as pd

def load_data(file_path):
    # Realiza a leitura dos dados
    df = pd.read_csv(file_path)

     # Certifique-se de que a coluna "YEAR" esteja no formato de data (YYYY-MM-DD) e, em seguida, converta para o ano.
    df['YEAR'] = pd.to_datetime(df['YEAR'], format='%Y').dt.year
    
    return df
