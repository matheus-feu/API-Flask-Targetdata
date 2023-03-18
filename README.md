# Vaga Desenvolvedor Python Backend

## Teste:

### **Criar uma Api usando Python e Flask retornando JSON integrando com duas APIs públicas e gratuitas.**

Passo a passo:

- [x]  Crie um banco de dados **MongoDB** em Docker.
- [x]  Crie um **ElasticSearch** em Docker.
- [x]  Crie uma API utilizando **Flask** e **Python**.
- [x]  Crie um endpoint na sua api para criar usuário e senha e salvar no mongoDB.
- [x]  Crie outro endpoint na sua api para criar um **access token**.
- [x]  Crie um endpoint na sua api com o método **“POST”** com um campo **CEP** requirido, onde será consultado o endereço usando o CEP na api da ViaCEP ([https://viacep.com.br/](https://viacep.com.br/)) e pegar a cidade retornada e buscar a previsão do tempo dos 4 dias dessa cidade na api do INPE ([http://servicos.cptec.inpe.br/XML/](http://servicos.cptec.inpe.br/XML/)).

<aside>
💡 **Obs:** A sua api deve retornar todos os campos da ViaCEP e do INPE juntos em JSON.

</aside>

- [ ]  Crie logs de todas as requisições feita na sua api e salve no **ElasticSearch.**
- [ ]  Crie um endpoint na sua api com o método **“GET”** para trazer todos os logs do usuário.
    - Basicamente, o log de todas as informações da requisição possível do endpoint de consulta do CEP, como:
        - IP
        - User Agent,
        - CEP consultado
        - Usuário que fez a requisição
        
        E se conseguir:
        
        - localização do IP e o provedor.
- [ ]  Crie uma documentação utilizando Swagger que fique disponível no endpoint **‘’/docs”.**
- [ ]  Crie um arquivo Dockfile e docker-compose.yaml para rodar o container da api.

<aside>
💡 **Obs:** Todos os endpoints devem retornar JSON.

</aside>
