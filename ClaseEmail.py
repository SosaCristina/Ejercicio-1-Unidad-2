class Email:
    __idCuenta=""
    __dominio=""
    __tipoDominio=""
    __Contraseña=""

    def generar (self, idC,dom,tipoDom,contra):
        self.__idCuenta= idC
        self.__dominio= dom
        self.__tipoDominio= tipoDom
        self.__Contraseña=contra

    def  getIde (self):
        return self.__idCuenta

    def retornaEmail(self):
        return self.__idCuenta+"@"+self.__dominio +"."+self.__tipoDominio
    def getDominio(self):
        return self.__dominio

    def __str__(self):
        return "Ide:%s - dominio:%s  tipodominio: %s" % (self.__idCuenta,self.__dominio,self.__tipoDominio)

    def modificarcontraseña(self,c):
        if(c == self.__Contraseña):
            nueva=input("Ingresar nueva contraseña\n")
            self.__Contraseña=nueva
            print("Contraseña modificada con exito")
        else:
            print("Contraseña incorrecta, no es posible modificarla")

    def crearCuenta(self,correo):
        arre1= correo.split("@")
        self.__idCuenta=arre1[0]
        arre2=arre1[1].split(".")
        self.__dominio=arre2[0]
        self.__tipoDominio=arre2[1]
        print("El correo ingresado fue aceptado con exito")



