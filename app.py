import losClientes
import losLibros
import os
import asyncio

clientes="clientes.txt"
libros= "libros.txt"

cliente=losClientes
libro= losLibros

def prestamoLibro(dni,isbn):

    if cliente.consultarEstado(dni) and libro.estadoLibro(isbn):

        elCliente=cliente.buscarCliente(dni)
        elCliente[4]="O"
        elClienteSinSplit=",".join(elCliente)
        
        elLibro= libro.buscarLibro(isbn)
        elLibro[3]="P"
        elLibroSinSplit=",".join(elLibro)

        elClienteSinSplit=elClienteSinSplit+","+elLibro[0]+"\n"
        elLibroSinSplit=elLibroSinSplit+","+elCliente[0]+"\n"

        print(elLibroSinSplit)
        print(elClienteSinSplit)
        with open(libros,"r") as rlosLibros:
            renglonesLibros=rlosLibros.readlines()
            for iterador,valor in enumerate(renglonesLibros):
                if isbn in valor:
                    renglonesLibros[iterador]=elLibroSinSplit

            rlosLibros.close()

            with open(libros,"w") as wLosLibros:
                wLosLibros.writelines(renglonesLibros)
                wLosLibros.close()
        
        with open(clientes,"r") as rLosClientes:
            renglonesClientes=rLosClientes.readlines()
            for iterador,valor in enumerate(renglonesClientes):
                if dni in valor:
                    renglonesClientes[iterador]=elClienteSinSplit

            rLosClientes.close()

            with open(clientes,"w") as wLosClientes:
                wLosClientes.writelines(renglonesClientes)
                wLosClientes.close()
        
        tituloYAutor=libro.mostrarLibroCliente(isbn)
        nombreCliente=cliente.mostrarClienteLibro(dni)
        print(f'''
        El libro:
        \"{tituloYAutor[0]}\n de \"{tituloYAutor[1]}
        ha sido prestado al cliente \"{nombreCliente}\" con éxito
        ''')
    else:
        print('''
        Error, el libro ya esta prestado o
        el cliente ya tiene un libro a su disposición
        Intente:
        -Devolver el libro seleccionado
        -Que el cliente seleccionado devuelva el libro que tiene
        -Intentar con otro libro o con otro cliente
        ''')

def devolucionLibro(dni,isbn):

    if cliente.consultarEstado(dni)==False and libro.estadoLibro(isbn)==False:
        
        elLibro= libro.buscarLibro(isbn)
        if elLibro[-1][:-1] == dni:
            
            del elLibro[-1]
            elLibro[-1]="D"
            elLibroSinSplit=",".join(elLibro)
            elLibroSinSplit=elLibroSinSplit+"\n"

            elCliente=cliente.buscarCliente(dni)
            del elCliente[-1]
            elCliente[-1]="D"
            elClienteSinSplit=",".join(elCliente)
            elClienteSinSplit=elClienteSinSplit+"\n"

            elLibro= libro.buscarLibro(isbn)
            del elLibro[-1]
            elLibro[-1]="D"
            elLibroSinSplit=",".join(elLibro)
            elLibroSinSplit=elLibroSinSplit+"\n"

            print(elClienteSinSplit)
            print(elLibroSinSplit)

            with open(libros,"r") as rlosLibros:
                renglonesLibros=rlosLibros.readlines()
                for iterador,valor in enumerate(renglonesLibros):
                    if isbn in valor:
                        renglonesLibros[iterador]=elLibroSinSplit

                rlosLibros.close()

                with open(libros,"w") as wLosLibros:
                    wLosLibros.writelines(renglonesLibros)
                    wLosLibros.close()
            
            with open(clientes,"r") as rLosClientes:
                renglonesClientes=rLosClientes.readlines()
                for iterador,valor in enumerate(renglonesClientes):
                    if dni in valor:
                        renglonesClientes[iterador]=elClienteSinSplit

                rLosClientes.close()

                with open(clientes,"w") as wLosClientes:
                    wLosClientes.writelines(renglonesClientes)
                    wLosClientes.close()

            busquedaCliente=cliente.buscarCliente(dni)
            nombreCliente=busquedaCliente[1]
            busquedaLibro=libro.buscarLibro(isbn)
            tituloYAutor=busquedaLibro[1],busquedaLibro[2]
            print(f'''
            El cliente \"{nombreCliente}\" ha hecho la devolución del libro:
            \"{tituloYAutor[0]}\" de \"{tituloYAutor[1]}\"
            con éxito 
            ''')
        else:
            print("Error, no se puede devolver el libro porque esta a nombre de otro cliente")

        
    else:
        print('''
        Error, el cliente seleccionado o el libro seleccionado estan disponibles
        No hace falta una devolución
        Intente:
        -Seleccionar otro libro
        -Seleccionar otro cliente
        ''')

