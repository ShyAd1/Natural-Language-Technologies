import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import matplotlib.pyplot as plt
import spacy

# -------------------------------
# Parte 1
# -------------------------------
docs = [
    "el gato duerme en la cama",
    "el perro duerme en el sofá",
    "el gato corre en el jardín",
]

vectorizador = CountVectorizer()
X = vectorizador.fit_transform(docs)

# Mostrar matriz de frecuencias
tf = pd.DataFrame(X.toarray(), columns=vectorizador.get_feature_names_out())
print("Frecuencia (TF) absoluta:")
print(tf)

# -------------------------------
# Parte 2
# -------------------------------
# Calcula el TF-IDF de los documentos anteriores, usando tfidf_vectorizer
tfidf_vectorizador = TfidfVectorizer()
X_tfidf = tfidf_vectorizador.fit_transform(docs)
tfidf = pd.DataFrame(
    X_tfidf.toarray(), columns=tfidf_vectorizador.get_feature_names_out()
)
print("\nTF-IDF:")
print(tfidf)

# -------------------------------
# Parte 3
# -------------------------------
docs2 = [
    "la inteligencia artificial aprende de los datos",
    "la inteligencia humana razona con lógica",
    "el aprendizaje automático usa datos y modelos",
]
# Calcula el TF-IDF y muestra los términos más importantes por documento.
tfidf_vectorizador = TfidfVectorizer()
X_tfidf2 = tfidf_vectorizador.fit_transform(docs2)
tfidf2 = pd.DataFrame(
    X_tfidf2.toarray(), columns=tfidf_vectorizador.get_feature_names_out()
)
print("\nTF-IDF:")
print(tfidf2)

# Mostrar los términos más importantes por documento
for i, doc in enumerate(docs2):
    doc_tfidf = X_tfidf2[i].toarray()[0]
    top_indices = np.argsort(doc_tfidf)[::-1][:3]  # Top 3 términos
    top_terms = [
        (tfidf_vectorizador.get_feature_names_out()[idx], doc_tfidf[idx])
        for idx in top_indices
        if doc_tfidf[idx] > 0
    ]
    print(f"\nDocumento {i+1}: '{doc}'")
    print("Términos más importantes (TF-IDF):")
    for term, score in top_terms:
        print(f"  {term}: {score:.4f}")

# -------------------------------
# Parte 4
# -------------------------------
# Usando matplotlib, muestra el vocabulario de docs2.
vocabulario = tfidf_vectorizador.get_feature_names_out()
frecuencias = np.sum(X_tfidf2.toarray(), axis=0)

plt.figure(figsize=(12, 6))
plt.barh(vocabulario, frecuencias)
plt.xlabel("Frecuencia")
plt.title("Vocabulario de docs2")
plt.show()

# -------------------------------
# Parte 5
# -------------------------------
# Intentar cargar el modelo en español
nlp = spacy.load("es_core_news_sm")

# 1.- Pasar a minúsculas
textos = [texto.lower() for texto in docs2]

# 4.- Tokenización, lematización y filtrado con spaCy
docs = [nlp(texto) for texto in textos]

# 5.- Eliminar stopwords
tokens_per_doc = [
    [token.lemma_.lower() for token in doc if token.is_alpha and not token.is_stop]
    for doc in docs
]

# Calcula el TF-IDF y muestra los términos más importantes por documento.
tfidf_vectorizador = TfidfVectorizer()
document_texts = [" ".join(toks) for toks in tokens_per_doc]
X_tfidf = tfidf_vectorizador.fit_transform(document_texts)
tfidf = pd.DataFrame(
    X_tfidf.toarray(), columns=tfidf_vectorizador.get_feature_names_out()
)
print("\nTF-IDF con spaCy:")
print(tfidf)

# Mostrar los términos más importantes por documento
for i, doc in enumerate(document_texts):
    doc_tfidf = X_tfidf[i].toarray()[0]
    top_indices = np.argsort(doc_tfidf)[::-1][:3]  # Top 3 términos
    top_terms = [
        (tfidf_vectorizador.get_feature_names_out()[idx], doc_tfidf[idx])
        for idx in top_indices
        if doc_tfidf[idx] > 0
    ]
    print(f"\nDocumento {i+1}: '{doc}'")
    print("Términos más importantes (TF-IDF con spaCy):")
    for term, score in top_terms:
        print(f"  {term}: {score:.4f}")

# Mostrar el vocabulario
vocabulario = tfidf_vectorizador.get_feature_names_out()
frecuencias = np.sum(X_tfidf.toarray(), axis=0)
plt.figure(figsize=(12, 6))
plt.barh(vocabulario, frecuencias)
plt.xlabel("Frecuencia")
plt.title("Vocabulario con spaCy")
plt.show()
