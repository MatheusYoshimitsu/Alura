# Anotacoes

## Pré-requisitos

### Criando um novo ambiente virtual

```bash
python3 -m venv ./venv
```

### Ativando o ambiente virtual

```bash
source venv/bin/activate
```

### Instalando as bibliotecas necessárias

```bash
pip install asgiref Django djangorestframework Faker python-dateutil pytz six sqlparse text-unidecode validate-docbr django-cors-headers pillow
# Para instalar a partir de um arquivo requirements
pip install -r requirements.txt
```

Também podemos enviar nossas dependências para um arquivo de _requirements_ com:

```bash
pip freeze > requirements.txt
```

### Rodar as migrações

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Carregando dados iniciais

```bash
python3 seed.py
```

### Subindo o servidor

```bash
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

* Criar uma pasta _test_
* Dentro desta pasta, criar um arquivo _\_\_init\_\_.py_
* Criar arquivo _testes\_cursos.py_

Caso esteja usando o Redis, é importante se lembrar de iniciá-lo antes de fazer os testes.

No terminal:

```bash
sudo systemctl start redis-server
```

Em  _testes\_cursos.py_:

```python
from rest_framework.test import APITestCase
from rest_framework import status
from escola.models import Curso
from django.urls import reverse

class CursosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cursos-list') # Devemos passar o basename definido em urls.py
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT1', descricao='Curso teste 1', nivel='B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso='CTT2', descricao='Curso teste 2', nivel='A'
        )
    # def test_falhador(self):
    #     self.fail('Teste falhou propositalmente. Ta safe')

    def test_requisicao_get_para_listar_curso(self):
        """Teste para verificar a requisicao GET para listar cursos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_curso(self):
        """Teste para verificar a requisicao POST para criar cursos"""
        data = {
            'codigo_curso': 'CTT3',
            'descricao': 'Curso teste 3',
            'nivel': 'A'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
```

## Aula 08 - Testando PUT e DELETE

Supondo que não queremos mais permitir que seja possível deletar um curso:

Em _views.py_:

```python
class CursosViewSet(viewsets.ModelViewSet):
    # (...)
    serializer_class = CursoSerializer
    http_method_names = ['get', 'post', 'put', 'path']
    # (...)
```

Em  _testes\_cursos.py_:

```python
class CursosTestCase(APITestCase):
    # (...)
    def test_requisicao_delete_para_deletar_curso(self):
        """Teste para verificar a requisicao DELETE nao permitida para deletar cursos"""
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_put_para_atualizar_curso(self):
        """Teste para verificar requisicao PUT para atualizar um curso"""
        data = {
            'codigo_curso': 'CTT1',
            'descricao': 'Curso teste 1 atualizado',
            'nivel': 'I'
        }
        response = self.client.put('/cursos/1/', data=data)
        self.assertAlmostEquals(response.status_code, status.HTTP_200_OK)
```

Estes não são os métodos mais indicados para se fazer testes em uma API, já que esta é um tópico muito mais denso do que parece. Seria necessário todo um curso sobre testes, ao invés de apenas duas aulas curtas, no entanto, esta é uma forma simples de mostrar como funcionam testes no Django Rest.

## Aula 09 - Pensando em Segurança

Não queremos que nossa URL de admin seja facilmente acessada. Podemos então fazer algumas alterações.

Em _urls.py_:

```python
urlpatterns = [
    path('controle-geral/', admin.site.urls),
    # (...)  
] # (...)
```

No entanto, a API ainda devolve nosso código de _urls.py_. Portanto devemos desativar o DEBUG em _settings.py_.

Em _settings.py_:

```python
DEBUG = False

ALLOWED_HOSTS = ['localhost']
```

## Aula 10 - Honeypot

Registrando tentativas de acesso não autorizado.

Instalando a dependência:

* **A BIBLIOTECA NAO ESTA FUNCIONANDO COM O DJANGO 5**

```bash
pip install django-admin-honeypot
```

Em _settings.py_:

```python
INSTALLED_APPS = [
    # (...)
    'admin_honeypot',
]
```

Em _urls.py_:

```python
urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    # (...)
] # (...)
```

[Correção de um aluno da Alura](https://cursos.alura.com.br/forum/topico-sugestao-incluindo-honeypot-correcao-para-compatibilidade-com-django-4-2-2-307367)

Fazendo as migrações pendentes:

```bash
python3 manage.py migrate
```

Ao subir o servidor, podemos tentar fazer um login na URL fake _/admin_. Esta tentativa poderá ser vista na URL correta de admin _/controle-geral_.
