# Anotacoes

## Pré-requisitos

### Criando um novo ambiente virtual

```python
python3 -m venv ./venv
```

### Ativando o ambiente virtual

```python
source venv/bin/activate
```

### Instalando as bibliotecas necessárias

```python
pip install asgiref Django djangorestframework Faker python-dateutil pytz six sqlparse text-unidecode validate-docbr django-cors-headers pillow
# Para instalar a partir de um arquivo requirements
pip install -r requirements.txt
```

### Rodar as migrações

```python
python3 manage.py makemigrations
python3 manage.py migrate
```

### Carregando dados iniciais

```python
python3 seed.py
```

### Subindo o servidor

```python
python3 manage.py runserver
```

## Aula 01 - Upload de arquivos estáticos

Em _settings.py_ colocamos:

```python
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')
MEDIA_URL = '/media/'
```

Em _models.py_

Para adicionar um campo capaz de realizar upload de fotos, colocamos na classe Aluno:

```python
class Aluno(models.Model):
    # (...)
    foto = models.ImageField(blank=True)
    # (...)
```

Depois disso, precisamos atualizar o _serializer.py_:

```python
fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento', 'foto']
```

Por fim, precisamos atualizar o arquivo _urls.py_:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # (...)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Aula 02 - Caching