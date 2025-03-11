"""
Programa para gestionar una lista de invitados a una fiesta.
Se almacena la informacion en un archivo de texto y se incluyen detalles adicionales por cada invitado.
"""

import os

# Ruta del archivo donde se guardaran los datos
RUTA_ARCHIVO = "C:/Quinto/archivo.txt"

def agregar_invitado():
    """Funcion para agregar un nuevo invitado a la lista."""
    nombre = input("Ingrese el nombre del invitado: ")
    cuota = 100.00  # Cuota fija por invitado
    automovil = input("Llevara automovil? (si/no): ").strip().lower()
    pago = input("Forma de pago (tarjeta/efectivo): ").strip().lower()
    ubicacion = input("Ingrese la ubicacion del invitado: ")

    # Guardar los datos en el archivo
    with open(RUTA_ARCHIVO, "a") as archivo:
        archivo.write(f"{nombre},{cuota},{automovil},{pago},{ubicacion}\n")

    print("Invitado agregado correctamente.")

def contar_invitados():
    """Funcion para contar el numero total de invitados registrados."""
    if not os.path.exists(RUTA_ARCHIVO):
        return 0
    
    with open(RUTA_ARCHIVO, "r") as archivo:
        return sum(1 for _ in archivo)

def calcular_total_cuotas():
    """Funcion para calcular el total de cuotas de los invitados."""
    total = contar_invitados() * 100
    return total

def listar_invitados():
    """Funcion para mostrar la lista de invitados registrados."""
    if not os.path.exists(RUTA_ARCHIVO):
        print("No hay invitados registrados.")
        return

    with open(RUTA_ARCHIVO, "r") as archivo:
        print("Lista de invitados:")
        for linea in archivo:
            datos = linea.strip().split(",")
            print(f"Nombre: {datos[0]}, Automovil: {datos[2]}, Pago: {datos[3]}, Ubicacion: {datos[4]}")

def menu():
    """Funcion principal que muestra el menu de opciones."""
    while True:
        print("\n--- Menu ---")
        print("1. Agregar invitado")
        print("2. Contar invitados")
        print("3. Calcular total de cuotas")
        print("4. Listar invitados")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_invitado()
        elif opcion == "2":
            print(f"Total de invitados: {contar_invitados()}")
        elif opcion == "3":
            print(f"Total de cuotas: Q{calcular_total_cuotas():.2f}")
        elif opcion == "4":
            listar_invitados()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida, intente de nuevo.")

# Ejecutar el menu principal
if __name__ == "__main__":
    menu()
