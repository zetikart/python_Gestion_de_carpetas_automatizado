import os  # Importa el módulo 'os' que permite interactuar con el sistema operativo.

class DirectorySearcher:  # Define una clase llamada 'DirectorySearcher'.
    def find(self, path, dir):  # Define un método 'find' dentro de la clase, que toma 'path' y 'dir' como parámetros.
        try:
            os.chdir(path)  # Intenta cambiar el directorio de trabajo al especificado por 'path'.
        except OSError:
            # Si 'path' no es un directorio válido, captura la excepción 'OSError' y sale del método.
            return

        current_dir = os.getcwd()  # Guarda la ruta del directorio actual en 'current_dir'.
        for entry in os.listdir("."):  # Itera sobre cada entrada en el directorio actual.
            if entry == dir:  # Si la entrada es igual al nombre del directorio buscado 'dir', ejecuta el siguiente bloque.
                print(os.getcwd() + "/" + dir)  # Imprime la ruta completa del directorio encontrado.
            self.find(current_dir + "/" + entry, dir)  # Llama al método 'find' recursivamente para buscar en subdirectorios.

directory_searchv3er = DirectorySearcher()  # Crea una instancia de la clase 'DirectorySearcher'.
directory_searchv3er.find("./tree", "python")  # Llama al método 'find' con la ruta inicial './tree' y busca un directorio llamado 'python'.
