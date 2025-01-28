class Rama:
    def __init__(self, nombre, commit_act=None):
        """
        Inicializa un objeto Rama.

        Los arguentos son:
            nombre (str): El nombre de la rama.
            commit_act (Commit, opcional): El commit actual de la rama o el valor None.
            """
        self.nombre = nombre
        self.commit_act = commit_act

    def act_commit(self, commit):
        """
        Actualiza el commit actual de la rama.

        los argumentos son:
            commit (Commit): El nuevo commit actual.
        """
        self.commit_act = commit

    def __str__(self):
        #Devuelve una cadena con el nombre de la rama y la información del commit actual.
        return f"Rama: {self.nombre}\n\tCommit Actual:\n{self.commit_act if self.commit_act else 'Ninguno'}"
