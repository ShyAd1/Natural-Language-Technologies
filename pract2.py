import re

# Ejercicio 1

texto = "Ana_ 123, Pedro!, @Luis45, Maria99##, #Sofía"
patron = r"[\d\W_]+"

print(re.sub(patron, ", ", texto))

# Ejercicio 2

texto = '192.168.1.1 - - [16/Sep/2025:10:30:00] "GET /index.html HTTP/1.1" 200 1024'
patron_ip = r"[\d{1,3}\.]+"
patron_fecha = r"\d{2}/[A-Za-z]{3}/\d{4}:[\d{2}:]+"
patron_GET = r"GET"

ip = re.search(patron_ip, texto).group()
fecha = re.search(patron_fecha, texto).group()
metodo = re.search(patron_GET, texto).group()

print(f"IP: {ip} \nFecha y hora: {fecha} \nMétodo: {metodo}")
