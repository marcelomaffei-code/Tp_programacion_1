clientesMatris = [] # lista de clientes
# voy a asumir que tiene estos animales
listaAnimales = ["Perro", "Gato", "Conejo", "Cobayo", "Hámster", "Hurón", "Erizo","Otros"]
# vamos a asumir algunas razas cargadas
listaRazas = ["Golden Retriever","Pastor Alemán","Bulldog Francés","Caniche (Poodle)","Beagle","Rottweiler","Dálmata","Border Collie","Boxer","Schnauzer","Husky Siberiano","Dogo Argentino","Mestizo (Perro)","Siames","Persa","Sphynx (sin pelo)","Mestizo (Gato)","otras"]

#valido que no me ingresen datos vacios
def validarCamposVacios(textoIngreso,textoError):
    valor = ""
    valor = input(textoIngreso).strip()
    while valor == "":
        print(textoError)
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
        parte_local, dominio = email.split("@")
        if parte_local == "" or dominio == "":
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

def cargarDatos():
    cliente = []
    dni = ""
    tipo = ""
    raza = ""
    turno = ""

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
            print(clientesMatris[i][2]) # se que dni esta en la pos 2
            if clientesMatris[i][2] == dni:
                print("!!! Ya existe un cliente registrado con ese DNI.")
                repetido = False
            i += 1         
    cliente.append(dni)

    email = validarEmail()
    cliente.append(email)

    mascota = validarCamposVacios("Ingrese Nombre de la mascota: ","!!! El nombre no puede estar vacío. Intente nuevamente.")
    cliente.append(mascota)

    tipo = opbtenerValorSeleccionado("-Tipos de Mascotas-",listaAnimales)
    cliente.append(tipo)

    raza = opbtenerValorSeleccionado("-Razas-",listaRazas)
    cliente.append(raza)
    
    cliente.append(turno) #aca lo le asigno turno, porque solo carga sus datos
    print(":) Cliente cargado con éxito.")
    # agrego los datos en la clientesMatris
    clientesMatris.append(cliente)

def buscarUnCliente():
    if len(clientesMatris) == 0:
        print("\n No hay datos cargados para realizar la busqueda.")
        return

    print("\n--- Buscar un cliente ---")
    print("1) Buscar por DNI\n2) Buscar por nombre y apellido")
    modo = input("Elija una opción (1-2): ").strip()

    
"""
    if modo == "1":
        dni = input("Ingrese DNI: ").strip()
        i = 0
        while i < len(dnis):
            if dnis[i] == dni:
                mostrar_cliente(i)
                return
            i += 1
        print("No se encontró cliente con ese DNI.")

    elif modo == "2":
        nombre_apellido = input("Ingrese nombre y apellido (exacto): ").strip()
        objetivo = normalizar_texto(nombre_apellido)
        i = 0
        while i < len(nombres_apellidos):
            if normalizar_texto(nombres_apellidos[i]) == objetivo:
                mostrar_cliente(i)
                return
            i += 1
        print("No se encontró cliente con ese nombre y apellido.")
    else:
        print("Opción inválida.")

"""




def mostrarMenu():
    # menú principal con opciones para el usuario
    print("\n================ MENÚ PRINCIPAL ================")
    print("1: Cargar datos de un cliente")
    print("2: Buscar un cliente")
    print("3: Buscar una mascota")
    print("4: Ver la cantidad de mascotas según la raza")
    print("5: Asignar un turno")
    print("6: Salir del programa")

# función principal del programa
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
                print("")
            case "4":
                print("")
            case "5":
                print("")
            case "6":
                print("\nGracias por usar el programa!!!. Hasta luego.")
            case _:
                print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()





"""








def buscar_mascota():
    print("\n--- Buscar una mascota ---")
    nombre = input("Nombre de la mascota (exacto): ").strip()
    objetivo = normalizar_texto(nombre)

    encontrados = []  # guardamos índices para mostrar todos los que coincidan
    i = 0
    while i < len(nombres_mascotas):
        if normalizar_texto(nombres_mascotas[i]) == objetivo:
            encontrados.append(i)
        i += 1

    if len(encontrados) == 0:
        print("No se encontró mascota con ese nombre.")
    else:
        print("Se encontraron", len(encontrados), "coincidencia(s):")
        j = 0
        while j < len(encontrados):
            mostrar_cliente(encontrados[j])
            j += 1


def cantidad_por_raza():
    print("\n--- Cantidad de mascotas según la raza ---")
    # Para no usar diccionarios, construimos dos listas: razas_unicas y cant_razas
    razas_unicas = []
    cant_razas = []

    i = 0
    while i < len(razas_mascotas):
        raza = normalizar_texto(razas_mascotas[i])
        # buscar raza en razas_unicas
        pos = -1
        j = 0
        while j < len(razas_unicas):
            if razas_unicas[j] == raza:
                pos = j
                break
            j += 1
        if pos == -1:
            razas_unicas.append(raza)
            cant_razas.append(1)
        else:
            cant_razas[pos] = cant_razas[pos] + 1
        i += 1

    if len(razas_unicas) == 0:
        print("No hay mascotas cargadas.")
    else:
        print("Raza -> Cantidad")
        k = 0
        while k < len(razas_unicas):
            print("-", razas_unicas[k], "->", cant_razas[k])
            k += 1


def asignar_turno():
    print("\n--- Asignar un turno ---")
    dni = input("Ingrese DNI del cliente: ").strip()

    i = 0
    while i < len(dnis):
        if dnis[i] == dni:
            print("Cliente encontrado:")
            mostrar_cliente(i)
            turno = input("Ingrese fecha y hora del turno (ej: 12/11/2025 15:30): ").strip()
            if turno == "":
                print("✗ Turno vacío. Operación cancelada.")
                return
            turnos[i] = turno
            print("✓ Turno asignado correctamente.")
            return
        i += 1

    print("No se encontró un cliente con ese DNI.")


# -------------------------------
# Apoyo (impresión de un "registro" en la posición i)
# -------------------------------

def mostrar_cliente(i):
    print("----------------------------------------")
    print("Nombre y Apellido:", nombres_apellidos[i])
    print("DNI:", dnis[i])
    print("Correo:", correos[i])
    print("Mascota:", nombres_mascotas[i])
    print("Tipo:", tipos_mascotas[i])
    print("Raza:", razas_mascotas[i])
    if turnos[i] != "":
        print("Turno asignado:", turnos[i])
    else:
        print("Turno asignado: (sin turno)")
    print("----------------------------------------")



"""



