

from Persona import Persona #esto importa la clas Persona para ser usada en otra clase


#en Test persona hemos importado la clase persona ahora creamos
# Una instancia de persona
persona1 = persona(1,"Pepito","Perez","PP@gmail.com","xyz123")

id = 1

persona1._id(id) #Esto genera un error porque el valor esta protegido


persona1.imprimir_persona()
