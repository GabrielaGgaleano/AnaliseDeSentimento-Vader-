import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from googletrans import Translator

nltk.download('vader_lexicon')

# Adiciona novas palavras ao léxico do VADER - Avaliação vai de -4.0 (Péssimo) a 4.0 (Maravilhoso)
new_words = {
    'gostosa': 3.0,  # Exemplo de palavra positiva
    'ruim': -2.0     # Exemplo de palavra negativa
}

# Tradutor de girias
substituir_palavras = {
    'gostosa': 'muito boa',
    'tesão': 'muito boa',
}

def analise_sentimento(texto):
    # Cria um objeto tradutor
    translator = Translator()

    # Substitui as gírias no texto
    for giria, traducao in substituir_palavras.items():
        texto = texto.replace(giria, traducao)

    # Traduz o texto para inglês
    texto_traduzido = translator.translate(texto, dest='en').text

    print(f"Texto traduzido: {texto_traduzido}")
    
    # Cria um objeto SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()
    sia.lexicon.update(new_words)

    # Analisa o sentimento do texto traduzido
    sentiment = sia.polarity_scores(texto_traduzido)

    print("Resultados gerais: ", sentiment)
    print(sentiment['neg']*100, "% Negativo")
    print(sentiment['neu']*100, "% Neutro")
    print(sentiment['pos']*100, "% Positivo")
    
    if sentiment['compound'] >= 0.6:
        resultado = "Ótimo"
    elif sentiment['compound'] >= 0.2:
        resultado = "Bom"
    elif sentiment['compound'] > -0.2:
        resultado = "Neutro"
    elif sentiment['compound'] > -0.6:
        resultado = "Ruim"
    else:
        resultado = "Péssimo"

    return resultado

# comentario = "Essa sopa esta muito gostosa"
comentario = "Melhor sopa que eu ja tomei"

resultado = analise_sentimento(comentario)

print(f"O texto analisado é considerado: {resultado}")