async def creditos():
    print("Este trabajo fue hecho por:")
    await asyncio.sleep(2)
    print("Mauro Bernardi")
    
    await asyncio.sleep(3)
    print("Kevin Aviles Bejarano")
    await asyncio.sleep(2)
    print("---------------------------------------")
    print("Apruébenos")
def limpioPantalla():
	sisOper = os.name
	if sisOper == "posix":   # si fuera UNIX, mac para Apple, java para maquina virtual Java
		os.system("clear")
	elif sisOper == "ce" or sisOper == "nt" or sisOper == "dos":  # windows
		os.system("cls")

#----------------------------------------Menu General---------------------------------
def mostrarMenu():
    print("****************** Biblioteca Grupo 1 *******************")
    print("****************** Menú Principal ***********************")
    print('''
    1 - Consulta de disponibilidad(todos los libros)
    2 - Prestamo de un libro
    3 - Gestión del cliente
    4 - Gestión del libro
    5 - Limpiar Pantalla
    6 - Creditos
    7 - Salir
    ''')

def elejirOpcionPorConsola():   #Metodo para que se elija una opcion en la consola sin que se corte el programa
    while True:
        try:
            opcion = int(input("Elija la opción deseada: ")) 
        except ValueError:
            print("Error debe de elejir un número")
        else:
            break
    return opcion

def ejecutarMenu():     #Inicia el menu principal
    opc=0
    while opc != 7:
        mostrarMenu()
        opcion = elejirOpcionPorConsola()
        if opcion == 1:
            libro.librosDisponibles()
        elif opcion == 2:
            opc=7
            limpioPantalla()
            ejecutarMenuPrestamo()
        elif opcion == 3:
            opc=7
            limpioPantalla()
            ejecutarMenuClientes()
        elif opcion == 4:
            opc=7
            limpioPantalla()
            ejecutarMenuLibros()
            
        elif opcion == 5:
            limpioPantalla()
        elif opcion == 6:
            limpioPantalla()
            asyncio.run(creditos())
        else:
            opc=opcion

def mostrarPrestamoLibroSubMenu():
    print("****************** Préstamo de Libro Menú *******************")
    print('''
    1 - Consultar si un libro esa disponible
    2 - Registrar préstamo de un libro
    3 - Registrar devolución de un libro
    4 - Atras
    ''')

def ejecutarMenuPrestamo():
    opc = 0
    while opc !=10:
        mostrarPrestamoLibroSubMenu()
        opcion = elejirOpcionPorConsola()
        if opcion == 1:
            codigoLibro=libro.preguntarSiElLibroExistePorConsola()
            datosLibro=libro.buscarLibro(codigoLibro)
            if libro.estadoLibro(codigoLibro):
                print(f"El libro con el titulo {datosLibro[1]} de {datosLibro[2]} esta disponible para un prestamo")
            else:
                print(f"El libro con el titulo {datosLibro[1]} de {datosLibro[2]} no esta disponible para un prestamo ")
        elif opcion == 2:
            elDni=cliente.consultaSiClienteExisteConsola()
            elIsbn=libro.preguntarSiElLibroExistePorConsola()
            prestamoLibro(elDni,elIsbn)
            
        elif opcion == 3:
            elDni=cliente.consultaSiClienteExisteConsola()
            elIsbn=libro.preguntarSiElLibroExistePorConsola()
            devolucionLibro(elDni,elIsbn)
            
        elif opcion == 4:
            opc=10
            limpioPantalla()
            ejecutarMenu()
        else:
            opc=opcion

def mostrarMenuClientes():
    #await asyncio.sleep(3)
    print("****************** Gestión del cliente *******************")
    print('''
    1 - Alta de cliente
    2 - Consultar estado del cliente
    3 - Modificar teléfono o dirección del cliente
    4 - Eliminar cliente
    5 - Atras
    ''')

