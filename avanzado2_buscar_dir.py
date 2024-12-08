# Importar el módulo os para trabajar con archivos y directorios
import os

# Definir la función find que toma dos argumentos: path y dir
def find(path, dir):
    # Convertir la ruta a una ruta absoluta
    path = os.path.abspath(path)
    # Comprobar si la ruta existe y es un directorio
    if os.path.exists(path) and os.path.isdir(path):
        # Recorrer todos los archivos y subdirectorios en la ruta
        for file in os.listdir(path):
            # Obtener la ruta completa del archivo o subdirectorio
            file_path = os.path.join(path, file)
            # Si el nombre del archivo o subdirectorio coincide con el argumento dir, imprimir la ruta absoluta
            if file == dir:
                print(file_path)
            # Si el archivo o subdirectorio es un directorio, llamar a la función find de forma recursiva con la nueva ruta y el mismo argumento dir
            elif os.path.isdir(file_path):
                find(file_path, dir)
    # Si la ruta no existe o no es un directorio, mostrar un mensaje de error
    else:
        print("La ruta no es válida o no es un directorio.")

# Pedir al usuario el argumento path
path = input("Introduce la ruta donde comenzar la búsqueda: ")
# Pedir al usuario el argumento dir
dir = input("Introduce el nombre del directorio que quieres encontrar: ")
# Llamar a la función find con los argumentos introducidos por el usuario
find(path, dir)
