import re
import unicodedata
import nltk

# Descargar recursos necesarios de NLTK
# nltk.download("punkt")
# nltk.download("punkt_tab")
# nltk.download("stopwords")
# nltk.download("wordnet")

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Texto de ejemplo
texto = "Los autos son más RÁPIDOS que las bicicletas, pero las bicicletas son más ecológicas."

# 1.- Pasar a minúsculas
texto = texto.lower()

# 2.- Eliminar puntuacion
texto = re.sub(r"[^\w\s]", "", texto)

# 3.- Elminar acentos
texto = "".join(
    (c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn")
)

# 4.- Tokenización
tokens = word_tokenize(texto)

# 5.- Eliminar stopwords en español
stop_words = set(stopwords.words("spanish"))
tokens = [word for word in tokens if word not in stop_words]

# 6.- Lematización
lemmatizer = WordNetLemmatizer()
tokens = [lemmatizer.lemmatize(word) for word in tokens]

print(f"Tokens procesados: {tokens}")
