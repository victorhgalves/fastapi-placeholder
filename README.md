# API - Place Holder

Principais dependências:
- [FastApi](https://fastapi.tiangolo.com/)

### Como iniciar a API localmente
1- Configure o ambiente virtual:
```shell script
python -m venv venv
```

2- Ative o ambiente virtual:
```shell script
source venv/bin/activate
```

3- Execute o comando para instalar as dependências:
```shell script
make requirements-dev
```
4- Agora basta executar o comando abaixo para iniciar o aplicativo.
O comando abaixo ira executar a aplicacao localmente
```shell script
make run
```

### Como iniciar a API usando Docker

1 - Vá para o diretório do projeto:

2 - Execute o aplicativo com o seguinte comando para executar o container docker:
```bash

docker build -t api-framework . 

docker run -p 5001:5001 api-framework

```

## Para testar o projeto

1 - Efetuar Download do framework.postman_collection.json e importar no seu Postman

