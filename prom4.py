import funciones

while True:
    print("Ingrese una opcion: ")
    print("1) Leer el archivo 1")
    print("2) Registrar datos en el archivo 2")
    print("3) Leer el archivo 2")
    print("4) Salir")

    opcion = input("ingrese una opcion: ")
    if opcion == "1":
        funciones.leer_archivo_1()
        print("-"*30)
        print(" "*30)

    if opcion == "2":
        nombre = input("Ingrese su nombre: ")
        curso = input("Ingrese su curso: ")
        nota_1 = int(input("Ingrese la nota 1: "))
        nota_2 = int(input("Ingrese la nota 2: "))

        funciones.registrar_datos(nombre, curso, nota_1, nota_2)

        print("Se registro los datos")
        print("-"*30)
        print(" "*30)

    if opcion == "3":
        funciones.leer_archivo_2()
        print("-"*30)
        print(" "*30)

    if opcion == "4":
        print("DATOS GUARDADOS")
        break    

