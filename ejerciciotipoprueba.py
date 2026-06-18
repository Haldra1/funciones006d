#Funciones
#opcion 2: buscar mascotas
def buscar_mascota(lista_mascotas, nombre_busqueda):
    #recorrer y devolver la posicion
    for i in range(len(lista_mascotas)):
        if lista_mascotas[i]["nombre"]== nombre_busqueda:
            return i #retorno la posicion
    return -1 #se termino el ciclo por tanto no se encontro



def mostrar_menu():
    print("="*35)
    print("MENU PRINCIPAL")
    print("="*35)
    print("1. Agregar una mascota")
    print("2. Buscar Mascota")
    print("3. Eliminar mascota")
    print("4. Marcar como Vacunada")
    print("5. Mostrar mascotas")
    print("6. Salir")
    print("="*35)

#funciones de validacion
def validar_nombre(name):
    #strip -> eliminar todos los espacion en blanco al inicio y al final de un string
    #retorna True si es valido o False si no
    return name.strip() != ""

def validar_especie(especie):
    especies_validas=["perro", "gato", "ave"]
    #retorna True si lo consigue o False si no
    return especie.strip().lower() in especies_validas

def validar_edad(edad):
    #El isdigit() se puede utilizar para no utilizar try/except y revisa si un string contiene solo digitos
    return edad.isdigit() and int(edad)>0 

def solicitar_opciones():
    while True:
        try:
            opcion= int(input("Ingrese la opcion a elegir: "))
            if opcion <=0 or opcion > 6:
                raise ValueError
            else:
                break
        except ValueError:
            print ("Debe elegir una opcion valida")
    return opcion

#funcion opcion 1
def agregar_mascotas(lista_m):
    #solicitamos los datos
    nombre=input("Ingrese el nombre de su mascota: ")
    correcta=validar_nombre(nombre)
    if not correcta:
        print("El nombre no puede esta en blanco")
        #El return provoca que el codigo pare aqui y no siga preguntando
        return
    especie=input("Ingrese la especie (perro ,gato o ave): ")
    correcta=validar_especie(especie)
    if not correcta:
        print("La especie solo puede ser perro, gat o ave")
        return
    edad=input("Ingrese la edad de la mascota: ")
    correcta=validar_edad(edad)
    if not correcta:
        print("La edad debe ser un numero entero mayor a 0")
        return
    #agregar los datos al diccionario
    mascota = {
        "nombre":nombre.strip(),
        "especie":especie.strip().lower(),
        "edad":int(edad),
        "vacunada":False
    }
    #agrego a la lista
    lista_m.append(mascota)
    print("Mascota agregada correctamente")
#opcion 4
def actualizar_vacunas(lista_m):
    #recorre la lista completa
    for m in lista_m:
        #preguntamos por la edad para validar
        if m["edad"] >=1:
            m["vacunada"] = True
        else:
            m["vacunada"] = False
#codigo principal
#declarar lista mascotas
datos_mascotas=[]

op=0
while op != 6:
    mostrar_menu()
    op=solicitar_opciones()

    if op==1:
       agregar_mascotas(datos_mascotas) 
    elif op==2:
        print("**** Buscar Mascota ****")
        busqueda_nombre=input("Ingrese el nombre de la mascota que desea buscar: ")
        posicion=buscar_mascota(datos_mascotas, busqueda_nombre)
        if posicion != -1:
            #Guardar en una variable de la masctoa en la posicion de la lista
            m=datos_mascotas[posicion]
            print(f"Mascota encontrada en la posicion: {posicion}")
            print(f"Nombre mascota: {m["nombre"]}")
            print(f"Nombre mascota: {m["especie"]}")
            print(f"Nombre mascota: {m["edad"]}")
            print(f"Nombre mascota: {m["vacunada"]}")
        else:
            print(f"No se encontro la mascota con el {busqueda_nombre}")
    elif op==3:
        print("**** Eliminar Mascota ****")
        #solicitar el nombre de la mascota a buscar
        nom=input("Ingrese el nombre de la mascota a eliminar: ")
        posicion=buscar_mascota(datos_mascotas, nom)
        if posicion !=-1:
            #procedemos a eliminarla
            datos_mascotas.pop(posicion)
            print("Mascota eliminada correctamente")
        else:
            print(f"La mascota {nom} no se encuentra registrada")
    elif op==4:
        actualizar_vacunas(datos_mascotas)
        print("Estado de vacunas actualizada")
    elif op==5:
        #actualizar el estado de las vacunas
        actualizar_vacunas(datos_mascotas)
        #mostrar sus datos
        if len(datos_mascotas) == 0:
            print("No hay mascotas en la lista")
        else:
            print("== Lista de Mascotas ==")
            for m in datos_mascotas:
                print(f"Nombre mascota: {m["nombre"]}")
                print(f"Especie: {m["especie"]}")
                print(f"Edad: {m["edad"]}")
                #variable para cambiar el valor de vacunada
                estado= "AL DÍA" if m["vacunada"] else "PENDIENTE"
                print(f"Estado Vacuna: {estado}")
    elif op==6:
        print("Gracias por usar el sistema. Vuelva pronto")