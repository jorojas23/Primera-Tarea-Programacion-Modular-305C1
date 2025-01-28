from rama import Rama
from commit import Commit

class Repositorio:
    def __init__(self):
        """
        Inicializa un Repositorio.

        Crea la rama 'main' y establece el puntero a 'main'.
        """
        self.ramas = {"main": Rama("main")}  # Diccionario para almacenar las ramas,siendo 'main' la rama principal.
        self.puntero = "main"  # Puntero a la rama actual, iniciando en 'main'.

    def nueva_rama(self, nombre):
        """
        Crea una nueva rama.

        Los argumentos son:
            nombre (str): El nombre de la nueva rama.
        """
        if nombre not in self.ramas:
            rama_actual = self.ramas[self.puntero]  # Obtiene la rama actual a partir del puntero
            #se crea la nueva rama siguiendo con el commit actual de la rama anterior
            self.ramas[nombre] = Rama(nombre, rama_actual.commit_act)
        else:
            raise ValueError("La rama ya existe")#lanza error si la rama ya existe

    def nuevo_com(self, lista_archivos, mensaje):
        """
        Crea un nuevo commit en la rama actual.

        Los argumentos son:
            lista_archivos (list[Archivo]): Lista de objetos Archivo para el commit.
            mensaje (str): El mensaje del commit.
        """
        rama_actual = self.ramas[self.puntero]  # se guarda la rama actual
        nuevo_commit = Commit(lista_archivos, mensaje, rama_actual.commit_act)  # se crea un nuevo commit.
        rama_actual.act_commit(nuevo_commit)  # actualizamos el commit actual de la rama con el nuevo commit

    def cambiar_rama(self, nombre):
        """
        Cambia la rama actual (a la que apunta el puntero).

        Los argumentos son:
            nombre (str): El nombre de la rama a la que cambiar.

        """
        if nombre in self.ramas:
            self.puntero = nombre  # Mueve el puntero a la nueva rama.
        else:
            raise ValueError("La rama no existe") #regresa un error si la rama no existe
        
    def merge(self, nombre):
        #verifica si la rama existe, el nombre no es el mismo del puntero y si no es main
        if nombre not in self.ramas or nombre == self.puntero or nombre == "main":
            raise ValueError("Operación inválida") #lanza error "operacion invalida" si no cumple las condiciones 
            return

        # Obtener commits actuales da las ramas que se van a funcionar
        commit_r = self.ramas[nombre].commit_act
        commit_r_act = self.ramas[self.puntero].commit_act

        band = False #indica si se cierra el ciclo o no
        pos = 0 #indica las cantdad de vueltas del ciclo

        while not band:
            # verifica si el commit de la rama(apuntada) es None
            if commit_r_act is None:
                # verifica si el commit de la rama a funcionar es None
                if commit_r is None:
                    raise ValueError("no hay ancestro comun") #lanza error si no hay un ancestro en comun
                    break
                #si no se cumple la condicion anterior 
                commit_r = commit_r.commit_ant #se retrocede a un commit anterior en la rama a funcionar 
                commit_r_act = self.ramas[self.puntero].commit_act #se regresa al commit actual de la rama(apuntada)
                
                

            # Compara los id de los commit para ver si los commit de las ramas son el ancestro
            if str(commit_r.id) == str(commit_r_act.id):
                
                if pos <= 1 : #pasa por aqui si no se creo un nuevo commit en la rama apuntada
                    self.ramas[self.puntero].act_commit(self.ramas[nombre].commit_act)
                else: 
                    # se combinan los archivos
                    lista_merge = self.ramas[self.puntero].commit_act.archivos.copy() #copia de el commit de la rama(apuntada)
                    for archivo in self.ramas[nombre].commit_act.archivos + commit_r.archivos:
                        """
                            se recorre la lista de archivos del commit actual de la rama a
                            funcionar unida al del commit ancestro
                        """
                        if archivo not in lista_merge or archivo is lista_merge: 
                            lista_merge.append(archivo) #se agrega un archivo si este no esta en la lista merge
                    self.nuevo_com(lista_merge, "merge")
                band = True

            else:
                commit_r_act = commit_r_act.commit_ant  #se retrocede a un commit anterior 
                pos += 1
        

    def __str__(self):
        
        ramas_str = "\n".join(str(rama) for rama in self.ramas.values())  # Formatea la información de cada rama.
        return f"---------------------------------------------------\nRepositorio:\n{ramas_str}"  # Devuelve la representación del repositorio.
