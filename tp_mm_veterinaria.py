from datetime import datetime

clientesMatris = [] # lista de clientes
clientesMatris.append(["Marcelo", "Maffei", "30087647", "marcelo@gmail.com", "Sonic", "1", "13", "Sin turno"])
# voy a asumir que tiene estos animales
listaAnimales = ["Perro", "Gato", "Conejo", "Cobayo", "Hámster", "Hurón", "Erizo","Otros"]
# vamos a asumir algunas razas cargadas
listaRazas = ["Golden Retriever (perro)","Pastor Alemán (perro)","Bulldog Francés (perro)","Caniche (perro)","Beagle (perro)",
              "Rottweiler (perro)","Dálmata (perro)","Border Collie (perro)","Boxer (perro)","Schnauzer (perro)","Husky Siberiano (perro)",
              "Dogo Argentino (perro)","Mestizo (perro)","Siames (gato)","Persa (gato)","Sphynx (sin pelo) (gato)",
              "Mestizo (gato)","otras"]

#valido que no me ingresen datos vacios
def validarCamposVacios(textoIngreso,textoError):
    while True:
        valor = input(textoIngreso).strip()
        if valor == "":
            print(textoError)
        else:
            return valor

# valido el mail, por lo general suelo usar un liberia o expresiones regulares, pero como no la vimos, lo hago a mano
def validarEmail():
    while True:
        email = input("Ingrese email: ").strip()
        if email == "":
            print("!!! El email no puede estar vacío. Intente nuevamente.")
            continue
        if email.count("@") != 1:
            print("!!! El email debe contener exactamente un '@'.")
            continue
        parteLocal, dominio = email.split("@")
        if parteLocal == "" or dominio == "":
            print("!!! El email no puede empezar ni terminar con '@'.")
            continue
        if "." not in dominio:
            print("!!! El dominio debe contener al menos un punto (por ejemplo: gmail.com).")
            continue
        if email.startswith(".") or email.endswith("."):
            print("!!! El email no puede empezar ni terminar con un punto.")
            continue
        return email

def opbtenerValorSeleccionado(textUno, lista):
    print(textUno)
    j = 1
    for objeto in lista:
        print(str(j) + " - " + objeto)
        j += 1
    while True:
        tipo = input("Ingrese el valor (número): ").strip()
        if not tipo.isdigit():
            print("!!! Debe ingresar un número válido.")
            continue
        tipo = int(tipo)
        if tipo < 1 or tipo > len(lista):
            print(f"!!! Debe ingresar un número entre 1 y {len(lista)}.")
            continue
        break       
    return tipo

def pausa():
    input("\nPresioná ENTER para continuar...")

def mostrarUnCliente(cliente):
    print(f"NOMBRE: {cliente[0]} {cliente[1]} | DNI: {cliente[2]} | " +
            f"EMAIL: {cliente[3]} | MASCOTA: {cliente[4]} | TIPO: {listaAnimales[int(cliente[5])-1]} | RAZA: {listaRazas[int(cliente[6])-1]} | TURNO: {cliente[7]}")  
    print("\n================================================================")
    
