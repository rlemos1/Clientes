# Projeto de Favoritos

Este projeto consiste em duas partes principais: uma aplicação web e uma aplicação mobile. Ambas interagem com um servidor para adicionar e visualizar URLs de imagens favoritas.

## Estrutura do Projeto

### Aplicação Web

A aplicação web é desenvolvida com Flask e exibe uma lista de imagens favoritas. Ela tem duas funcionalidades principais:
1. **Visualizar Favoritos**: Mostra uma lista de imagens favoritas salvas.
2. **Adicionar Favorito**: Permite que o usuário adicione uma nova URL de imagem à lista de favoritos.

#### Dependências

- Flask
- Requests

#### Instruções de Uso

1. **Instalação**:
   ```bash
   pip install flask requests

2. **Executar a Aplicação:**:
   Execute o servidor Flask:
   
   ```bash
    python app.py

A aplicação web será acessível em http://127.0.0.1:5001.

# Aplicação Mobile

A aplicação mobile é desenvolvida com Kivy e oferece uma interface para adicionar e atualizar a lista de imagens favoritas.

## Dependências

- Kivy
- Requests

## Instruções de Uso

### Instalação

1. **Instale as dependências necessárias com o seguinte comando:**
    ```bash
    pip install kivy requests

2. **Executar a Aplicação:**:
   Para iniciar a aplicação mobile, execute o seguinte comando:
   
   ```bash
    python mobile_app.py
A aplicação será iniciada em seu dispositivo móvel ou emulador.

### Funcionalidades

Adicionar Favorito: Insira uma URL de imagem e pressione o botão "Add Favorite".
Atualizar Favoritos: Pressione o botão "Update Favorites" para ver a lista atualizada de imagens favoritas.
