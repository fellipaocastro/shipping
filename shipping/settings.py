# coding: utf-8

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TABLES = {
    'table': {
        'routes': os.path.join(BASE_DIR, 'tabela', 'rotas.csv'),
        'price_per_kg': os.path.join(BASE_DIR, 'tabela', 'preco_por_kg.csv'),
        'delimiter': ',',
        'icms': 6.0,
    },
    'table2': {
        'routes': os.path.join(BASE_DIR, 'tabela2', 'rotas.tsv'),
        'price_per_kg': os.path.join(BASE_DIR, 'tabela2', 'preco_por_kg.tsv'),
        'delimiter': '\t',
    },
}
