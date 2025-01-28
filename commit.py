import uuid
import datetime

class Commit:
    def __init__(self, archivos, mensaje, commit_ant):
        """
        Inicializa un objeto Commit.

        Los argumentos son:
            archivos (list[Archivo]): Una lista de objetos Archivo.
            mensaje (str): El mensaje del commit.
            commit_ant (Commit, opcional): El commit anterior.
        """
        self.id = uuid.uuid4()  # se genera un id unico con el uuid
        self.archivos = archivos
        self.mensaje = mensaje
        self.commit_ant = commit_ant
        self.fecha = datetime.datetime.now()  # obtenemos la fecha de creacion

    def __str__(self):
        #Devuelve una cadena con la información del commit.
        archivos_str = "\n".join(str(archivo) for archivo in self.archivos)
        return f"\t\tCommit ID: {self.id}\n\t\tFecha: {self.fecha}\n\t\tMensaje: {self.mensaje}\n\t\tArchivos: {archivos_str}\n\t\tCommit Anterior ID: {self.commit_ant.id if self.commit_ant else None}"
