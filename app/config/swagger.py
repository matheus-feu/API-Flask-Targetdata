template = {
    "swagger": "2.0",
    "info": {
        "title": "Flask API - Targetdata - Consulta de CEP",
        "description": "Esta API é capaz de fornecer aos usuários informações precisas sobre CEP, permitindo a consulta de dados relevantes como endereço, bairro, cidade e estado. "
                       "Além disso, a API também oferece a funcionalidade de previsão do tempo para até quatro dias com base no CEP fornecido, permitindo que os usuários se planejem para as condições climáticas futuras."
                       "\n\nPara garantir a segurança dos dados dos usuários, a API conta com um sistema de cadastro de usuários e login, que gera um token de acesso exclusivo para cada usuário. "
                       "Esse token é necessário para acessar os endpoints da API e garantir que apenas usuários autorizados possam obter as informações disponíveis."
                       "\n\nCom essa API, os usuários podem ter acesso a informações precisas e atualizadas sobre CEP e previsão do tempo, permitindo um planejamento mais eficiente e uma melhor organização das atividades diárias."
        ,
        "contact": {
            "email": "matheusfeu@gmail.com",
            "url": "https://www.linkedin.com/in/matheus-feu-558558186/",
        },
        "version": "v1.0.0"
    },
    "basePath": "/api/",  # base bash for blueprint registration
    "schemes": [
        "http",
        "https"
    ],
    "securityDefinitions": {
        "APIKeyHeader": {
            "type": "apiKey",
            "name": "x-access-token",
            "in": "header",
            "description": "Authorization header using the APIKeyHeader scheme. Example: \"Authorization: APIKeyHeader {token}\""
        }
    },
}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/"
}
