import re


def extraer_informacion(informacion):
    patron = re.compile(
        r"Nombre:\s*([A-Za-zÁÉÍÓÚáéíóúÑñ\s]+),\s*Email:\s*([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}),\s*Tel:\s*(\+\d{2}-\d{2}-\d{4}-\d{4})"
    )

    if patron.search(informacion):
        nombre = re.search(r"([A-Za-zÁÉÍÓÚáéíóúÑñ\s]+),", informacion).group(1)
        email = re.search(
            r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", informacion
        ).group(1)
        telefono = re.search(r"(\+\d{2}-\d{2}-\d{4}-\d{4})", informacion).group(1)
        print(f"{nombre:15} | {email:25} | {telefono}")
    else:
        print("No se encontró información válida.")


informacion1 = (
    "Nombre: Juan Pérez, Email: juan.perez@example.com, Tel: +52-55-1234-5678"
)

informacion2 = (
    "Nombre: María López, Email: maria.lopez@uni.edu.mx, Tel: +52-81-9876-5432"
)

informacion3 = "Nombre: Pedro Ramírez, Email: pedro99@gmail.com, Tel: +52-33-5555-6666"

print("Nombre          |   Email                   |   Telefono")
print("-" * 62)
extraer_informacion(informacion1)
extraer_informacion(informacion2)
extraer_informacion(informacion3)
