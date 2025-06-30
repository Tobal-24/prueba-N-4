stock1 = 50
stock2 = 50
entradas = {}

def venta():
    global stock1 ,stock2
    nombre = input("Ingrese su nombre: ")
    if nombre in entradas:
        print("el nombre ya existe ")
        return
    print("1- show con tripulacion\n 2- Show con sonrisa")
    opcion= input("Elige el show (1 o 2): ")
    if opcion == "1" and stock1 > 0:
        entradas [nombre] = 1
        stock1 -= 1
        print("compra de entrada realizada con exito.")
    elif opcion == "2" and stock2 > 0:
        entradas[nombre] = 1
        stock2 -= 1
        print("compra de entrada realizada con exito.")
    else:
        print("Opcion invalida o sin stock. ")

def cambio():
    global stock1 , stock2
    nombre = input("ingrese su nombre: ")
    if nombre not in entradas:
        print ("no encontrado.")
        return
    actual = entradas [nombre]
    nuevo = 2 if actual == 1 else 1
    if (nuevo == 1 and stock1 > 0) or (nuevo == 2 and stock2 > 0):
        if nuevo == 1:
            stock1 -= 1
            stock2 += 1
        else:
            stock2 -= 1
            stock += 1
        entradas [nombre] = nuevo
        print("cambio realizado")
    else:
        print (" sin cupo para cambiar ")

def stock ():
    print("stock show 1:" , stock1)
    print("stock show 2:" , stock2)

while True:
    print("1-venta de entradas\n 2- cambio de show \n 3- stock disponibles\n 4- salir del programa")
    opcion = input("elige una de las opciones a elegir: ")
    if opcion == "1":
        venta()
    elif opcion == "2":
        cambio()
    elif opcion == "3":
        stock()
    elif opcion == "4":
        print("¡hasta luego y muchas gracias!")
        break
    else:
        print("opcion no valida")    



     