import os

# Crear un directorio anidado llamado "my_first_directory/my_second_directory"
os.makedirs("my_first_directory/my_second_directory")

# Cambiar el directorio actual a "my_first_directory"
os.chdir("my_first_directory")
print(os.getcwd())  # Imprimir la ruta actual

# Cambiar el directorio actual a "my_second_directory"
os.chdir("my_second_directory")
print(os.getcwd())  # Imprimir la ruta actual
