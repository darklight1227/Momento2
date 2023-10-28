from Persona import Persona


class Empleado(Persona):


    def __init__(self,id,nombre,apellido,correo,contrasena, cargo, salario, tipo_contrato):
        super().__init__(id,nombre,apellido,correo,contrasena)
        self._cargo = cargo
        self._salario = salario
        self._tipo_contrato = tipo_contrato

        # vamos a generar Getter and Setter
        # GET

    @property
    def cargo(self):
        return self._cargo

        # SET
    @cargo.setter
    def cargo(self, cargo):
        self.cargo = cargo

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    @property
    def tipo_contrato(self):
        return self._tipo_contrato

    @tipo_contrato.setter
    def tipo_contrato(self, tipo_contrato):
        self._tipo_contrato = tipo_contrato


    #Vamos a sobreescribir los metodos

    def registrar_usuario(self):
        self._id = input("Ingrese el id del usuario")
        self._nombre = input("Ingrese el nombre del usuario")
        self._apellido = input("Ingrese el apellido del usuario")
        self._correo = input("Ingrese el correo del usuario")
        self._contrasena = input("Ingrese la contrasena del usuario")
        self._cargo = input("Ingrese el cargo del empleado")
        self._salario = float(input("Ingrese el salario del empleado"))
        self._tipo_contrato = input("Ingrese el tipo de contrato del empleado")


    def imprimir_Registro(self):
        super().imprimir_Registro()
        print(f"Cargo: {self._cargo} Salario: {self._salario} Tipo de contrato : {self._tipo_contrato}")


    def iniciar_sesion(self, appEmpleado):
        correo_emp = input("Ingrese el correo registrado: ")
        contrasena_emp = input("Ingrese la contraseña: ")

        if correo_emp == self._correo and contrasena_emp == self._contrasena:
            return True
        else:
            return False

    def appEmpleado(self,iniciar_sesion, imprimir_Registro):
        iniciar_sesion() == True
        print("Has iniciado sesion")
        imprimir_Registro()