def ejecutarMenuClientes():     #Ejecuta el menu de clientes al elejir la opcion 3 en el menu principal
   
    opc = 0
    while opc != 10:
        mostrarMenuClientes()
        opcion = elejirOpcionPorConsola()
        if opcion == 1:
            print("Alta cliente")
            dni = cliente.agregarDni()
            nombreCompleto = cliente.agregarNombreCompleto()
            telefono = cliente.agregarTelefono()
            direccion = cliente.agregarDireccion()
            cliente.altaCliente(dni,nombreCompleto,telefono,direccion)
            print(f"\nPerfecto el cliente con nombre: {nombreCompleto} ya se encuentra en nuesta base de datos\n")
        elif opcion == 2:
            print("Conusulta del Cliente")
            dniCliente = cliente.consultaSiClienteExisteConsola()
            if cliente.consultarEstado(dniCliente):
                print(f"\nEl cliente con dni: {dniCliente} esta disponible para pedir un libro\n")
            else:
                renglon=cliente.buscarCliente(dniCliente)
                isbnCliente=renglon[5][:-1]
                tituloYAutor=libro.mostrarLibroCliente(isbnCliente)
                print(f"\nEl cliente con dni: {dniCliente} ya tiene un producto a su disposición y es \"{tituloYAutor[0]}\" de \"{tituloYAutor[1]}\"\n")
        elif opcion == 3:
            opc = 10
            limpioPantalla()
            ejecutarSubMenuClientes()
            
        elif opcion == 4:
            dniCliente = cliente.consultaSiClienteExisteConsola()
            cliente.eliminarCliente(dniCliente)
        elif opcion == 5:
            opc = 10
            limpioPantalla()
            ejecutarMenu()
        else: 
            opc=opcion


def mostrarSubMenuClientes():
    #await asyncio.sleep(3)
    print("****************** Gestión del cliente Teléfono y Dirección *******************")
    print('''
    1 - Modificar Teléfono
    2 - Modificar Direccién
    3 - Atras
    ''')
def ejecutarSubMenuClientes():     #Ejecuta el subMenu del cliente si en el menu del cliente este presiono la opcion 3
    subOpc = 0
    while subOpc != 10:
        mostrarSubMenuClientes()
        opcion = elejirOpcionPorConsola()
        if opcion == 1:
            print ("Modificar Teléfono")
            dniCliente = cliente.consultaSiClienteExisteConsola()
            telefono = cliente.agregarTelefono()
            #modificarTelefono(dniCliente,telefono)
            cliente.modificarTelefonoOrDireccion(dniCliente,telefono,"")
            print("El teléfono del cliente a sido cambiado con éxito")
        elif opcion == 2:
            print("Modificar Dirección")
            dniCliente = cliente.consultaSiClienteExisteConsola()
            direccion = cliente.agregarDireccion()
            #modificarDireccion(dniCliente,direccion)
            cliente.modificarTelefonoOrDireccion(dniCliente,"",direccion)
            print("La dirección del cliente a sido cambiada con éxito")
        elif opcion == 3:
            subOpc = 10
            limpioPantalla()
            ejecutarMenuClientes()
        else:
            subOpc = opcion


def mostrarMenuLibro():
    print("****************** Gestión de libros *******************")
    print('''
    1 - Alta de libro
    2 - Consultar  libro
    3 - Modificar titulo o autor del libro
    4 - Eliminar libro
    5 - Atras
    ''')
def ejecutarMenuLibros():
    opc=0
    while opc !=10:
        mostrarMenuLibro()
        opcion=elejirOpcionPorConsola()
        if opcion == 1:
            print("Alta Libro")
            libro.altaLibro(libro.agregarIsbn(),libro.agregarTitulo(),libro.agregarAutor())
        elif opcion ==2:
            print("Consulta Libro")
            codigoLibro=libro.preguntarSiElLibroExistePorConsola()
            libro.mostrarLibro(codigoLibro) #A BUSCAR
        elif opcion == 3:
            print("Modificar titulo o autor")
            opc=10
            limpioPantalla()
            ejecutarSubMenuLibro()
        elif opcion == 4:
            print("Eliminar libro")
            isbn=libro.preguntarSiElLibroExistePorConsola()
            libro.eliminarLibro(isbn)
        elif opcion == 5:
            opc=10
            limpioPantalla()
            ejecutarMenu()
        else:
            opc=opcion

def mostrarSubMenuLibro():
    print("****************** Gestión del libro Titulo y Autor *******************")
    print('''
    1 - Modificar Titulo 
    2 - Modificar Autor
    3 - Atras
    ''')

def ejecutarSubMenuLibro():
    subOpc=0
    while subOpc !=10:
        mostrarSubMenuLibro()
        opcion= elejirOpcionPorConsola()
        if opcion == 1:
            print("Modificar Tituto")
            isbn=libro.preguntarSiElLibroExistePorConsola()
            titulo=libro.agregarTitulo()
            libro.modificarTituloORAutor(isbn,titulo,"")
            print(f"El libro con el isbn {isbn} ya tiene el titulo modificado")
        elif opcion == 2:
            print("Modificar Autor")
            isbn=libro.preguntarSiElLibroExistePorConsola()
            autor=libro.agregarAutor()
            libro.modificarTituloORAutor(isbn,"",autor)
            print(f"El libro con el isbn {isbn} ya tiene el autor modificado")
        elif opcion == 3:
            subOpc=10
            limpioPantalla()
            ejecutarMenuLibros()
        else:
            subOpc=opcion
#---------------------------Ejecucion de la APP---------------------
ejecutarMenu()