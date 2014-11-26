# coding: utf-8
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TABLE1_NAME = 'tabela'
TABLE2_NAME = 'tabela2'
TABLES = {
    TABLE1_NAME: {
        'routes': os.path.join(BASE_DIR, TABLE1_NAME, 'rotas.csv'),
        'price_per_kg': os.path.join(BASE_DIR, 'tabela', 'preco_por_kg.csv'),
        'delimiter': ',',
        'icms': 6.0,
    },
    TABLE2_NAME: {
        'routes': os.path.join(BASE_DIR, TABLE2_NAME, 'rotas.tsv'),
        'price_per_kg': os.path.join(BASE_DIR, 'tabela2', 'preco_por_kg.tsv'),
        'delimiter': '\t',
    },
}
