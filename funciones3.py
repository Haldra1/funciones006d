#Funciones
def mostrar_encabezado():
    print("**********************************")
    print("|| Sistema de Registro Escolar ||")
    print("**********************************")
def datos_est():
    lista_datos={}
    lista_datos["nombre"]=input("Ingrese el nombre del estudiante: \n")
    while True:
        try:
            lista_datos["semestre"]=int(input("Ingrese el semestre que cursa: \n"))
            if lista_datos["semestre"]<1 or lista_datos["semestre"]>5:
                print("Debe ingresar un semestre del 1 al 5")
            else:
                break
        except ValueError:
            print("Debe ingresar numeros")
    lista_datos["carrera"]=input("Ingrese la carrera que estas cursando: \n")
    lista_datos["rut"]=input("Ingrese el rut del estudiante: \n")
    return lista_datos
def mostrar_ficha(estudiante):
    print(f"Nombre Estudiante: {estudiante["nombre"]}")
    print(f"Rut Estudiante: {estudiante["rut"]}")
    print(f"Carrera Estudiante: {estudiante["carrera"]}")
    print(f"Semestre Estudiante: {estudiante["semestre"]}")
#Codigo principal
datos=datos_est()
mostrar_encabezado
mostrar_ficha(datos)
