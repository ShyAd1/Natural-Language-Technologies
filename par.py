# a = int(input("igresa un numero:"))

# if a % 2:
#     print("El numero es impar")
# else:
#     print("El numero es par")


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)


# num = int(input("ingresa un numero: "))
# print(f"el factorial de {num} es: {factorial(num)}")


cadena = input("ingresa una cadena: ")
print("Cadena invertida: ", cadena[::-1])
print("Cadena en minusculas: ", cadena.lower())
vocales = "aeiouAEIOU"
contador = sum(1 for letra in cadena if letra in vocales)
print("Cantidad de vocales: ", contador)

if cadena.strip().lower().replace(" ", "") == cadena[::-1].strip().lower().replace(
    " ", ""
):
    print("La cadena es un palindromo")
else:
    print("La cadena no es un palindromo")
