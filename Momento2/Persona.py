
class Persona:

    def __init__(self,id,nombre,apellido,correo,contrasena):
        self.id = id
        self.nombre  = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasena = contrasena


        #vamos a generar Getter and Setter
        #GET

    @property
    def id(self):
        return self.id


    #SET
    @id.setter
    def id(self, id):
        self.id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre (self,nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def nombre(self, apellido):
        self._apellido = apellido

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

    @property
    def contrasena(self):
        return self._contrasena

    @correo.setter
    def contrasena(self, contrasena):
        self._contrasena = contrasena

    #Vamos a generar los metodos para registrar los usuarios e imprimir el registro

    def registrar_usuario(self):

        id = input("Ingrese el id del usuario")
        nombre = input("Ingrese el nombre del usuario")
        apellido = input("Ingrese el apellido del usuario")
        correo = input("Ingrese el correo del usuario")
        contrasena = input("Ingrese la contrasena del usuario")

    def imprimir_Registro(self):

        print(f"Id : {self._id} Nombre : {self._nombre} Apellido : {self._apellido} Correo : {self._correo} Contrasena : {self._contrasena} ")
