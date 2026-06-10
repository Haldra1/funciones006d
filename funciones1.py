#Funciones
def datos_productos(nombre, stock, precio): #No importa el orden de los parametros
    print("====================================")
    print(f"||Nombre del producto {nombre} ||")
    print(f"||Precio del producto {precio} ||")
    print(f"||Stock del producto {stock} ||")
    print("====================================")
    
#Codigo principal
nombre=input("Ingrese el nombre del producto: \n")
while True:
    try:
        precio=int(input("Ingrese el precio del producto: \n"))
        if precio<=0:
            print("Error: Debe ser un número positivo ")
        else:
            break
    except ValueError:
        print("Error: Ingrese numeros")
while True:
    try:
        stock=int(input("Ingrese el stock del producto: \n"))
        if precio< 0:
            print("Error: No puede ser un numero negativo ")
        else:
            break
    except ValueError:
        print("Error: Ingrese numeros")
datos_productos(nombre, stock, precio) #Se deben enviar los parametros en el orden exacto que los declare al crear la funcion
