# Bash Script con Python.
# Script de automatizacion de tareas y uso simple de comandos shell.
# Corriendo bash scripts desde Python.
import subprocess
from alive_progress import alive_bar
import time

def listar_carpetas():
    result = subprocess.run(["ls", "-la"])
    print(result.stdout)

def crear_carpeta(nombre):
    result = subprocess.run(["mkdir", nombre])
    print(result.stdout)

def eliminar_carpeta(nombre):
    result = subprocess.run(["rm", "-r", nombre])
    print(result.stdout)

def crear_archivo(nombre):
    result = subprocess.run(["touch", nombre])
    print(result.stdout)

def eliminar_archivo(nombre):
    result = subprocess.run(["rm", nombre])
    print(result.stdout)

def mostrar_archivo(archivo):
    result = subprocess.run(["batcat", archivo])
    print(result.stdout)

def barra_progresiva():
    with alive_bar(100) as bar:
        for i in range(100):
            bar()
            time.sleep(0.01)
    print("Fin del programa")
    


lista_comandos = ["ls", "batcat", "mkdir", "rm -r", "touch", "rm", "exit"]
SEPARADOR = "=" * 50
SALTO_LINEA = "\n"
bienvenida = """Bash y Python
Este programa ejecuta comandos de sistema
Ingrese el comando que desea ejecutar"""
print(SEPARADOR)
print(bienvenida)
print(SEPARADOR)

while True:

    print("Comandos disponibles:")
    for comando in lista_comandos:
        print(f" - {comando}")

    opcion = input("Ingrese un comando: ")
    if opcion not in lista_comandos:
        print("Comando no válido")
        continue
    if opcion == "ls":
        listar_carpetas()
        print(SALTO_LINEA)
    elif opcion == "batcat":
        archivo = input("Ingrese el nombre del archivo: ")
        mostrar_archivo(archivo)
        print(SALTO_LINEA)
    elif opcion == "mkdir":
        nombre = input("Ingrese el nombre de la carpeta a crear: ")
        crear_carpeta(nombre)
        if True:
            print("Carpeta creada.")
            print(SALTO_LINEA)
    elif opcion == "rm -r":
        nombre = input("Ingrese el nombre de la carpeta a eliminar: ")
        eliminar_carpeta(nombre)
        if True:
            print("Carpeta eliminada.")
            print(SALTO_LINEA)
    elif opcion == "touch":
        nombre = input("Ingrese el nombre del archivo a crear: ")
        crear_archivo(nombre)
        if True:
            print("Archivo creado.")
            print(SALTO_LINEA)
    elif opcion == "rm":
        nombre = input("Ingrese el nombre del archivo a eliminar: ")
        eliminar_archivo(nombre)
        if True:
            print("Archivo eliminado.")
            print(SALTO_LINEA)
    elif opcion == "exit":
        print(SEPARADOR)
        print("Gracias por utilizar este programa")
        print(SEPARADOR)
        barra_progresiva()
        break
