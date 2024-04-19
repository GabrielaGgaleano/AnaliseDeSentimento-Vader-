import tkinter as tk
from tkinter import ttk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from googletrans import Translator
import nltk

nltk.download('vader_lexicon')

# Adiciona novas palavras ao léxico do VADER - Avaliação vai de -4.0 (Péssimo) a 4.0 (Maravilhoso)
new_words = {
    'gostosa': 3.0,  # Exemplo de palavra positiva
    'ruim': -2.0     # Exemplo de palavra negativa
}

# Tradutor de gírias
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

    # Cria um objeto SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()
    sia.lexicon.update(new_words)

    # Analisa o sentimento do texto traduzido
    sentiment = sia.polarity_scores(texto_traduzido)

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

    return resultado, sentiment

def calcular_sentimento():
    comentario = comentario_entry.get()
    resultado, sentiment = analise_sentimento(comentario)
    resultado_label.config(text=f"O texto analisado é considerado: {resultado} ({sentiment['compound']})")
    porcentagem_label.config(text=f"Positivo: {sentiment['pos']*100:.2f}% | Neutro: {sentiment['neu']*100:.2f}% | Negativo: {sentiment['neg']*100:.2f}%")

# Configuração da janela principal
root = tk.Tk()
root.title("Análise de Sentimento")

# Criando widgets
comentario_label = ttk.Label(root, text="Digite o comentário:")
comentario_entry = ttk.Entry(root, width=50)
analise_button = ttk.Button(root, text="Analisar", command=calcular_sentimento)
resultado_label = ttk.Label(root, text="")
porcentagem_label = ttk.Label(root, text="")

# Posicionamento dos widgets
comentario_label.grid(row=0, column=0, padx=10, pady=10)
comentario_entry.grid(row=0, column=1, padx=10, pady=10)
analise_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
resultado_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
porcentagem_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Iniciando o loop principal da aplicação
root.mainloop()