#Funciones
def mostrar_menu():
    print("="*35)
    print("======== MENÚ PRINCIPAL ========")
    print("="*35)
    print(" 1. Agregar reserva ")
    print(" 2. Buscar reserva")
    print(" 3. Eliminar reserva")
    print(" 4. Confirmar reservas")
    print(" 5. Mostrar reservas")
    print(" 6. Salir ")
    print("="*35)

def escoger_opcion():
    while True:
        try:
            opcion=int(input("Selecciona una de las opciones: \n"))
            if opcion<=0 or opcion>6:
                raise ValueError
            else:
                break
        except ValueError:
            print("Ingresa una opcion valida")
    return opcion
      
def Agregar_reserva(lista_reserva):
    nombre_cliente=input("Ingrese su nombre completo: \n")
    validado=validar_nombre(nombre_cliente)
    if not validado:
        print("Error: El nombre completo no puede estar en blanco")
        return
    numero_habitacion=input("Ingrese el numero de habitacion (1 a 200): \n")
    validado=validar_NHabitacion(numero_habitacion)
    if not validado:
        print("Error: La habitacion ingresada es incorrecta ingrese una entre la numero 1 al 200 ")
        return
    cant_noches=input("Ingrese la cantidad de noches que se hospedara en el Hotel: \n")
    validado=validar_Cnoches(cant_noches)
    if not validado:
        print("Error: Minimo tienes que reservar por 1 noche")
        return
    Datos_usuario={
        "nombre":nombre_cliente.strip().upper(),
        "N_Habitacion":int(numero_habitacion),
        "C_noches":int(cant_noches),
        "Confirmada":False
    }
    lista_reserva.append(Datos_usuario)
    print("Reserva registrada correctamente")
    
def validar_nombre(name):
    return name.strip().upper() != ""

def validar_NHabitacion(numero):
    return numero.isdigit and int(numero)>1 and int(numero)<200

def validar_Cnoches(cantidad_noches):
    return int(cantidad_noches)>0

def buscar_reserva(lista_m, nombre_busqueda):
    for i in range (len(lista_m)):
        if lista_m[i]["nombre"] == nombre_busqueda:
            return i
    return -1            

def confirmar_reserva(lista_r):
    for i in lista_r:
        if i["C_noches"] >=2:
            i["Confirmada"]= True
        else:
            i["Confirmada"]= False
#Programa principal
Datos_Reserva=[]

opc=0
while opc!=6:
    mostrar_menu()
    opc=escoger_opcion()
    if opc == 1:
        Agregar_reserva(Datos_Reserva)
    elif opc == 2:
        nombre_busq=input("Ingrese el nombre completo de la persona que reservo: \n").upper()
        posicion=buscar_reserva(Datos_Reserva, nombre_busq)
        if posicion != -1:
            m=Datos_Reserva[posicion]
            print("******* Datos de Reserva *******")
            print(f"El numero de la reserva del huesped es: {posicion}")
            print(f"Nombre Cliente: {m["nombre"]}")
            print(f"Numero de Habitacion: {m["N_Habitacion"]}")
            print(f"Cantidad de noches: {m["C_noches"]}")
            print(f"Confirmacion Reserva: {m["Confirmada"]}")
        else:
            print(f"No se encontro una reserva al nombre de: {nombre_busq}")
    elif opc == 3:
        eliminar_reserva=input("Ingrese el nombre del huesped cuya reserva se desea eliminar: ").upper()
        posicion=buscar_reserva(Datos_Reserva, nombre_busq)
        if posicion != -1:
            Datos_Reserva.pop(posicion)
            print("Reserva eliminada correctamente")
        else:
            print("La reserva del huésped 'nombre' no se encuentra registrada.")
    elif opc == 4:
        confirmar_reserva(Datos_Reserva)
    elif opc == 5:
        confirmar_reserva(Datos_Reserva)
        print("=== LISTA DE RESERVAS ===")
        for m in Datos_Reserva:
            print(f"Nombre Cliente: {m["nombre"]}")
            print(f"Numero de Habitacion: {m["N_Habitacion"]}")
            print(f"Cantidad de noches: {m["C_noches"]}")
            estado= "CONFIRMADA" if m["Confirmada"] else "PENDIENTE"
            print(f"Confirmacion Reserva: {estado}")
            print()
            print("*"*40)
    elif opc == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")