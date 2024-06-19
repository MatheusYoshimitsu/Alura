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

Também podemos enviar nossas dependências para um arquivo de _requirements_ com:

```bash
pip freeze > requirements.txt
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

Criando super usuário:

```bash
python3 manage.py createsuperuser
```

Subindo servidor:

```bash
python3 manage.py runserver
```

Em _views.py_:

```python
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class MatriculaViewSet(viewsets.ModelViewSet):
    # (...)
    
    @method_decorator(cache_page(20)) # 20 segundos de cache
    def dispatch(self, *args, **kwargs):
        return super(MatriculaViewSet, self).dispatch(*args, **kwargs)
```

Ao fazer o teste, percebemos que ao criar uma nova matrícula, irá demorar 20 segundos para esta nova matrícula aparecer em ListaMatrículas. Ou seja, durante 20 segundos, a API está acessando o cache e não o servidor em si.

## Alura+: Args e Kwargs

[Alura+: *args e **kwargs](https://cursos.alura.com.br/extra/alura-mais/args-e-kwargs-multiplos-argumentos-em-python-c253)

## Aula 03 - Instalando o Redis

Exemplo para o Ubuntu:

```bash
sudo apt install lsb-release curl gpg
```

```bash
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
```

```bash
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
```

```bash
sudo apt update
```

```bash
sudo apt install redis
```

### Verificar o Status do Serviço

```bash
sudo systemctl status redis-server  
```

### Iniciar o Redis

```bash
sudo systemctl start redis-server  
```

### Parar o Redis

```bash
sudo systemctl stop redis-server  
```

### Reiniciar o Redis

```bash
sudo systemctl restart redis-server  
```

### Testar a Conexão ao Redis

```bash
redis-cli  
```

Uma vez no prompt do Redis (127.0.0.1:6379>), você pode executar comandos para verificar a funcionalidade. Por exemplo, para definir e obter um valor:

```bash
127.0.0.1:6379> SET minha_chave "Hello, Redis!"  
OK  
127.0.0.1:6379> GET minha_chave  
"Hello, Redis!"  
```

### Configuração do Redis

```bash
sudo nano /etc/redis/redis.conf  
```

[Documentação do Redis](https://redis.io/docs/latest/)

## Aula 04 - Integrando Django e Redis

Em _settings.py_:

```python
# (...)

CACHES = {
    "default":{
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1", #/1 indica que esta sera a porta principal
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache" # nao queremos que o redis interfira no painel admin do Django

SESSION_CACHE_ALIAS = "default"
```

Se pararmos o redis, **perderemos a conexão** e receberemos um erro.

* O Redis é opcional. Podemos também apenas comentar as linhas acima e usar o cache do nosso próprio servidor.

## Aula 05 - Internacionalização da API

Em _settings.py_:

```python
MIDDLEWARE = [
    # (...)
    'django.middleware.locale.LocaleMiddleware',
]
```

Podemos testar essas alterações no **Postman**.

POST <http://localhost:8000/alunos/>

Em _headers_, ligar _Accept-Language_.

```text
# Exemplo em espanhol
es-es
```

## Aula 06 - Personalizando mensagens padrões

* Criar nova pasta _locale_

Em _settings.py_:

```python
# (...)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)
```

No terminal:

```bash
python3 manage.py makemessages -l pt_BR
```

Em _locale/pt_BR/LC_MESSAGES/django.po_

```python
#: venv/lib/python3.10/site-packages/django/forms/fields.py:95
msgid "This field is required."
msgstr "Deu ruim. Campo obrigatório."
```

No terminal:

```bash
python3 manage.py compilemessages -l pt_BR
```

Podemos testar essas alterações no Postman.

POST <http://localhost:8000/alunos/>

Em _headers_, desligar _Accept-Language_.

* Deve-se enviar um POST vazio

## Aula 07 - Content Negotiation

Para podermos mostrar nosso conteúdo em formato JSON e XML, podemos fazer a seguinte alteração:

Em _settings.py_

```python
REST_FRAMEWORK = {
    # (...)
        'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework_xml.parsers.XMLParser',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
    ],
}
```

Nota: ao fazer isso, perdemos a parte visual do Django no navegador.

## Aula 07 - Cenário de teste
