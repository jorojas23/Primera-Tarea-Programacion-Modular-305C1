from archivo import Archivo
from repositorio import Repositorio

def main():
    # Crear repositorio
    repo = Repositorio()

    # Crear archivos
    a1 = Archivo("hola.txt", "Hola Mundo")
    a2 = Archivo("foo.txt", "Foo")

    # Commit inicial en main
    repo.nuevo_com([a1], "Primer commit")

    # Nueva rama y cambio de rama a 'mcQueen'
    repo.nueva_rama("mcQueen")
    repo.cambiar_rama("mcQueen")

    # Commit en la rama mcQueen
    a3 = Archivo("hola_universo.txt", "Hola Universo")
    repo.nuevo_com([a3, a2], "agregar hola_universo y agregar foo")

    # Volver a main y hacer merge
    repo.cambiar_rama("main")
    repo.merge("mcQueen")
    

    print(repo) 

if __name__ == "__main__":
    main()
