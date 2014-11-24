# coding: utf-8

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'tabela': {
        'rotas': os.path.join(BASE_DIR, 'tabela', 'rotas.csv'),
        'preco_por_kg': os.path.join(BASE_DIR, 'tabela', 'preco_por_kg.csv'),
    },
    'tabela2': {
        'rotas': os.path.join(BASE_DIR, 'tabela2', 'rotas.tsv'),
        'preco_por_kg': os.path.join(BASE_DIR, 'tabela2', 'preco_por_kg.tsv'),
    }
}
