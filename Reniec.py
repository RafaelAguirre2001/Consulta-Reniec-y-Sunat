import requests

dni = input("Ingrese el número de DNI: ")
ruc = input("Ingrese el número de RUC: ")

# Consulta del DNI
url_dni = f"https://api.apis.net.pe/v1/dni?numero={dni}"
response_dni = requests.get(url_dni)

if response_dni.ok:
    try:
        data_dni = response_dni.json()
        print(f"Nombre completo: {data_dni['apellidoPaterno']} {data_dni['apellidoMaterno']}, {data_dni['nombres']}")
        print(f"DNI: {data_dni['numeroDocumento']}")
    except ValueError:
        print("La respuesta del servidor no contiene datos JSON válidos.")
else:
    print("No se pudo obtener información del DNI ingresado.")

# Consulta del RUC
url_ruc = f"https://api.apis.net.pe/v1/ruc?numero={ruc}"
response_ruc = requests.get(url_ruc)

if response_ruc.ok:
    try:
        data_ruc = response_ruc.json()
        print(f"RUC: {data_ruc['numeroDocumento']}")
        print(f"Estado: {data_ruc['estado']}")
        print(f"Condicion: {data_ruc['condicion']}")
    except ValueError:
        print("La respuesta del servidor no contiene datos JSON válidos.")
else:
    print("No se pudo obtener información del RUC ingresado.")
