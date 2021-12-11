def leer_archivo_1():
    file_object = open("archivo1.txt","r")
    print(file_object.read())


def registrar_datos(nombre,curso,nota_1,nota_2):
    promedio = (nota_1+nota_2)/2

    aprobado = False
    if promedio >= 13:
        aprobado = True

    file = open("archivo2.txt","a")
    file.write("Nombre: " + nombre + "\n")
    file.write("Curso: " + curso + "\n")
    file.write("Nota 1: " + str(nota_1) + "\n")
    file.write("Nota 2: " + str(nota_2) + "\n")
    file.write("Promedio: " + str(promedio) + "\n")
    file.write("Aprobado: " + str(aprobado) + "\n")
    file.close()

def leer_archivo_2():
    file_object = open("archivo2.txt","r")
    print(file_object.read())