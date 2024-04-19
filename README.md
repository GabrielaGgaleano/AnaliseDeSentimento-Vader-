# Análise de Sentimento- Vader com Python

Este projeto é uma aplicação de análise de sentimentos que usa a biblioteca NLTK (Natural Language Toolkit) para analisar o sentimento de um texto inserido pelo usuário.

## Funcionalidades

* Tradução de gírias para palavras mais "formais"
* Análise de sentimentos usando o léxico VADER do NLTK
* Interface gráfica simples usando Tkinter

## Dependências

Para executar este projeto, você precisa ter as seguintes bibliotecas instaladas:

* nltk
* tkinter
* googletrans

Você pode instalar essas dependências usando pip:

bash
pip install nltk tkinter googletrans


## Como usar

1. Execute o script Python.
2. Insira o texto que deseja analisar na caixa de entrada.
3. Clique no botão “Analisar”.

O resultado da análise de sentimentos será exibido abaixo do botão. Os resultados possíveis são:

- Ótimo para sentimentos com pontuação composta maior ou igual a 0.6
- Bom para sentimentos com pontuação composta entre 0.2 e 0.6
- Neutro para sentimentos com pontuação composta entre -0.2 e 0.2
- Ruim para sentimentos com pontuação composta entre -0.6 e -0.2
- Péssimo para sentimentos com pontuação composta menor ou igual a -0.6

## Nota Importante
O léxico VADER do NLTK realiza a análise de sentimento somente para palavras em inglês. Devido a isso, precisamos traduzir as palavras que recebemos. No entanto, devido a problemas de traduções, é necessário também tratar palavras que possam ter um significado diferente ao realizar uma tradução direta do português para a língua inglesa. Além disso, é possível inserir novas palavras para treinamento do algoritmo, sendo possível informar o seu valor entre o intervalo de -4, para uma palavra péssima, e 4 para uma ótima palavra.

## Licença

Este projeto está licenciado sob a licença MIT.