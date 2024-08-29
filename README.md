## Desafio técnico de API REST
Neste projeto, criarei uma API REST usando majoritariamente Python e MySQL para criar uma API REST que armazena dados de anotações em imagens.

A API foi desenvolvida usando Flask, JSONIFY e SQLAlchemy como o ORM.

Em cada módulo Python temos seu próprio arquivo de teste unitário, alguns os quais serão posteriormente deletados
para melhorar a legibilidade, pois não servem a muito mais funções além de testar a alocação e 
instanciamento de determinado recurso; O projeto também tem partes do código onde foi usada uma ferramenta muito prática do 
Python chamada programação reflexiva, que pode ser meio confusa aos leitores que nunca viram,
mas abrevia muito a criação de código e creio estar bem explicada em comentários.

Após a criação da API estou dando seguimento aos testes no Postman, e o primeiro caso está OK.

Foi efetuado o primeiro teste a uma requisição GET apenas para testar a resposta do servidor do Flask
com os seguintes resultados:

![Imagem tela do postman](tela_postman_resposta.PNG)

Note que a API devolve um JSON com as classes de veículos, 
e aqui temos a imagem do servidor Flask recebendo a requisição:

![Imagem Flask recebendo o GET](tela_cmd_Flask.PNG)
