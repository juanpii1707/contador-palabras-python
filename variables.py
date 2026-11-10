# VARIABLES: [Son contenedores que almacenan datos, que pueden cambiar durante la ejecucion de un programa]
# Cada variable tiene un nombre único y un valor asociado al nombre
# Para poder asignarle ese valor, usamos el operador '='
# Ejemplo:
x = 5               # para números 
nombre = "jhon"     # para letras, se usa comillas
y = str(x)          # Sí quiero que la variable 'y' sea la version texto(sring) de 'x' que tiene asignado un número
# el formato STR se usa para cambiar el formato de una varibale

print(x)            # 5
print(nombre)       # jhon
print(y)            # el resultado es '5', nos da un número pero el formato del número es ahora string


# VARIABLES VALIDAS
# Validos: Si inicia con una letra y sin caracteres especiales
mivariable = "Texto"
# Validos: Si inicia con una letra y con guiones bajos intermedios
mi_variable = "Texto"
# Validos: Si inicia con una letra y con guiones bajos intermedios
_mi_variable = "Texto"
# Validos: se llaman 'camelCase' que es usar mayúsculas al iniciar cada palabra, excepto la primera o puede ser todo mayúscula
miVariable = "Texto"
MIVARIABLE = "Texto"
# Validos: podemos usar números con las letras, pero los números no deben ir al inicio
mivariable2 = "Texto"
# Validos: podemos usar números con las letras y guiones, pero los números no deben ir al inicio
mivariable_2 = "Texto"


# VARIABLES INVALIDAS
# Invalidas: iniciar con números
# 2mivariable = "Texto"
# Invalidas: usar guion medio
# mi-variable = "Texto"
# Invalidas: que haya espacios entre variables
# mi variable = "Texto"

# Invalidas: tampoco está permitido, pero si en javascript, el simbolo dolar
# $mi_variable = "Texto"

#REPASO:
#VARIABLES: Contenedores que almacenan datos que pueden cambiar durante la ejecución de un programa, 
#cada variable tiene un nombre único y un valor ascociado, para asignarle el valor se usa el operador '='
x = 5
nombre = "Juan"
y = str(x)  #Casteo: cambiar de formato un valor de numero a cadena de caracteres o viceversa.
print(x)
print(nombre)
print(y) #se imprime el número en formato carácter

#VALIDO:Sí inicia con letra y sin caracteres especiales
mivariable = "texto"

#VALIDO:Sí inicia con letra y con guiones abajo
mi_variable = "texto"

#VALIDO:Sí inicia con letra y con guiones al inicio
_mi_variable = "texto"

#VALIDO:camelcase(que es usar mayúscula al comenzar cada palabra excepto la primera)
miVariable = "texto"

#VALIDO:Sí Todas estan en mayúscula
MIVARIABLE = "texto"

#VALIDO: Se puede usar números pero no al inicio
mivariable2 = "texto"
#-------------------
#NoVALIDO:Sí inicia con letra y con guiones al inicio
#2mivariable = "texto" 

#NoVALIDO:Sí inicia con letra y con guiones al inicio
#2mivariable = "texto"

#NoVALIDO:Tampoco se puede usar guion medio
#mi-variable = "texto"#

#NoVALIDO:Tampoco se puede usar espacios
#mi variable = "texto"

#NoVALIDO:Usar simbolo del dolar
#$mivariable = "texto"

#Tipos de Datos Numéricos

x = 1     #int
y = 2.8   #float
z = 2j    #complex

print(type(x))
print(type(y))
print(type(z))

#CASTEO NUMERO FLOTANTO CON ENTERO

X=5

y=float(X)

print(y)
print(type(y)) #el número entero s paso a flotante con coma.


X=4.25

y=int(X)

print(y)
print(type(y)) #el número flotante 4.25 paso a entero sin coma.

#Random: es una libreria de python que genera valores aleatorios

import random

x = random.randrange(1,10) #No incluye el maximo número
print(x)

x = random.random()    #Esto es un método dentro de la libreria random que genera números del 0 al 9
print(x)
print(type(x))  #Nos da un número flotante


x = random.randint(1,9)    #Esto es un método dentro de la libreria random que genera números del 0 al 9
print(x)
print(type(x))  #Nos da un número entero

#STRING: cadena de caracteres.

print("Hola Mundo")

txt = "Hola Mundo"  #comilla simple
print(txt)

#txt  = ""Hola Mundo""  #comilla doble
print(txt)

txt = """Hola Mundo"""  #comilla triple
print(txt)
#Con las comillas triples, podemos hacer saltos de línea sin error de sintaxys

