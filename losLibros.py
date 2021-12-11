#campos: ISBN, Titulo, Autor, estado, DNI del cliente (solo cuando el libro esté en préstamo)
clientes="clientes.txt"
libros= "libros.txt"

#------------------Libros----------------------------------
def altaLibro(isbn,titulo,autor): 
    with open(libros,"a") as aLibros:
        aLibros.write(isbn+","+titulo+","+autor+","+"D"+""+"\n")
        aLibros.close()
    
        print(f"***************** Libro {titulo} agregado ***************")
        print("{4}{0:^6}{4} {4}{1:^30}{4} {4}{2:^25}{4} {4}{3:^8}{4}".format("ISBM","Titulo", "Autor","Estado", "|"))
        print("{4}{0:^6}{4} {4}{1:30s}{4} {4}{2:25s}{4} {4}{3:^8}{4}".format(isbn,titulo,autor,"Disponible","|"))
        print("----------------------------------------------------------")

def buscarLibro(isbn):  # Consultar Libro
    with open("libros.txt","r") as rLibros:
        for linea in rLibros:
            renglon=linea.split(',')
            if isbn in renglon[0]:
                #print(renglon)
                return renglon
        rLibros.close()

def cambiarLetras(isbn):
    renglon=buscarLibro(isbn)
    if renglon[3][:-1]=="D":
        renglon[3]="Disponible"
    else:
        renglon[3]="Prestado"
    return renglon


def mostrarLibro(isbn):
    renglon=cambiarLetras(isbn)
    print(f"***************** Libro {renglon[1]} datos ***************")
    print("{4}{0:^6}{4} {4}{1:^30}{4} {4}{2:^25}{4} {4}{3:^12}{4}".format("ISBM","Titulo", "Autor","Estado", "|"))
    print("{4}{0:^6}{4} {4}{1:30s}{4} {4}{2:25s}{4} {4}{3:^12}{4}".format(renglon[0],renglon[1],renglon[2],renglon[3],"|"))

def mostrarLibroCliente(isbn):
    renglon=buscarLibro(isbn)
    tituloYAutor=renglon[1],renglon[2]
    return tituloYAutor

def modificarTituloORAutor(isbn,nuevoTitulo,nuevoAutor):
    elRenglon = buscarLibro(isbn)
    valor = 0 

    if nuevoTitulo == "":
        valor = 2
        elRenglon[valor] = nuevoAutor
    else:
        valor = 1
        elRenglon[valor] = nuevoTitulo

    elRenglon= ",".join(elRenglon)

    with open(libros,"r") as rModificacionLibros:
        renglones= rModificacionLibros.readlines()
        for iterador,valor in enumerate(renglones):
            if isbn in valor:
                renglones[iterador] =elRenglon  

        rModificacionLibros.close()

    with open(libros,"w") as wModificarLibros:
        wModificarLibros.writelines(renglones)
        wModificarLibros.close()

def estadoLibro(isbn):
    renglon= buscarLibro(isbn)
    if renglon[3][:-1]=="D":
        return True
    else:
        return False

def eliminarLibro(isbn):
    if estadoLibro(isbn):

        with open(libros,"r") as rEliminarLibros:
            lineas = rEliminarLibros.readlines()
            with open(libros,"w") as wEliminarLibros:
                for renglon in lineas:
                    if isbn not in renglon.split(','):
                        wEliminarLibros.write(renglon)

                rEliminarLibros.close()
                wEliminarLibros.close()
        print("El libro a sido eliminado con exito")
    else:
        print("Error, el libro no puede ser eliminado ya que esta en prestamo")


def preguntarSiElLibroExistePorConsola():
    while True:
        try:
            elIsbn=str(input("Ingrese el isbn del libro: "))
        except ValueError:
            print("Error, debe de ingresar un isbn valido")
        else:
            resultado = buscarLibro(elIsbn)

            if len(elIsbn) != 3:
                print("Error, el isbn solo contiene 3 digitos")
            elif elIsbn.isalpha():
                print("Error, el isbn solo contiene números")
            elif resultado is None:
                print(f"Error el isbn que ingreso \"{elIsbn}\" no se encuentra en la base de datos")
            else:
                break
    return elIsbn

def agregarIsbn():
    while True:
        try:
            isbn=str(input("Ingrese el ISBN del nuevo libro: "))
        except ValueError:
            print("Error, debe de ingresar un ISBN valido")
        else:
            resultado= buscarLibro(isbn)

            if len(isbn) != 3:
                print("Error, el ISBN solo contiene 3 digitos")
            elif isbn.isalpha():
                print("Error, el ISBN solo contiene números")
            elif resultado != None:
                print(f"Error el ISBN \"{isbn}\" ya esta en la base de datos intente con otro ISBN")
            else:
                break
    return isbn
def agregarTitulo():
    while True:
        try:
            tituloLibro= str(input("Ingrese el titulo para el libro: ")).title()
        except ValueError:
            print("Error debe de ingresar un titulo valido")
        else:
            break
    return tituloLibro

def agregarAutor():
    while True:
        try:
            autorLibro= str(input("Ingrese el nombre del autor para el libro: ")).title()
        except ValueError:
            print("Erro debe de ingresar un nombre de autor valido")
        else:
            if not autorLibro.isalpha:
                print("Error el nombre del autor solo debe contener letras")
            else:
                break
    return autorLibro


#def consultaDisponibilidad(isbn): supuestamente esto es lo mismo que buscarLibro(isbm)

def librosDisponibles():
    with open(libros, "r") as rLibros:
        print("***************** Libros Diponibles ***************")
        print("{4}{0:^6}{4} {4}{1:^30}{4} {4}{2:^25}{4} {4}{3:^12}{4}".format("ISBM","Titulo", "Autor","Estado", "|"))
        for linea in rLibros:
            renglon=linea.split(',')
            if renglon[3][:-1]=="D":
                print("{4}{0:^6}{4} {4}{1:30s}{4} {4}{2:25s}{4} {4}{3:^12}{4}".format(renglon[0], renglon[1], renglon[2], "Disponible", "|"))
        print("------------------------------------------------------------")
        rLibros.close()