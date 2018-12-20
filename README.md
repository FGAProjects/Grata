# Esse repositório é utilizado para o desenvolvimento do projeto Grata

Link do deploy: https://projeto-grata.herokuapp.com/

O projeto Grata tem como objetivo gerar um software para gerenciar
reuniões, cadastrando informações desde a fase de preparação
da reunião, até a geração da ATA. O projeto é baseado no método
JAD (Join Application Design) que é um guia de boas práticas para
reuniões de coleta de requisitos. 

Para faciliar o desenvolvimento para contribuidores do projeto, o projeto Grata possui o docker para melhor ajudar desenvolvedores que utilizam containers para desenvolver seus projetos.

## Instalação do Docker no Windows

https://docs.docker.com/docker-for-windows/install/

## Instalação do Docker no Linux

https://docs.docker.com/install/linux/docker-ce/ubuntu/

## Como rodar o projeto

Para rodar o projeto, basta rodar os seguintes comandos:

#### No Windows

https://docs.docker.com/docker-for-windows/

#### No linux

No linux basta no terminal rodar os seguintes comandos:

```
docker-compose build
```
Esse comando irá montar a build do projeto e instalar as dependências.

```
docker-compose up
```
Esse comando irá rodar o projeto localmente.