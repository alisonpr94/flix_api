Flix API
=========

Overview
---------

Esta é uma API RESTful para gerenciar informações sobre filmes e suas avaliações. A API oferece operações CRUD (Create, Read, Update, Delete) para atores, gêneros, filmes e avaliações. Utiliza os métodos HTTP para interação e retorna dados em formato JSON.

Endpoints
----------

### Atores (Actors)
- #### Listar Atores:
    - Método: GET
    - Endpoint: /api/v1/actors
    - Resposta: Lista de atores.

- #### Detalhes do Ator:
    - Método: GET
    - Endpoint: /api/v1/actors/:id
    - Resposta: Detalhes do ator com o ID especificado.

- #### Adicionar Ator:
    - Método: POST
    - Endpoint: /api/v1/actors
    - Corpo da Requisição: JSON com informações do ator.
    - Resposta: Ator adicionado.

- #### Atualizar Ator:
    - Método: PUT
    - Endpoint: /api/v1/actors/:id
    - Corpo da Requisição: JSON com informações atualizadas do ator.
    - Resposta: Ator atualizado.

- #### Remover Ator:
    - Método: DELETE
    - Endpoint: /api/v1/actors/:id
    - Resposta: Ator removido.

### Gêneros (Genres)
- #### Listar Gêneros:
    - Método: GET
    - Endpoint: /api/v1/genres
    - Resposta: Lista de gêneros.

- #### Detalhes do Gênero:
    - Método: GET
    - Endpoint: /api/v1/genres/:id
    - Resposta: Detalhes do gênero com o ID especificado.

- #### Adicionar Gênero:
    - Método: POST
    - Endpoint: /api/v1/genres
    - Corpo da Requisição: JSON com informações do gênero.
    - Resposta: Gênero adicionado.

- #### Atualizar Gênero:
    - Método: PUT
    - Endpoint: /api/v1/genres/:id
    - Corpo da Requisição: JSON com informações atualizadas do gênero.
    - Resposta: Gênero atualizado.

- #### Remover Gênero:
    - Método: DELETE
    - Endpoint: /api/v1/genres/:id
    - Resposta: Gênero removido.

### Filmes (Movies)
- #### Listar Filmes:
    - Método: GET
    - Endpoint: /api/v1/movies
    - Resposta: Lista de filmes.

- #### Detalhes do Filme:
    - Método: GET
    - Endpoint: /api/v1/movies/:id
    - Resposta: Detalhes do filme com o ID especificado.

- #### Adicionar Filme:
    - Método: POST
    - Endpoint: /api/v1/movies
    - Corpo da Requisição: JSON com informações do filme.
    - Resposta: Filme adicionado.

- #### Atualizar Filme:
    - Método: PUT
    - Endpoint: /api/v1/movies/:id
    - Corpo da Requisição: JSON com informações atualizadas do filme.
    - Resposta: Filme atualizado.

- #### Remover Filme:
    - Método: DELETE
    - Endpoint: /api/v1/movies/:id
    - Resposta: Filme removido.

### Avaliações (Reviews)
- #### Listar Avaliações:
    - Método: GET
    - Endpoint: /api/v1/reviews
    - Resposta: Lista de avaliações.

- #### Detalhes da Avaliação:
    - Método: GET
    - Endpoint: /api/v1/reviews/:id
    - Resposta: Detalhes da avaliação com o ID especificado.

- #### Adicionar Avaliação:
    - Método: POST
    - Endpoint: /api/v1/reviews
    - Corpo da Requisição: JSON com informações da avaliação.
    - Resposta: Avaliação adicionada.

- #### Atualizar Avaliação:
    - Método: PUT
    - Endpoint: /api/v1/reviews/:id
    - Corpo da Requisição: JSON com informações atualizadas da avaliação.
    - Resposta: Avaliação atualizada.

- #### Remover Avaliação:
    - Método: DELETE
    - Endpoint: /api/v1/reviews/:id
    - Resposta: Avaliação removida.

Requisitos
----------

Faça o clone do reposirório.

    git clone git@github.com:alisonpr94/flix_api.git

Crie um ambiente virtual

    python -m venv venv

Instale as dependências.

    pip install -r requirements.txt