def cargarDatos():
    cliente = []
    dni = ""
    tipo = ""
    raza = ""
    turno = ""
    print("\n=========================================")
    print(" #### Cargar datos de un cliente ####")

    nombre = validarCamposVacios("Ingrese Nombre: ","!!! El nombre no puede estar vacío. Intente nuevamente.")
    cliente.append(nombre) 

    apellido = validarCamposVacios("Ingrese Apellido: ","!!! El apellido no puede estar vacío. Intente nuevamente.")
    cliente.append(apellido)
    
    repetido = False
    while dni == "" or not dni.isdigit() or len(dni) > 8 or repetido == False: # validacion de dni
        repetido = True
        dni = input("Ingrese DNI (sin puntos): ").strip()
        if dni == "":
            print("!!! El DNI no puede estar vacío. Intente nuevamente.")
        elif not dni.isdigit():
            print("!!! El DNI debe contener solo números. Intente nuevamente.")
        elif len(dni) > 8:
            print("!!! El DNI no puede tener más de 8 dígitos. Intente nuevamente.")
        #no podemos dejar que haya cliente con el mismo dni
        #vamos a recorre los datos para verificarlo
        i = 0
        while i < len(clientesMatris):
           # pos 2 es dni
            if clientesMatris[i][2] == dni:
                print("!!! Ya existe un cliente registrado con ese DNI.")
                repetido = False
            i += 1         
    cliente.append(dni)

    email = validarEmail()
    cliente.append(email)

    mascota = validarCamposVacios("Ingrese Nombre de la mascota: ","!!! El nombre no puede estar vacío. Intente nuevamente.")
    cliente.append(mascota)

    tipo = opbtenerValorSeleccionado(" #### Tipos de Mascotas #### ",listaAnimales)
    cliente.append(tipo)

    while True:
        raza = opbtenerValorSeleccionado(" #### Razas #### ",listaRazas)
        if tipo == 1 and (1 <= raza <= 13 or raza == 18):      # Perro
            break
        elif tipo == 2 and (14 <= raza <= 17 or raza == 18):     # Gato
            break
        elif tipo >= 3 and raza == 18:     # Otro
            break
        else:
            print("!!! Esa raza no corresponde al tipo de mascota seleccionado.") 

    cliente.append(raza)
    
    cliente.append("Sin turno") # Inicializamos el turno como "Sin turno"
    print(":) Cliente cargado con éxito.")
    # agrego los datos en la clientesMatris
    clientesMatris.append(cliente)
    mostrarUnCliente(cliente)
    clientesMatris.sort(key=lambda cliente: (cliente[0].lower(), cliente[1].lower()))
    pausa()

def buscarUnCliente():
    if len(clientesMatris) == 0:
        print("\n!!! No hay datos cargados para realizar la busqueda.")
        return
    opcion = "0"
    while opcion != "4":
        print("\n=========================================")
        print(" #### Buscar un cliente ####")
        print("1) Buscar por DNI\n2) Buscar por nombre o apellido\n3) Ver todos los clientes\n4) Salir")
        opcion = input("Elija una opción (1-4): ").strip()
        encontrado = False

        if opcion == "1":
            dniBuscado = input("Ingrese el DNI a buscar: ").strip()
            for cliente in clientesMatris:
                if cliente[2] == dniBuscado:
                    print("\n--- Cliente Encontrado ---")
                    mostrarUnCliente(cliente)
                    encontrado = True
                    pausa()
                    break
        elif opcion == "2":
            #aca vamos a buscar por nombre y apellido, pero como un like 
            nombreBuscado = input("Ingrese el Nombre a buscar: ").strip().lower()
            apellidoBuscado = input("Ingrese el Apellido a buscar: ").strip().lower()
            for cliente in clientesMatris:
                if (nombreBuscado in cliente[0].lower() or apellidoBuscado in cliente[1].lower()):
                    print(f"\n--- Cliente Encontrado ---")
                    mostrarUnCliente(cliente)
                    encontrado = True
                    # No hacemos break aqui por si hay homónimos
                    pausa()
        elif opcion == "3":
            print("\n=========================================")
            print("\n#### Clientes Encontrados ####")
            for cliente in clientesMatris:
                mostrarUnCliente(cliente)
            encontrado = True
            pausa()
        elif opcion == "4":
            return    
        else:
            print("Opción no válida.")
        if (opcion=="1" or opcion=="2" or opcion=="3") and not encontrado:
            print("\n!!! No se encontró ningún cliente con esos datos.")
            pausa()

def buscarMascota():
    if len(clientesMatris) == 0:
        print("\n!!! No hay datos cargados para realizar la busqueda.")
        return
    print("\n=========================================")
    nombreMascota = input("Ingrese el nombre de la mascota a buscar: ").strip().lower()
    encontrado = False
    
    for cliente in clientesMatris:
        if nombreMascota in cliente[4].lower():
            print("------ Mascota Encontrada ------")
            mostrarUnCliente(cliente)
            encontrado = True
    
    if not encontrado:
        print(f"\n!!! No se encontró ninguna mascota llamada '{nombreMascota}'.")

