import nltk
from nltk import bigrams, FreqDist
from nltk.tokenize import word_tokenize
import unicodedata
import random
import pandas as pd
import spacy
import re

nlp = spacy.load("es_core_news_sm")

# texto = "El principito vivía en un planeta apenas más grande que él y tenía necesidad de un amigo. Buscaba entre las estrellas y encontraba siempre el mismo silencio. Cuando por fin llegó a la Tierra, conoció muchas flores, pero ninguna como su rosa."

texto = "El sol se escondía lentamente detrás de las montañas cuando el viajero llegó al pequeño pueblo. Las casas, construidas con piedra y madera, reflejaban la luz dorada del atardecer. En la plaza central, los niños jugaban mientras los ancianos conversaban bajo los árboles. El viajero se detuvo frente a una fuente antigua y observó su reflejo en el agua tranquila. Había recorrido muchos caminos, cruzado ríos y desiertos, pero aún no había encontrado lo que buscaba. Llevaba un mapa gastado y una brújula que apenas funcionaba. Una mujer se acercó con una sonrisa amable y le ofreció un poco de pan. Él agradeció el gesto y le preguntó por el camino hacia el norte. La mujer señaló la carretera que cruzaba el valle y desaparecía entre las colinas. El viajero respiró profundamente y siguió su marcha. A medida que avanzaba, la noche cubría el cielo con un manto de estrellas. Cada paso lo acercaba a su destino, aunque todavía no sabía cuál era. El viento soplaba suave, trayendo consigo el aroma del bosque y el murmullo de los insectos. En ese silencio, comprendió que el viaje era más importante que la llegada."

texto = texto.lower()

texto = re.sub(r"[^\w\s]", "", texto)

texto = "".join(
    (c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn")
)

tokens = word_tokenize(texto)

freq_words = FreqDist(tokens)
print("Frecuencia de palabras:")
for word, freq in freq_words.items():
    print(f"{word}: {freq}")

bigrams_list = list(bigrams(tokens))
freq_dist = FreqDist(bigrams_list)
print("Lista de bigramas y sus frecuencias:")
for bigram, freq in freq_dist.items():
    print(f"{bigram}: {freq}")


def calcular_probabilidad(bigram, freq_dist, freq_words):
    return freq_dist[bigram] / freq_words[bigram[0]] if freq_words[bigram[0]] > 0 else 0


for bigram in bigrams_list:
    prob = calcular_probabilidad(bigram, freq_dist, freq_words)
    print(f"Probabilidad del bigrama {bigram}: {prob:.4f}")


def predecir_palabra_siguiente(palabra):
    # Candidatos pero por la probabilidad
    candidatos = [bigram[1] for bigram in freq_dist.keys() if bigram[0] == palabra]
    # print(f"Candidatos para la palabra '{palabra}': {candidatos}")
    if candidatos:
        return random.choice(candidatos)
    else:
        return None


print("\n\n\n\nPredicción de la siguiente palabra para 'el':")
print(predecir_palabra_siguiente("el"))
print("\nPredicción de la siguiente palabra para 'principito':")
print(predecir_palabra_siguiente("principito"))


def genetar_texto(palabra_inicial, longitud=10):
    texto_generado = [palabra_inicial]
    for _ in range(longitud - 1):
        siguiente_palabra = predecir_palabra_siguiente(texto_generado[-1])
        if siguiente_palabra:
            texto_generado.append(siguiente_palabra)
        else:
            break
    return " ".join(texto_generado)


print("\nGeneración de texto a partir de 'el':")
print(genetar_texto("el", 20))
