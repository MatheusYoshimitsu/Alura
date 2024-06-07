# Anotações

## Passos para criar a API

1. Criar e acessar a pasta do projeto.
2. Criar e ativar o ambiente virtual.

```bash
python3 -m venv ./venv
source venv/bin/activate
```

3. Instalar Django, Django Rest Framework e Markdown.

```bash
pip install django
pip install djangorestframework
pip install markdown
```

4. Criar projeto setup, para manter a configuração da aplicação

```bash
django-admin startproject setup .
```

5. Criar a aplicação

```bash
python3 manage.py startapp escola
```

### Para rodar a aplicação

```bash
python3 manage.py runserver
```

6. Mudar em _settings.py_:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', # adicionando rest framework
    'escola', # adicionando a aplicacao
]
```

```python
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'
```

7. Codificar!

8. Após fazer os códigos, aplicar as migrações

```bash
python3 manage.py makemigrations
```

9. Subir as migrações

```bash
python3 manage.py migrate
```

10. Criar super usuário

```bash
python3 manage.py createsuperuser
```
