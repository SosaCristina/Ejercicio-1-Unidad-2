from ClaseEmail import Email
import csv

if __name__=="__main__":
    objetoEmail=Email()
    nombre=input("Ingrese nombre\n")
    id=input("Ingrese Id de su cuenta\n")
    dom=input("Ingrese Dominio\n")
    tipodom=input("Ingrese tipo de dominio\n")
    contra=input("Ingresar contraseña\n")
    objetoEmail.generar(id,dom,tipodom,contra)
    print(objetoEmail)
    print("Estimado" + nombre + "te enviaremos tus mensajes a la direccion:{}".format(objetoEmail.retornaEmail()))
    print("Modificar Contraseña")
    c=input("Ingresar contraseña actual\n")
    objetoEmail.modificarcontraseña(c)
    otroObjeto=Email()
    correo=input("Ingresar correo\n")
    otroObjeto.crearCuenta(correo)


    listacorreos=[]
    o_email=Email()
    archivo=open("correos.csv")
    reader=csv.reader(archivo,delimiter=";")
    for fila in reader:
        correo=fila[0]
        contraseña=fila[1]
        o_email.crearCuenta(correo)
        listacorreos.append(o_email)
        print(o_email)

    archivo.close()

    identificador=input("Para saber si las ide estan repetidas, debe ingresar un identificador\n")
    i=0
    while i<len(listacorreos) and listacorreos[i].getIde()!=identificador :
       i+=1
    if(i<=len(listacorreos)):
        print("Si esta repetido")
    else:
        print("No se encuentra repetido")








