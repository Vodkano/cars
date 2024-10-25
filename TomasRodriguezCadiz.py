import re
from datetime import datetime

vehiculos = {}
registros = {}  

def validar_patente(patente):
    fpatente = r'[A-Za-z]{2}\d{4}$| [A-Za-z]{4}\d{2}$' 
    return re.fullmatch(fpatente, patente)

def registrar_vehiculo():
    auto = {}
    while True:
        patente = input(" Ingrese la patente (AA1000 o BBBB10): ")
        if validar_patente(patente):
            if patente in vehiculos:
                print(" Error La patente ya está registrada.")
            else:
                auto['patente'] = patente
                break
        else:
            print(" Error Patente no válida. Formato correcto: AA1000 o BBBB10.")
    while True:
        auto['marca'] = input("Marca\n: ")
        if auto['marca']:
            break
        else:
            print(" error La marca no puede estar vacía ")
    while True:
        try:
            auto['año'] = int(input(" Año de fabricación (1900 - 2021): "))
            if 1900 <= auto['año'] <= 2021:
                break
            else:
                print(" Error: El año debe estar entre 1900 y 2021.")
        except ValueError:
            print("Error: Debes ingresar un número entero para el año.")
    while True:
        auto['modelo'] = input("Modelo: ")
        if auto['modelo']:
            break
        else:
            print("Error El modelo no puede estar vacío")
    while True:
        tipo_vehiculo = input(" Tipo de vehículo (b/d/e/h): ").lower()
        if tipo_vehiculo in ['b', 'd', 'e', 'h']:
            auto['tipo_vehiculo'] = tipo_vehiculo
            break
        else:
            print(" Error El tipo de vehículo debe ser b, d, e o h ")
    vehiculos[patente] = auto
    registros[patente] = []
    print(" Automóvil registrado exitosamente.")

def agregar_registro():
    patente = input("Ingrese la patente del vehículo: ")    
    if patente not in vehiculos:
        print("Error: Vehículo no registrado en el sistema.")
        return
    while True:
        fecha = input("Ingrese la fecha (DD-MM-YYYY): ")
        try:
            fecha_obj = datetime.strptime(fecha, "%d-%m-%Y")
            break
        except ValueError:
            print("Error: Fecha no válida. Formato correcto: DD-MM-YYYY.")
    observaciones = input("Ingrese las observaciones: ")
    nuevo_registro = {
        "fecha": fecha,
        "observaciones": observaciones
    }
    registros[patente].append(nuevo_registro)
    
    print("Registro de mantenimiento agregado exitosamente.")

def consultar_vehiculo():
    patente = input("Ingrese la patente del vehículo a consultar: ")
    if patente not in vehiculos:
        print("Error: Vehículo no registrado en el sistema.")
        return
    auto = vehiculos[patente]
    print(f"""
          Patente: {auto['patente']}
         Marca: {auto['marca']}
         Modelo: {auto['modelo']}
         Año de fabricación: {auto['año']}
        Tipo de vehículo: {auto['tipo_vehiculo']}""")
    if registros[patente]:
        print( "\n--- Registros de Mantenimiento ---")
        for reg in registros[patente]:
            print(f"Fecha: {reg['fecha']}\nObservaciones: {reg['observaciones']}\n")
    else:
        print(" No hay registros de mantenimiento para este vehículo.")
def menu():
    while True:
        print("""
             ServiExpress")
        [1] Registrar automóvil")
        [2] Registro Mantenimiento")
        [3] Consultar Automóvil")
        [4]. Salir""")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            registrar_vehiculo()
        elif opcion == '2':
            agregar_registro()
        elif opcion == '3':
            consultar_vehiculo()
        elif opcion == '4':
            print("""Cerrando sesión.
                  by tomas""")
            break
        else:
            print(" Error Intente nuevamente.")


menu()
