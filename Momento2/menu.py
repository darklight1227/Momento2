from Persona import Persona
from Empleado import Empleado

empleado = Empleado

def menuApp():

    print("Inicialice con 1")

    init = int(input("Escribe 1"))

    while init !=0:

        print("Seleccione 1 para registrar Empleado\n",
              "Seleccione 2 para Iniciar Sesion\n",
              "Seleccione 3 para salir")


        opc = int(input("Ingrese una opcion"))

        if opc ==1:
            empleado.registrar_usuario()

        elif opc ==2:
            empleado.iniciar_sesion()
            empleado.appEmpleado(empleado.iniciar_sesion(), empleado.imprimir_Registro())

        elif opc ==3:
            print("Salir")

