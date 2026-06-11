#Funciones
def convertir_nota(puntaje, puntaje_total):
    nota=(puntaje * 6/puntaje_total)+1
    return round(nota, 1)
#Principal
while True:
    try:
        p=int(input("Ingrese el puntaje del estudiante: "))
        if p<0:
            print("Error: El puntaje no puede ser menor que 0")
        else:
            break
    except ValueError:
        print("Error: Ingresa números")
#end while
while True:
    try:
        pt=int(input("Ingrese el puntaje total del examen: "))
        if pt< 0:
            print("Error: El puntaje total no puede ser menor 0")
        else:
            break
    except ValueError:
        print("Error: Ingresa números")
#end while
#llamar funcion
calificacion=convertir_nota(p, pt)
print(f"La calificación en escala chilena es: {calificacion}")