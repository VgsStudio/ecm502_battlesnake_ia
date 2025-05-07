# battlesnake com AStar  🐍

Este trabalho realiza a implementação de uma inteligência artificial para o jogo [Battlesnake](http://play.battlesnake.com)  utilizando o algoritmo A*. O objetivo é criar uma estratégia eficiente para movimentar a cobra no tabuleiro, coletando comida e evitando colisões com outras cobras, bordas e perigos.

## Integrantes
- Enzo Yuji Sakamoto **21.00210-0**
- João Vitor Choueri Branco **21.01075-7**
- Pedro Henrique de Sousa Matumoto - **21.00784-5**
- Rafael Rubio Carnes - **20.00611-0**
- Vitor Guirão Soller - **21.01444-2**


## O que é o algoritmo A*?
A* é um algoritmo de busca de caminho que encontra o caminho mais curto entre dois pontos em um grafo. Ele é amplamente utilizado em jogos e aplicações de inteligência artificial para encontrar rotas eficientes. O algoritmo combina a busca em largura com uma heurística que estima o custo restante para chegar ao destino, permitindo que ele explore os caminhos mais promissores primeiro.

## O que é o Battlesnake?
Segundo o site oficial: "Battlesnake é um jogo de programação competitivo onde seu código é o controle".

![FastApi AWS drawio](https://miro.medium.com/v2/resize:fit:1400/1*l0IkrbNLnkCB1VzDq2Qy7A.gif)

Cada jogador controla uma cobra que deve se mover pelo tabuleiro, coletando comida e evitando colisões com outras cobras e com as bordas do tabuleiro. O objetivo é sobreviver o maior tempo possível. Cada cobra é controlada através de uma API. Nós conhecemos esse evento através do Campeonato Battlesnake organizado anualmente pela Dev. Community Mauá. Eles desenvolveram um template que utilizamos de base para nosso projeto. Todos estão convidados a utilizar o template para desenvolver suas cobras e participar do campeonato.

## O que exatamente fizemos?
Neste projeto, fizemos a nossa própria interpretação da API do jogo, utilizando o algoritmo A* para encontrar o caminho mais curto até a comida. O código é dividido em duas partes principais: a implementação do algoritmo A* e a lógica do Battlesnake.

O notebook com a implementação, demonstração e explicação do que foi feito pode ser encontrada [aqui](https://github.com/VgsStudio/ecm502_battlesnake_ia/tree/dev/notebook)

## Como rodar 🤔
Crie um ambiente virtual e instale os requisitos

## Instalação 👩‍💻

### Criar ambiente virtual em python (somente na primeira vez)

###### Windows

    python -m venv venv

###### Linux

    virtualenv -p python3.9 venv

#### Ativar a venv

###### Windows:

    venv\Scripts\activate

###### Linux:

    source venv/bin/activate

#### Instalar os requirements

    pip install -r requirements-dev.txt
    pip install -r requirements.txt
    cd notebook
    pip install -r requirements.txt
    


### Executar o notebook
