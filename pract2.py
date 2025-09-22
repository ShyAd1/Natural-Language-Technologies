import re

# Ejercicio 1

texto = "Aprender Python es divertido"
patron = re.compile("Python")

if patron.search(texto):
    print("¡Patrón encontrado!")
    print(f"Texto encontrado: {patron.search(texto).group()}")
else:
    print("Patrón no encontrado.")

# Ejercicio 2

texto = "Hola, bienvenido"
patron = r"^Hola"

if re.match(patron, texto):
    print(f"El texto comienza con 'Hola' {re.match(patron, texto)}")
else:
    print(f"El texto no comienza con 'Hola' {re.match(patron, texto)}")


# Ejercicio 3

frase = "Hoy es un gran dia"
patron = r"dia$"

if re.search(patron, frase):
    print(f"La frase termina con 'dia' {re.search(patron, frase)}")
else:
    print(f"La frase no termina con 'dia' {re.search(patron, frase)}")


# Ejercicio 4

texto = "Tengo 2 perros, 3 gatos y 1 tortuga"
patron = r"\d+"

if re.search(patron, texto):
    print(f"Se encontraron números: {re.findall(patron, texto)}")
else:
    print("No se encontraron números.")


# Ejercicio 5
cadena = "Python 3 es genial"
patron = r"\w+"

palabras = re.findall(patron, cadena)
print(f"Palabras encontradas: {palabras}")


# Ejercicio 6
texto = "Ese producto es malo y feo"
patron = r"\b(malo|feo)\b"

if re.search(patron, texto):
    resultado = re.sub(patron, "***", texto)
    print(f"Texto modificado: {resultado}")
else:
    print("No se encontraron palabras ofensivas.")


# Ejercicio 7

patron = r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{3,})"

lista_correos = ["usuario@gmail.com", "usuario@mail", "usuario@dominio.org"]

correos_validos = [correo for correo in lista_correos if re.match(patron, correo)]

print(f"Correos válidos: {correos_validos}")

# Ejercicio 8
texto = "Hoy es 16/09/2025 y mañana sera 17/09/2025"
patron = r"\d{2}/\d{2}/\d{4}"

fechas = re.findall(patron, texto)
print(f"Fechas encontradas: {fechas}")
