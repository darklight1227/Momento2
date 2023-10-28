
#Python usa la palabra reservada def
# Funcion que recibe un parametro y lo imprime
saludo = "hola mundo"

def imprimir(saludo):
    print(saludo)


imprimir(saludo)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Calcular masa corporal

def calcularImc(peso,altura):
    imc = peso/(altura*altura)
    print(imc)

calcularImc(74,1.74)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Calcular salario

salario = 1500000

def calcularSalud(salario):
    eps = salario*0.04
    return eps

def calcularPension(salario):
    pension = salario*0.04
    return pension

def calcularSalarioNeto(salario,eps,pension):
    salario_neto = salario - eps - pension
    print(salario_neto)

eps = calcularSalud(salario)
pension = calcularPension(salario)
calcularSalarioNeto(salario,eps,pension )
#-------------------------------------------------------------------------------------------------------------------------------------------
# Call back, llamar una funcion dentro de una funcion
def calcularSalarioNeto2(salario):
    eps = calcularSalud(salario)
    pension = calcularPension(salario)
    salario_neto2 = salario - eps - pension
    print(salario_neto2)

calcularSalarioNeto2(salario)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Funcion de la que desconocemos los parámetros

def registro(*items):
    print(f"Los datos son:  {items[:4]}")


registro("Pepito","Perez",25,"Pepito@mail.com")

#-------------------------------------------------------------------------------------------------------------------------------------------
def calcularpagonomina(salario):

   pago_eps = lambda salary : salario*0.04
   pago_pension = lambda sal : salario*0.04
#las lambdas son funciones locales anonimas, funcionan dentro de una funcion pero exclusivamente para esta parte del codigo
# Estructura ----variable(se convierte en funcion)---- = lamba ----argumento ---- : ---- operacion -----
   salario_neto3 = salario - pago_eps(salario) - pago_pension(salario)


   print(salario_neto3)
calcularpagonomina(1000000)

#-------------------------------------------------------------------------------------------------------------------------------------------

#Bancolombia requiere calcular los salarios de su nueva start up Pagui:
# 1 puede registrar nombre, apellido, cargo, area y salario
# 2 requiere poder listar a los empleados
# 3 requiere calcular el salario neto de cada uno, teniendo presente que si gana <2 smlv se paga aux de transporte
# 4 Imprimir colilla de pago
# 5 Un empleado podrá ingresar al sistema, hacer su colilla e imprimirla, nada más
# 6 un analista de recursos humanos podra visualizar todos los empleados y todas las colillas, ademas buscar por empleado
# 7 como plus el de recursos humanos podra visualizar el total de la nómina
# 8 solo se puede realizar una funcion por ejm calculadora nomina
#-------------------------------------------------------------------------------------------------------------------------------------------













