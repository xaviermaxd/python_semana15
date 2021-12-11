nombre = input("Ingrese su nombre: ")
curso = input("Ingrese su curso: ")
nota_1 = int(input("Ingrese la nota 1: "))
nota_2 = int(input("Ingrese la nota 2: "))

promedio = (nota_1+nota_2)/2

aprobado = False
if promedio >= 13:
    aprobado = True

file = open("archivo2.txt","w")
file.write("Nombre: " + nombre + "\n")
file.write("Curso: " + curso + "\n")
file.write("Nota 1: " + str(nota_1) + "\n")
file.write("Nota 2: " + str(nota_2) + "\n")
file.write("Promedio: " + str(promedio) + "\n")
file.write("Aprobado: " + str(aprobado) + "\n")

file.close()