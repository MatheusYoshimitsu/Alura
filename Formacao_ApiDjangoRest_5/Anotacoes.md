# Anotações

## Pré-requisitos

### Criando e ativando o ambiente virtual

```bash
python3 -m venv ./venv
```

```bash
source venv/bin/activate
```

### Instalando dependencias

```bash
pip install -r requirements.txt
```

* Enviando dependências para o arquivo txt:

```bash
pip freeze > requirements.txt
```

### Migrando os modelos

```bash
python3 manage.py makemigrations
```

```bash
python3 manage.py migrate
```

### Criando super usuário

```bash
python3 manage.py createsuperuser
```

### Subindo o servidor

```bash
python3 manage.py runserver
```

## Carregando os dados

```bash
python3 manage.py loaddata programas_iniciais.json
```

## Tipos de testes

### Testes funcionais

* de Unidade x de Integração x Funcional

### Testes Não-Funcionais

* de Performance x de Carga x de Estresse

## Fixtures

Importando dados iniciais para nossa aplicação. Assim, não precisamos cadastrar uma por uma usando a interface. [Fixtures na Alura](https://cursos.alura.com.br/course/api-django-3-testes-documentacao/task/88509)

## Rodando teste

```python
python3 manage.py test
```

## Testes no Postman

```js
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Resposta no formato em JSON", function(){
    pm.response.to.be.json;
})

pm.test("Saltadores Utimato", function () {
    pm.expect(pm.response.text()).to.include("Saltadores Utimato");
});
```

## Documentação com o Swagger

### Instalando o Swagger

```bash
pip install -U drf-yasg
```

### Atualizando settings.py

```python
INSTALLED_APPS = [
    # (...)
    'rest_framework',
    'django_filters',
    'aluraflix',
    'drf_yasg',
]
```

### Em urls.py

```python
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Alura Flix",
      default_version='v1',
      description="Filmes e séries eba",
      terms_of_service="#",
      contact=openapi.Contact(email="c3po@email.com.br"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

```
