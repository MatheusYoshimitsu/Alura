# Anotacoes

## Biblioteca para validar documentos brasileiros

```bash
pip install validate-docbr
```

## Script para popular clientes

Durante o curso, usamos um script para popular clientes, algo que seria muito demorado de ser feito na mão. No entanto, é importante estar atento às dependências deste script, como por exemplo, a biblioteca Faker. Ela pode ser instalada com:

```bash
pip install Faker
```

## Paginação

Podemos paginar o método GET. Para isso, podemos consultar a documentação Django Rest Pagination. Então, devemos inserir o seguinte código no arquivo *settings.py*

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

## Ordenação

Por padrão, a ordenação encontrada em Admin é feita pelos últimos registros criados. Podemos mudar isto com a seguinte linha:

```python
ordering = ('nome', )
```

Desta forma, a ordenação será feita pelos nomes em ordem alfabética.

### Ordenação na API

A ordenação feita anteriormente se deu na página de admin, no entanto, é interessante colocar também no funcionamento de nossa API em si. Para isso, podemos consultar a documentação Django Rest Filter.

```bash
pip install django-filter
```

Após a instalação, devemos adicionar o Django Filter em *settings.py*:

```python3
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'clientes',
    'django_filters',
]
```

Em seguida, devemos fazer as alterações necessárias na View também.

## Deploy com Amazon AWS

1. Precisamos ter certeza que todas as dependências estão instaladas
2. Precisamos subir o projeto no Github
