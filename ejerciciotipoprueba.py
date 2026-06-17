#Funciones
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
        print()
    elif op==3:
        print()
    elif op==4:
        print()
    elif op==5:
        print()
    elif op==6:
        print("Gracias por usar el sistema. Vuelva pronto")