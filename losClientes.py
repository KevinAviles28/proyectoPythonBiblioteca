clientes="clientes.txt"
libros= "libros.txt"

#------------------Cliente----------------------------------
def altaCliente(dni,nombreCompleto,telefono,direccion):   #Crea un nuevo cliente en el archivo "clientes.txt"
    with open(clientes,"a") as aDatosClientes:
        aDatosClientes.write(dni+","+nombreCompleto+","+telefono+","+direccion+","+"D"+""+"\n")
        aDatosClientes.close()

def buscarCliente(dni):     #Busca al cliente por el dni y retorna todos su daton como un array
    with open(clientes, "r") as rDatosClientes:
        for dato in rDatosClientes:
            renglon = dato.split(',')       #convierte la linea de string en un array separado por ","
            if dni in renglon[0]: 
                return renglon
        rDatosClientes.close()


def modificarTelefonoOrDireccion(dni,nuevoTelefono,nuevaDireccion): #Modifica el telefono o la direccion, dependiendo el parametro que no este vacio
    elRenglon= buscarCliente(dni)
    valor = 0
    if nuevoTelefono=="": #Si el parametro de "nuevoTelefono" esta vacio se modificara la direccion
        valor = 3
        elRenglon[valor]=nuevaDireccion
    else:                   #Si no se modificara el telefono
        valor = 2
        elRenglon[valor]=nuevoTelefono

    elRenglon=",".join(elRenglon)
    
    with open(clientes,"r") as DatosCliente:
        renglones=DatosCliente.readlines()
        for iterador,valor in enumerate(renglones):
            if dni in valor:
                renglones[iterador]=elRenglon
        DatosCliente.close()

        with open(clientes,"w") as wDatosClientes:
            wDatosClientes.writelines(renglones)
            wDatosClientes.close()


def consultarEstado(dni): #Busca al cliente por el dni, si el cliente tiene un "D" de disponible retorna True
    elRenglon=buscarCliente(dni)
    if elRenglon[4][:-1] == "D":
        return True
    else:
        return False

def mostrarClienteLibro(dni):
    renglon=buscarCliente(dni)
    nombre=renglon[1]
    return nombre

def eliminarCliente(dni):   #Elimina al cliente siempre y cuando no tenga un libro a su disposicion
    if consultarEstado(dni):
        with open(clientes,"r") as rClientes:
            lineas=rClientes.readlines()
            with open(clientes,"w") as wClientes:
                for renglon in lineas:
                    if dni not in renglon.split(","):
                        wClientes.write(renglon)
                rClientes.close()
                wClientes.close()
        print("El cliente a sido eliminado con exito")
    else:
        print("Error, el cliente no se puede dar de baja porque todavia tiene un producto sin devolver")


def consultaSiClienteExisteConsola():  #Metodo para preguntar por consola el dni del cliente, verifica si el cliente esta en la base de datos etc
    while True:                        #Al final retorna el dni del cliente
        try:
            dniCliente= str(input("Ingrese el dni del cliente a buscar: "))
        except ValueError:
            print("Error, debe de ingresar un nombre valido")
        else:
            resultado=buscarCliente(dniCliente)
            if len(dniCliente) != 8:
                print("Error, el numero de DNI solo tiene que tener 8 campos")
            elif dniCliente.isalpha():
                print("Error, el DNI solo tiene que contener números") 
            elif resultado is None:
                print(f"Error, el DNI: {dniCliente} no se encuentra en la base de datos")
            else: 
                break
    return dniCliente

def agregarDni():   #Agrega el DNI por consola, no le deja agregarlo si el dni ya esta en el archivo de texto
    while True:      
        try:
            dni=str(input("Ingrese su DNI: "))
        except ValueError:
            print("Error, el DNI solo contiene numeros")
        else:
            resultado=buscarCliente(dni) 
            if len(dni) != 8:
                print("Error, el número de DNI sono tiene 8 campos")
            elif dni.isalpha():
                print("Error, el DNI solo tiene que contener números")
            elif resultado != None:
                print(f"Error, el DNI {dni} ya se encuentra en la base de datos, intente nuevamente" )
            else: 
                break
                
    return dni      #Retorna el DNI

def agregarNombreCompleto():    #Agrega el nombre Completo, cada ves que inicia una palabra esta comenzara con mayuscula
    while True:
        try:
            nombreCompleto= str(input("Ingrese su nombre completo: ")).title()
        except ValueError:
            print("Error debe de ingresar un nombre y un apellido valido")
        else:
            break
    return nombreCompleto   #Retorna el nombre completo

def agregarTelefono():  #Agregar el telefono del cliente
    while True:
        try:
            telefonoCliente=str(input("Ingrese un teléfono: "))
        except ValueError:
            print("Error, el teléfono solo tiene que contener números")
        else:
            if telefonoCliente.isalpha():
                print("Error, el teléfono solo tiene que contener números")
            else:
                break
    return telefonoCliente  #Retorna el telefono

def agregarDireccion(): #Agrega la direccion del Cliente
    while True:
        try:
            direccionCliente= str(input("Ingrese una dirección: ")).title()
        except ValueError:
            print("Error la dirección es errónea")
        else:
            break
    return direccionCliente #Retorna la direccion 