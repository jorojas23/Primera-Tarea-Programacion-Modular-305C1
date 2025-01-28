class Archivo:
    def __init__(self, nombre, contenido):
        """
        Constructor de la clase Archivo.

        Los argumentos que llegan son:
            nombre (str): El nombre del archivo.
            contenido (str): El contenido del archivo.

        """
        # ve si el nombre esta vacio o con espacios
        if not nombre.strip():
            # si se cumple la condicion lanza este error personalizado
            raise ValueError("El nombre del archivo no puede estar vacío.")

        # se define los valores del objeto 
        self.nombre = nombre
        self.contenido = contenido

    def __str__(self):
        
        # Devuelve una cadena con el nombre y el contenido del archivo.
        
        return f"\n\t\t\tArchivo: {self.nombre}\n\t\t\tContenido:{self.contenido}"
