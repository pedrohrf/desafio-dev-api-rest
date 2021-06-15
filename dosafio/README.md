# Seja Bem Vindo
Esse é o projeto que desenvolvi para resolver o [desafio](https://github.com/pedrohrf/desafio-dev-api-rest) proposto pela Dock.

## Considerações iniciais
Inicialmente gostaria de dizer que achei o desafio legal, e tentei fazer o projeto conforme minhas práticas cotidianas.
Os comandos especificados nessa página são para Linux, mas nada impede o sistema de rodar em outros SO's basta adapta-los.

### Tecnologias

#### Linguagem, bibliotecas e Frameworks
O projeto foi feito utilizando Python3.8 e o framework [Bottle](https://pypi.org/project/bottle/).
Escolhi pela simplicidade e comodidade pois já trabalho com eles.
As libs do Python que utilizei:

* [Cerberus](https://pypi.org/project/Cerberus/)
* [neo4j](https://pypi.org/project/neo4j/)
* [pytest](https://pypi.org/project/pytest/)
* [pytest-cov](https://pypi.org/project/pytest-cov/)
* [parameterized](https://pypi.org/project/parameterized/)


### Banco de Dados
Neo4j

### Padrões
Para esse projeto decidi seguir a seguinte hierarquia de diretorios:
```.tree
.
├── app.py
├── README.md
├── requirements_testing.txt
├── requirements.txt
├── setup.cfg
└── src
    ├── app_factory.py
    ├── exceptions.py
    ├── business
    │   ├── cerberus_rules.py
    │   ├── account
    │   │   ├── register.py
    │   │   ├── search.py
    │   │   └── transaction.py
    │   └── person
    │       ├── register.py
    │       └── search.py
    ├── components
    │   ├── database.py
    ├── entities
    │   ├── account.py
    │   ├── person.py
    │   └── transaction.py
    ├── helpers
    │   ├── cerberus_validator.py
    │   ├── neo4j_helper.py
    │   ├── adapters
    │   │   └── db_query
    │   │       ├── create.py
    │   │       ├── match.py
    │   │       └── update.py
    │   └── enum
    │       ├── database.py
    │       ├── messages.py
    │       └── system_variables.py
    ├── security
    │   └── configurations.py
    └── services
        ├── payloads
        │   ├── account.py
        │   ├── person.py
        │   └── transaction.py
        ├── account_services.py
        ├── person_services.py
        ├── transaction_services.py
        └── utils
            └── responses.py
```
Evitando assim dependencias cíclicas. a Seguir a responsábilidade de cada módulo:
* App - Iniciar
* Services - Definir os serviços, além formatos de entrada e saída
* Business - Definir regras de negócio
* Components - Centralizar acesso a componentes do sistema, como banco de dados.
* Helpers - Módulos/Classes para auxiliar/centralizar o uso de bibliotecas e/ou partes comuns genéricas as quais podem ser reaproveitadas 
* Entities - Classes as quais representão as entidades utilizadas

Tentei ao máximo fazer um código limpo sem redundâncias e fácil de ler de uma maneira Pythonica.

### Testes unitários
Na pasta [tests](https://github.com/pedrohrf/desafio-dev-api-rest/tree/master/dosafio/tests) 
estão os testes unitários, fiz 100% da cobertura do código, excluindo algumas partes as quais
não fazia sentido testar (verifique o arquivo [setup.cfg](https://github.com/pedrohrf/desafio-dev-api-rest/blob/master/dosafio/setup.cfg) 
para mais informações).

## Executando o Projeto
Primeiramente faça o clone do projeto em sua maquina e acesse a pasta do projeto.

#### Neo4j
Faça o pull da imagem do docker oficial do [neo4j](https://hub.docker.com/_/neo4j)

#### Criando ambiente de desenvolvimento e Instalando dependências
Primeiramente voce irá precisar do [python3.8](https://www.python.org/downloads/release/python-388/)
Caso esteja usando Linux, pode ser que os comandos lhe ajudem:
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt install python3.8 python3.8-dev python3.8-venv 
```
Na pasta do projeto iremos criar o ambiente de virtual e instalar as dependencias do projeto:
```
python3.8 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Por fim, para executar o projeto:
```
python app.py
```
Fique atento as variáveis de ambiente, pois talvez seja necessário adapta-las:
DB_URI
DB_USER
DB_PASSWORD

## Testes Unitários
Para executar os testes unitários, é necessário executar primeiro o tópico 
<Criando ambiente de desenvolvimento e Instalando dependências>, depois de concluído, basta executar:
```
pip install -r requirements_testing.txt
source env_test
pytest
```

## Como usar 
Para informações das chamadas e retornos consulte o swagger na raiz do projeto. Para visualiza-lo melhor 
copie o conteudo em: https://editor.swagger.io/ ou pode usar um [script](https://gist.github.com/oseiskar/dbd51a3727fc96dcf5ed189fca491fb3).

## Considerações finais
Finalizo pedindo desculpas pelos erros de português e com uma frase do Edsger Dijkstra: 
> Testing shows the presence, not the absence of bugs.

Divirta-se! :)