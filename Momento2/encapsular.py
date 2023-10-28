class Persona:


#vamos a crear un constructor
 def __init__(self,id,nombre,apellido,correo,password):

    self._id = id
    self._nombre = nombre
    self._apellido = apellido
    self._correo = correo
    self._password = password
    #Este contiene la palabra reservada self
    #Similar a this en java, por ejemplo




#Encapsulamiento con python

# Se usa underscore al principio de la variable para indicar que será encapsulada

#Usamos decoradores para crear los gett


#Esto es un setter

@property
def id(self):
        return self.id

#Vamos a hacer lo mismo para cada uno de los a

#Instancia

@nombre.setter
def nombre(self,nombre):
 self._nombre = nombre


@property
def apellido(self):
        return self._apellido


@apellido.setter
def apellido(self,apellido):
    self._apellido = apellido


    @property
    def correo(self):
        return self._correo


    @correo.setter
    def correo(self,correo):
        self._correo = correo


    @property
    def password(self):
        return self._password



    @password.setter
    def password(self,password):
        self._password = password



    def imprimir_persona(self):
        print(f"Id:{self._id} nombre: {self._nombre} apelldio {self._apellido}")











    
    
