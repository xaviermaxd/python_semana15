def ventas_del_dia(producto,precio,cantidad):
    total = precio*cantidad
    igv = 0.18*total
    subtotal = total-igv

    file = open("archivo5.txt","a")
    file.write("Nombre del producto: " + producto + "\n")
    file.write("Cantidad: " + str(cantidad) + "\n")
    file.write("Subtotal: " + str(subtotal) + "\n")
    file.write("IGV: " + str(igv) + "\n")
    file.write("Total: " + str(total) + "\n")
    file.close()
    


def fecha_de_compra(fecha,hora):
    file = open("archivo5.txt","a")
    file.write("fecha de compra: " + str(fecha) + "\n")
    file.write("hora de compra: " + str(hora) + "\n")
    file.write("-"*20 + "\n")
    file.write(" "*20 + "\n")
    file.close()


def leer_archivo_5():
    file_object = open("archivo5.txt","r")
    print(file_object.read())
    