def cantidadMascotasRaza():
    if len(clientesMatris) == 0:
        print("\n!!! No hay datos cargados.")
        return
    print("\n=========================================")
    print(" ###### Mascotas por raza ------ Cantidad ##### ")
    cantidadesPorRaza = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for cliente in clientesMatris:
       cantidadesPorRaza[int(cliente[6])-1] += 1
    x = 1
    for objeto in listaRazas:
        print(str(x) + " - " + objeto + " ------------ " + str(cantidadesPorRaza[x-1]))
        x += 1
    pausa()

def validarFechaHora():
    while True:
        fecha_str = input("Ingrese fecha (DD/MM): ").strip()
        if "/" not in fecha_str: # Validar formato básico antes de usar datetime
            print("Formato incorrecto. Use DD/MM")
            continue
        parte_dia, parte_mes = fecha_str.split("/", 1)
        # Validar que día y mes sean numéricos
        if not parte_dia.isdigit() or not parte_mes.isdigit():
            print("Día y mes deben ser números.")
            continue
        dia = int(parte_dia)
        mes = int(parte_mes)
        # Validación manual de rango
        if dia < 1 or dia > 31:
            print("Día inválido. Debe estar entre 1 y 31.")
            continue
        if mes < 1 or mes > 12:
            print("Mes inválido. Debe estar entre 1 y 12.")
            continue
        # Ahora pedimos hora
        hora_str = input("Ingrese hora (HH:MM): ").strip()
        if ":" not in hora_str:
            print("Formato incorrecto. Use HH:MM")
            continue
        parte_hora, parte_min = hora_str.split(":", 1)
        if not parte_hora.isdigit() or not parte_min.isdigit():
            print("La hora y los minutos deben ser números.")
            continue
        hora = int(parte_hora)
        minuto = int(parte_min)
        if hora < 0 or hora > 23:
            print("Hora inválida. Debe estar entre 00 y 23.")
            continue
        if minuto < 0 or minuto > 59:
            print("Minuto inválido. Debe estar entre 00 y 59.")
            continue
        # Validar fecha final usando datetime
        try:
            datetime(2025, mes, dia, hora, minuto)
            # Si llegamos acá es válida
            return f"{dia:02d}/{mes:02d} {hora:02d}:{minuto:02d}hs"
        except ValueError:
            print("Fecha inválida (el día no existe en ese mes). Intente otra vez.")

def asignarTurno():
    if len(clientesMatris) == 0:
        print("\n!!! No hay datos cargados.")
        return
    print("\n=========================================")
    print("\n#### Asignar Turno ####")
    dniBuscado = input("Ingrese el DNI del cliente para asignar turno: ").strip()
    
    clienteEncontrado = None
    indiceCliente = -1
    
    # Buscamos el cliente y guardamos su índice para poder modificarlo
    for i in range(len(clientesMatris)):
        if clientesMatris[i][2] == dniBuscado:
            clienteEncontrado = clientesMatris[i]
            indiceCliente = i
            break
            
    if clienteEncontrado:
        mostrarUnCliente(clienteEncontrado)
        nuevoTurno = validarFechaHora()
        clientesMatris[indiceCliente][7] = nuevoTurno
        print(":) Turno asignado correctamente.")
        mostrarUnCliente(clienteEncontrado)
        pausa()
    else:
        print("!!! No se encontró un cliente con ese DNI.")
        pausa()

def mostrarMenu():
    # menú principal con opciones para el usuario
    print("\n================ MENÚ PRINCIPAL ================\n1: Cargar datos de un cliente\n2: Buscar un cliente\n3: Buscar una mascota")
    print("4: Ver la cantidad de mascotas según la raza\n5: Asignar un turno\n6: Salir del programa")

# main del programa
def main():
    opcion = "0"
    while opcion != "6":  
        mostrarMenu()
        opcion = input("Seleccione una opción (1-6): ")
        match opcion:
            case "1":
                cargarDatos()
            case "2":
                buscarUnCliente()
            case "3":
                buscarMascota()
            case "4":
                cantidadMascotasRaza()
            case "5":
                asignarTurno()
            case "6":
                print("\nGracias por usar el programa!!!. Hasta luego.")
            case _:
                print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
