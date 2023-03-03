import requests

def consultar_dni(dni):
    url_dni = f"https://api.apis.net.pe/v1/dni?numero={dni}"
    response_dni = requests.get(url_dni)
    data_dni = response_dni.json()
    nombre_completo = f"{data_dni['apellidoPaterno']} {data_dni['apellidoMaterno']}, {data_dni['nombres']}"
    dni = data_dni['numeroDocumento']
    return nombre_completo, dni

def consultar_ruc(ruc):
    url_ruc = f"https://api.apis.net.pe/v1/ruc?numero={ruc}"
    response_ruc = requests.get(url_ruc)
    data_ruc = response_ruc.json()
    ruc = data_ruc['numeroDocumento']
    estado = data_ruc['estado']
    condicion = data_ruc['condicion']
    return ruc, estado, condicion

dni = input("Ingrese el número de DNI: ")
ruc = input("Ingrese el número de RUC: ")

try:
    nombre_completo, dni = consultar_dni(dni)
    print(f"Nombre completo: {nombre_completo}")
    print(f"DNI: {dni}")
except:
    print("No se pudo obtener información del DNI ingresado.")

try:
    ruc, estado, condicion = consultar_ruc(ruc)
    print(f"RUC: {ruc}")
    print(f"Estado: {estado}")
    print(f"Condicion: {condicion}")
except:
    print("No se pudo obtener información del RUC ingresado.")
