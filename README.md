[![wakatime](https://wakatime.com/badge/user/3bd24664-869f-460a-94e1-b98da8136504/project/6a658fa1-dcb1-45ea-b898-34455e00bb4a.svg)](https://wakatime.com/badge/user/3bd24664-869f-460a-94e1-b98da8136504/project/6a658fa1-dcb1-45ea-b898-34455e00bb4a)

<h2 align="center"> API Flask Targetdata 🚀 </h2> 

#### Autor: **[Matheus Feu](https://www.linkedin.com/in/matheus-feu-558558186/)**

## Índice 📋

- [Sobre](#-sobre)
- [Tecnologias Usadas](#-tecnologias-usadas)
- [Instalação](#-instalação)
- [Execução](#-execução)
- [Endpoints](#-endpoints)
- [Bibliotecas](#-bibliotecas)
- [Contato](#-contato)

## 📝 Sobre

Este projeto foi desenvolvido para o processo seletivo da [Targetdata](https://www.linkedin.com/company/targetdata/).
Neste projeto foi desenvolvido utilizando o ***microframework*** Flask escrita em **Python** que retorna JSON integrando
com
duas **APIs** públicas e
gratuitas e salva os logs no ElasticSearch, o projeto foi desenvolvido utilizando o **Docker** para criar os containers
do
**MongoDB** e do **ElasticSearch** e a aplicação **Flask**.

A API oferece diversas funcionalidades que podem ser úteis para diferentes tipos de sistemas. Entre elas, estão as
opções de login e registro, que permitem que os usuários acessem o sistema de forma segura e personalizada.

Ela conta também com a possibilidade de gerar tokens de acesso garantindo que apenas usuários autorizados após o login
possam realizar a consulta da previsão do tempo dos próximos 4 dias da cidade retornada na API do INPE.

Outra funcionalidade da API, é a possibilidade de gerar logs de todas as requisições realizadas, como por exemplo: **IP
**
**Address**, **User-Agent**, **Provedor**, **Cidade** e o **código** da cidade que são salvas no ElasticSearch, podendo
ser consultado
através do endpoint /logs.

No geral a API oferece uma solução completa para o sistema de previsão do tempo, oferece uma série de funcionalidades
que podem ser úteis para diferentes tipos de sistemas.


<div id="#tecnologias-usadas"></div>

## 🔗 Tecnologias Usadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![MongoDB](https://img.shields.io/badge/mongodb-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![ElasticSearch](https://img.shields.io/badge/elasticsearch-%234ea94b.svg?style=for-the-badge&logo=elasticsearch&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-%23Clojure.svg?style=for-the-badge&logo=swagger&logoColor=white)

---

## ⚙️ Instalação

#### 💻 Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:

- Você precisa instalar o [Docker](https://docs.docker.com/engine/install/) para criar os containers do MongoDB e do
  ElasticSearch.

- Você instalar o versão mais recente do [Python](https://www.python.org/downloads/), estou utilizando a 3.11.

- Ter instalado o [Git](https://git-scm.com/downloads) para clonar o projeto.

- Possuir um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)
  ou [PyCharm](https://www.jetbrains.com/pt-br/pycharm/).

Com tudo em mãos, vamos ao passo a passo de como rodar o projeto, é bem simples a instalação de todas as dependências
para que o projeto funcione corretamente.

---

## 🎯 Execução

#### Utilize os comandos abaixo para clonar o projeto e instalar as dependências no seu terminal:

```bash
# CLonar o repositório
git clone https://github.com/matheus-feu/API-Flask-Targetdata.git

# Entrar no diretório
cd API-Flask-Targetdata

# Criar um ambiente virtual
virtualenv venv

# Ativar o ambiente virtual
venv\Scripts\activate

# Instalar as dependências
pip install -r requirements.txt
```

#### Agora vamos criar os containers:

Nesta etapa você deverá executar o comando abaixo para baixar as imagens e subir os containers do MongoDB, ElasticSearch
e da aplicação Flask, ele irá criar
os containers e baixar as imagens necessárias que estão configurada no `Dockerfile` e o  `docker-compose.yml`.

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

## 📌 Endpoints

O fluxo de requisição é da seguinte forma:

- O usuário faz o cadastro na API;
- O usuário faz o login na API e recebe um token JWT;
- O usuário passa o x-acess-token no header da requisição para consumir o endpoint de consulta da previsão do tempo.;
- O usuário envia o CEP para a API e recebe a previsão do tempo dos próximos 4 dias;
- Há um método que salva todos os logs do usuário como: IP Address, User-Agent, Provedor, 
Cidade e o código da cidade no ElasticSearch, podendo ser consultado através do endpoint /logs.

**POST** /signup - Este endpoint é responsável por realizar o registro do usuário e senha na API.

```bash
{
    "username": "username123"
    "password": "password123"
}
```

**POST** /login - Este endpoint é responsável por realizar o login na aplicação no corpo da requisição deve ser
enviado um JSON com o username e password.

```bash
{
    "username": "username123"
    "password": "password123"
}
```

Ao realizar o login será retornado um x-acess-token JWT que deverá ser enviado no header da requisição para consumir
o endpoint de consulta da previsão do tempo instruindo o CEP.

Saída do token:

```bash	
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY0MWE0NWY0M2QwYTcwMjgxZDllZjJjMyIsImV4cCI6MTY3OTQ0Njg3NCwidXNlcm5hbWUiOiJjYWx2byJ9.tjcV0GJgs-3XRA5_m4U4WZYQqrkRCQo2qznKHBJlwao"
}
```

**POST** /weather-address - Neste endpoint recebe o CEP e retorna a previsão do tempo dos 4 dias da cidade retornada
na API do INPE.

```bash
{
    "cep": "01001000"
}
```

Saída da requisição:

```bash
{
  "cep": {
    "bairro": "Sé",
    "cep": "01001-000",
    "complemento": "lado ímpar",
    "ddd": "11",
    "gia": "1004",
    "ibge": "3550308",
    "localidade": "São Paulo",
    "logradouro": "Praça da Sé",
    "siafi": "7107",
    "uf": "SP"
  },
  "cidade": {
    "atualizacao": "2023-03-21",
    "nome": "São Paulo",
    "previsao": [
      {
        "dia": "2023-03-22",
        "iuv": "10.0",
        "maxima": "28",
        "minima": "18",
        "tempo": "pn"
      },
      {
        "dia": "2023-03-23",
        "iuv": "10.0",
        "maxima": "28",
        "minima": "18",
        "tempo": "pn"
      },
      {
        "dia": "2023-03-24",
        "iuv": "10.0",
        "maxima": "29",
        "minima": "18",
        "tempo": "ci"
      },
      {
        "dia": "2023-03-25",
        "iuv": "10.0",
        "maxima": "28",
        "minima": "18",
        "tempo": "pn"
      }
    ],
    "uf": "SP"
  }
}
```

**GET** /logs - Este endpoint é responsável por retornar todos os logs da aplicação salvos no ElasticSearch.

Saída da consulta:

```bash
[
  {
    "logger": "logs_api",
    "message": "Usuario: username123 criado com sucesso"
  },
  {
    "logger": "logs_api",
    "message": "Usuario: username123 logado com sucesso"
  },
  {
    "logger": "logs_api",
    "message": "Token gerado com sucesso"
  },
  {
    "logger": "logs_api",
    "message": "Token is valid!"
  },
  {
    "logger": "logs_api",
    "message": "CEP is valid"
  },
  {
    "logger": "logs_api",
    "message": "Consulta sucedida: 01001000 - IP: 178.224.458.23 - User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0 - Provider: VIP BR TELECOM S.A - City: São Paulo - Codígo: 244"
  }
]
```

---

## 📚 Bibliotecas

### Swagger

O Swagger é uma linguagem de descrição de interface para descrever APIs RESTful expressas usando JSON. O Swagger
inclui uma documentação de interface de usuário que permite que as partes interessadas visualizem e interajam com
as recursos da API sem ter conhecimento de como a API foi implementada.

A documentação da API foi feita utilizando o Swagger, para acessar a documentação acesse o
endereço http://localhost:5000/ e você terá acesso a documentação completa da API.

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

### ElasticSearch

O ElasticSearch é um sistema de busca e análise de dados distribuído,
baseado no Apache Lucene. Ele é um serviço de busca completo e de código aberto, com recursos semelhantes aos serviços
de busca comerciais.

- Para instalá-lo, basta utilizar o comando:

```bash
pip install elasticsearch==7.14.0
```

É necessário configurar a variável de ambiente ELASTICSEARCH_URL para permitir o acesso à aplicação. Para isso, defina o
valor como http://elasticsearch:9200.

```bash
ELASTICSEARCH_URL = http://elasticsearch:9200
```

Para criar o container do ElasticSearch, adicione o serviço no arquivo docker-compose.yml com as configurações abaixo:

```bash
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.5.2
    container_name: elasticsearch
    environment:
      - discovery.type=single-node
    ports:
      - "9200:9200"
      - "9300:9300"
```

---

### 📞 Contato

- [Email](mailto:matheusfeu@gmail.com)
- [Linkedin](https://www.linkedin.com/in/matheus-feu-558558186/)
- [Github](https://github.com/matheus-feu)
- [Instagram](https://www.instagram.com/math_feu/)
