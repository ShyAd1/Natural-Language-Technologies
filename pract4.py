from sklearn.feature_extraction.text import CountVectorizer
import spacy

# Intentar cargar el modelo en español
nlp = spacy.load("es_core_news_sm")

# Texto de ejemplo
textos_originales = [
    "Los autos son más RÁPIDOS que las bicicletas, pero las bicicletas son más ecológicas.",
    "Los profesores enseñan programación y matemáticas.",
    "La inteligencia artificial aprende de los datos.",
]

# 1.- Pasar a minúsculas
textos = [texto.lower() for texto in textos_originales]

# 4.- Tokenización, lematización y filtrado con spaCy
docs = [nlp(texto) for texto in textos]

# 5.- Eliminar stopwords
tokens_per_doc = [
    [token.lemma_.lower() for token in doc if token.is_alpha and not token.is_stop]
    for doc in docs
]
print(f"Tokens: {tokens_per_doc}")

# 6.- Vectorización
# Matriz global (vocabulario conjunto de todos los documentos)
vectorizador_global = CountVectorizer(binary=True)
document_texts = [" ".join(toks) for toks in tokens_per_doc]
matriz_global = vectorizador_global.fit_transform(document_texts)
print(f"Vocabulario global: {vectorizador_global.get_feature_names_out()}")
print(f"Matriz global (docs x features):\n{matriz_global.toarray()}")
