[![wakatime](https://wakatime.com/badge/user/3bd24664-869f-460a-94e1-b98da8136504/project/6a658fa1-dcb1-45ea-b898-34455e00bb4a.svg)](https://wakatime.com/badge/user/3bd24664-869f-460a-94e1-b98da8136504/project/6a658fa1-dcb1-45ea-b898-34455e00bb4a)

<h2 align="center"> API Flask Targetdata 🚀 </h2> 

#### Autor: **[Matheus Feu](https://www.linkedin.com/in/matheus-feu-558558186/)**

## <h3 align="center"> Índice </h3>

<p align="center">
   <a href="#-sobre>"> Sobre 📝</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
   <a href="#-tecnologias-usadas>"> Tecnologias Usadas 🔗</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
   <a href="#-instalação>"> Instalação ⚙️</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
   <a href="#-execução>"> Execução 🎯</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
   <a href="#-endpoints>"> Endpoints 📌</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
   <a href="#-documentação>"> Documentação 📚</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
   <a href="#-contato>"> Contato 📞</a> 
</p>


<a id="-sobre"></a>

## Sobre 📝

Este projeto foi desenvolvido para o processo seletivo da [Targetdata](https://www.linkedin.com/company/targetdata/).
Neste projeto foi desenvolvido uma API em Python com Flask que retorna JSON integrando com duas APIs públicas e
gratuitas e salva os logs no ElasticSearch.

A API foi desenvolvida utilizando o ***microframework*** Flask escrita em Python, banco de dados MongoB e ElasticSearch
dentro de containers Docker.

Tem o objetivo de consultar o CEP na API da ViaCEP e retornar a previsão do tempo dos 4 dias da cidade retornada na API
do INPE.

<a id="-tecnologias-usadas"></a>

## Tecnologias Usadas 🔗

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![MongoDB](https://img.shields.io/badge/mongodb-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![ElasticSearch](https://img.shields.io/badge/elasticsearch-%234ea94b.svg?style=for-the-badge&logo=elasticsearch&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-%23Clojure.svg?style=for-the-badge&logo=swagger&logoColor=white)

<a id="-instalação"></a>

## Instalação ⚙️

### 💻 Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:

- Você precisa instalar o [Docker](https://docs.docker.com/engine/install/) para criar os containers do MongoDB e do ElasticSearch.

- Você instalar o versão mais recente do [Python](https://www.python.org/downloads/), estou utilizando a 3.11.

- Ter instalado o [Git](https://git-scm.com/downloads) para clonar o projeto.

- Possuir um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)
  ou [PyCharm](https://www.jetbrains.com/pt-br/pycharm/).


Com tudo em mãos, vamos ao passo a passo de como rodar o projeto, é bem simples a instalação de todas as dependências
para que o projeto funcione corretamente.

<a id="-execução"></a>

## Execução 🎯

#### Utilize os comandos abaixo para clonar o projeto e instalar as dependências seu terminal:

```bash
git clone https://github.com/matheus-feu/API-Flask-Targetdata.git
cd API-Flask-Targetdata
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
```

#### Agora vamos criar os containers:

Nesta etapa você deverá executar o comando abaixo para criar os containers do MongoDB e do ElasticSearch, ele irá criar
os containers e baixar as imagens necessárias que estão configurada no `Dockerfile` eo  `docker-compose.yml`.

```bash
docker-compose up -d
```

Por fim vamos executar o projeto:

```bash
python run.py
```

A aplicação deverá estar rodando na porta 5000, acesse o endereço http://localhost:5000/ para ver se está tudo
funcionando corretamente.

![documentacao](https://imgur.com/S2MJ9ne.png)

<a id="-endpoints"></a>

## Endpoints 📌

- **POST** /login - Ao realizar o login será retornado um token de acesso que deverá ser utilizado nos demais endpoints.
- **POST** /signup - Cria um usuário e senha para realizar o login.
- **GET** /logs_api/_search - Retorna os logs da API salvo no ElasticSearch.
- **POST** /weather-address - Recebe um CEP e retorna a previsão do tempo dos 4 dias da cidade retornada na API do INPE.

<a id="-documentação"></a>

## Documentação 📚

A documentação da API foi feita utilizando o Swagger, para acessar a documentação acesse o
endereço http://localhost:5000/apidocs/ e você terá acesso a documentação completa da API.

### Flasgger

O Flasgger é uma biblioteca Python que permite que você crie documentação Swagger para sua API Flask. Ele usa o
Flask-RESTful para criar uma documentação Swagger para sua API Flask.

- Maneira mais fácil de documentar sua API Flask é usando o Flasgger, e fácil de instalar:

```bash
pip install flasgger
```

- Exemplo de como importar o Flasgger:

```bash
from flasgger import Swagger

app = Flask(__name__)
Swagger(app, template_file='swagger.yml')
```

- Exemplo de como documentar um endpoint:

```bash
from flasgger.utils import swag_from

@app.route('/weather-address', methods=['POST'])
@swag_from('swagger/weather-address.yml')
def weather_address():
    cep = request.json['cep']
    return jsonify(get_weather_address(cep))
```

### JWT

O JWT é um padrão aberto (RFC 7519) que define uma forma compacta e autocontida de transmitir informações entre
partes como um JSON Object. Essas informações podem ser verificadas e confiáveis porque são assinadas digitalmente.

- Para instalar o JWT:

```bash
pip install flask-jwt-extended
```

- Exemplo de como importar o JWT:

```bash
from flask_jwt_extended import JWTManager
```

- Exemplo de como configurar o JWT:

```bash
jwt = JWTManager(app)
```

- Exemplo de como criar um token de acesso:

```bash
import jwt

secret = app.config['SECRET_KEY']

security_token = jwt.encode({
    'id': str(db_login.id),
    'exp': exp,
    'username': db_login.username,
}, secret)
  es_logger.info(f"Usuario: {request_login.username} logado com sucesso")
  es_logger.info('Token gerado com sucesso')
  return {'token': security_token}
```

<id id="-contato"></id>

### Contato 📞

- [Email](mailto:matheusfeu@gmail.com)
- [Linkedin](https://www.linkedin.com/in/matheus-feu-558558186/)
- [Github](https://github.com/matheus-feu)
- [Instagram](https://www.instagram.com/math_feu/)
