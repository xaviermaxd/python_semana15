import ventas, time

contador = 0
dia = 0

while True:
    print("Ingrese una opcion: ")
    print("1) Registar compra")
    print("2) Observar facturas")
    print("3) Salir")
    print(" "*30)

    opcion = input("ingrese una opcion: ")
    if opcion == "1":
        if contador < 3:
            if dia == int(time.strftime("%d")):
                contador += 1
            else:
                contador = 1

            print(" "*30)
            producto = input("Ingrese el nombre del producto: ")
            precio = int(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad a comprar: "))
            fecha = time.strftime("%d/%m/%y")
            hora = time.strftime("%H:%M:%S")
            print(" "*30)
            ventas.ventas_del_dia(producto, precio, cantidad)
            ventas.fecha_de_compra(fecha,hora)
            print(" "*30)
            dia = int(time.strftime("%d"))
        else:
            if dia != int(time.strftime("%d")):
                contador = 0
                print("ya esta habilitado el sistema")
                print(" "*30)
            else:
                print(" "*30)
                print("3 ventas cumplidas, esperar hasta el dia siguiente")
                print(" "*30)

    if opcion == "2":
        print(" "*30)
        ventas.leer_archivo_5()
        print(" "*30)

    if opcion == "3":
        print("DATOS GUARDADOS")
        break    