#¿Podemos trabajar con sus caracteres?
txt="""Hola Mundo"""  #comilla triple
print(txt[0])     #Con la llave entramos al índice del carácter según su posición, H=indice [0]
print(txt[1])     #Con la llave entramos al índice del carácter según su posición, o=indice [1]
print(txt[2])     #Con la llave entramos al índice del carácter según su posición, l=indice [2]
print(txt[3])     #Con la llave entramos al índice del carácter según su posición, a=indice [3]
print(txt[4])     #Con la llave entramos al índice del carácter según su posición,  =indice [4]

print(len(txt))  #Nos da el número de carácteres, son 10 en total.
#Los espacios y saltos de línea son tomados como partes de los caracteres en len como espacios.


#Si queres saber si una palabra o frase esta en un texto:
txt1 = "debó repasar todos los archivos de python de nuevo para no perder lo que habia visto en las clases"
print("de nuevo para no" in txt1)


#Slicing: ponemos desde un caracter hasta un caracter no incluido al final, de una frase dentre de una variable
txt = "seguimos trabajando con cadena de caracteres"
print(txt[0:19])

#Para convertir un string en mayúscula a minúscula(lowercase)
txt2 = "CUANDO ESCRIBO EN MAYÚSCULA, TODOS CREEN QUE ESTOY GRITANDO"
print(txt2.lower())

#Para convertir un string en minúscula a mayúscula(uppercase)
txt2 = "este texto es tan importante que si lo escribo en minúscula, nadie lo entenderá"
print(txt2.upper())

#Para corregir un string que tiene espacios vacios,usamos el método 'strip'
txt2 = "             ¡uy! deje espacios en el texto"
print(txt2.strip())

#Operaciones con cadena de caracteres(string)
#Con el símbolo '+' concatenamos los string en una variable
a = "Hola"
b = "Mundo"
c = a  + " " + b
print(c)

#Sí queremos concatenar string con integer:
a = "Hola: "
b = 17
#primer método: por casteo
c = a + str(b)
print(c)
#segundo método: por 'format()
a = "Hola: {}"
b = 17
print(a.format(b))

##Sí queremos concatenar string con uno más integer:
a = "Hola número {} y número {}"
b = 17
c = 18
print(a.format(b ,c))

#Sí queremos cambiar la posición de los integer:
a = "Hola número {1} y número {0}"
b = 17
c = 18
print(a.format(b ,c))
#----------
#Caracteres no permitidos:
#txt = "no se puede poner commlias dobles dentro de "commillas dobles""
txt1 = "si se puede poner commlias dobles dentro de 'commillas simples' o viceversa"

#Escape de caracteres con \(barra invertida) para poder usar comillas dobles dentro de otras comillas dobles
txt = "Si se puede poner commlias dobles dentro de \"commillas dobles\" con este método"
print(txt)

#Escape de caracteres con \(barra invertida) para saltar barras invertidas
txt = "mi carpeta donde guardo este archivo es C:\\Users\\Asus\\OneDrive\\Escritorio\\PROYECTO_PYTHON\\INTRODUCCION"
print(txt)

#Saltos de línea en cadena de caracteres(string): \n
txt = "Lo mejor que me paso en la vida es conocer a: \nJESÚS"
print(txt)

#MÉTODOS DE CADENA DE CARACTERES:
#Método 'title()'
txt = "con este método cada palabra del texto empieza en mayúscula"
print(txt.title())

#Método 'center()'
txt = "con este método la frase o texto queda centrado, dependiento cuanto espacio le demos"
print(txt.center(100))

#Método 'count()'
txt = "con este método cuenta las veces que se repite una palabra dentro del texto como palabra"
print(txt.count("palabra"))

#Método 'endswith()'
txt = "con este método nos devuelve true or false si la palabra está al final"
print(txt.endswith("palabra"))
print(txt.endswith("final"))

#Método 'find()'
txt = "con este método nos dice en que posición está la palabra según su índice inicial"
print(txt.endswith("palabra"))
print(txt.find("posición"))

#Método 'isdigit()'
txt = "con este método nos devuelve true or false si la cadena de caracteres son dígitos"
txt2 = "123456789"
print(txt.isdigit())
print(txt2.isdigit())

#Método 'islower()'
txt = "con este método nos devuelve true or false si todo el texto está en minúscula"
print(txt.islower())

#Método 'isupper()'
txt = "con este método nos devuelve true or false si todo el texto está en minúscula"
print(txt.isupper())

