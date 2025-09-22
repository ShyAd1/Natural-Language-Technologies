import re

resultado = re.findall("\s", "esta es una cadena.")
print(resultado)

resultado = re.split("\s", "esta es una cadena.")
print(resultado)

resultado = re.sub("\s", "\n", "esta es una cadena.")
print(resultado)

patron = re.compile(",")
resultado = patron.findall("cadena1, cadena2, cadena3, cadena4, cadena5")
print(resultado)
resultado = patron.split("cadena1, cadena2, cadena3, cadena4, cadena5")
print(resultado)


patron = re.compile("\d+\.?\d*")
resultado = patron.findall("Esta es una cadena con los numeros 14, 15.5 y 0.25")
print(resultado)
