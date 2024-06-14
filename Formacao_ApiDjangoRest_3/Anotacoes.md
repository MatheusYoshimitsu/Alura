# Anotações

## Ambiente Virtual

### Criando e ativando um novo ambiente virtual

```bash
python3 -m venv ./venv
```

```bash
source venv/bin/activate
```

## Dependências

### Instalando dependências do projeto

Para instalar as versões utilizadas na aula:

```bash
pip install -r requirements.txt
```

Para instalar as versões mais recentes:

```bash
pip install asgiref Django djangorestframework Faker python-dateutil pytz six sqlparse text-unidecode validate-docbr
```

## Aplicar migrações

Primeiro:

```bash
python3 manage.py makemigrations
```

Em seguida:

```bash
python3 manage.py migrate
```

## Subir o servidor

```bash
python3 manage.py runserver
```

## Criar Super Usuário

```bash
python3 manage.py createsuperuser
```

## Popular os registros com o script

Neste caso, usaremos nosso script salvo _script.py_ para fazer a população de 200 alunos e 5 cursos

```bash
python3 seed.py
```

## Definindo permissões em **settings.py**

```python
REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.QueryParameterVersioning',
    'DEFAULT_PERMISSION_CLASSES':['rest_framework.permissions.IsAuthenticated',
                                  'rest_framework.permissions.DjangoModelPermissions'
                                  ]
}
```

Com isso, podemos limpar nosso código, retirando a seguinte linha das views:

```python
permission_classes = [IsAuthenticated, DjangoModelPermissions]
```

Podemos fazer a mesma coisa com as autenticações:

```python
REST_FRAMEWORK = {
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.QueryParameterVersioning",
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
        "rest_framework.permissions.DjangoModelPermissions",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES:":[
        'rest_framework.authentication.BasicAuthentication'
    ]
}
```

## Métodos HTTP

É possível restringir os métodos HTTP

```python
# Exemplo
http_method_names = ['get', 'post', 'put', 'patch']
```

## O que é o Node.js?

Node.js é um ambiente de execução que permite rodar códigos _server-side_, isso abre diversas utilidades para o JavaScript. Com isso, ele não depende do navegador para executar código JavaScript, permitindo inclusive fazer diversas ações paralelamente.

## CORS

De forma bruta, o CORS define quem pode ou não acessar a API

* Ex: usando a política de _same origin_ (mesma origem).

### Django CORS

Podemos seguir a documentação para saber como instalar corretamente o CORS na nossa API Django Rest. Para o middleware, é importante ressaltar que ele deve ser colocado o mais alto possível, pois a ordem importa para o funcionamento esperado do CORS.
