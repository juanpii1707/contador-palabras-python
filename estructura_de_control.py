#ESTRUCTURA DE CONTROL: Es un bloqué de código que permite controlar el flujo de ejecución de un programa.
#Estos bloques de códigos determinan que instruccuiones se ejecutarán y en que orden.
#CONDICIONALES: Permiten ejecutar un cierto bloque de código sí se cumple una condición, en caso contrario se ejecutaotro bloque
#EXAMPLE:
# if condicion_1:   #se cumple
    #el código se ejecutará mientras la condición_1 sea verdadera
# elif condicion_2:
    #el código se ejecutará mientras la condición_2 sea verdadera
# else:
    #el código se ejecutará mientras la condicion_1 y condicion_2 no sean verdaderas
#En un bloqué de código no es necesario que este el if ---else, puede estar solo el if y el bloque de código se ejecutará
#--------------------------------------------------------------------------
#CONDICIONALES TERNARIAS: son una forma concisa de expresar una estructura condicional en una sola línea
#example:
#valor_si_condicion_verdadera if condicion else valor_si_condicion_falsa
x = 8
resultado = "positivo" if x > 5 else "negativo"
print(resultado)

#------------------------------------------------------------------
#BUCLES(LOOPS): Permiten ejecutar un cierto código repetidamente mientras se cumpla una condición o hasta que la condición se vuelva falsa.
 #BUCLE 'WHILE'

#while condicion:
    #Código se ejecutara sí la condición es verdadera

 #BUCLE 'FOR'

#for indice in range(cantidad):
    #Código se ejecutará en cada iteración
    
#-------------------------------------------------------------------------
#ESTRUCTURA DE CONTROL DE EXCEPCIONES: Permiten manejar errores y excepciones en un programa, controlando como se manejan los errores
# cuando ocurren en la ejecución de un programa

#try:
    #Código que puede generar una excepción
    
#except TipodeExcepcion as nombre_variable:
    #Código para manejar la excepción
    
#finally:
    #Código que siempre se ejecuta, Opcional
    
    
#---------------------------------------------------
#PALABRAS CLAVE PARA CONTROL DE FLUJO: Forman parte del conjunto de herramientas que python proporciona para controlar el flujo 
#de ejecución y la lógica del programa.

#BREAK
for i in range(5):
    if i == 3:
     break     #Se corta el programa
    print(i)   #Se espera: 0,1,2
    
    
#CONTINUE
for i in range(5):
    if i == 3:
     continue  #Hace un salto a la siguiente línea
    print(i)   #Se espera: 0,1,2,4
    
#PASS
x = 2
if x > 3:
  pass      #No hace nada, mientras se cumpla la condición
else:
    print("x es menor o igual a 3")   
    
#OTHERS: RETURN, RISE

#---------------------------------------------------------------------
#CONDITIONAL:
#if , elif, else:
#example:
x = 10

if x > 0:
    print("x is a positive number")
elif x < 0:
    print("x is a negative number")
else:
    print("x is equal to zero ")
    
#Quisieramos viajar a el mundo
visa = False
passport = True

if visa and passport:
    print("Puedes ingresar a cualquier país")
elif passport and not visa:
    print("Puedes ingresar a los paises que no requieran visa")
else: 
    print("Debes conseguir la documentación necesaria")
    
edad = 40
if edad < 18 or edad > 60:
    print("No puedes ingresar al boliche")
elif edad > 18 and edad < 60:
    print("Puedes ingresar al boliche") 
else:
    print("")

#----------------------------------------
#BUCLES(LOOPS)
#while(MIENTRAS .....SE CUMPLA UNA CONDICIÓN):
#EXAMPLE:
contador = 0
limite = 5
sumatoria = 0

while contador <= limite:
    sumatoria += contador
    print("El contador es:", contador)
    contador +=1                 #contador + 1 = contador/Esto lo hacemos para que no se repita en un bucle infinito de '0'

print("La suma de los números hasta:",limite,"es:",sumatoria) #El contador=5 no cumple, al ser el ultimo número que toma, lo imprime fuera del bucle como 5


#For(): recorre otras estructuras o rangos.
#EXAMPLE:
for i in range(5):      #Recorre los números desde 0 hasta 5 o range(número hasta, otro número)
    print(i)            #tomas todos los números pero no el último
    
for i in range(1,8):      #Recorre los números desde 1 hasta 8 o range(número hasta, otro número)
    print(i)            #tomas todos los números pero no el último
    
for i in range(0,8,2):      #Recorre los números desde 0 hasta 8, y el ultimo describe los saltos
    print(i)            #tomas todos los números pero no el último, los saltos son de dos en dos.
    
#Podemos combinar el bucle 'for' con los conditionals 'if':
for i in range(0,8,2):      #Recorre los números desde 0 hasta 8, y el ultimo describe los saltos
    if i == 4:
        print("pasó por el número 4")
    else:
        print("No es número 4, es:",i)            #tomas todos los números pero no el último, los saltos son de dos en dos.
    
#EXCEPCIONES:
#try, except, finally: manejo de errores.
#example: Manejo de la división por cero.
a = 8
b = 0
#c = a/b
#print(c)    #ZeroDivisionError: division by zero
resultado = 0
try:
    resultado = a/b
    print(resultado)
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    resultado = 0 #Límpia el resultado finalmente
    
print(resultado)   #Límpia el resultado

#PALABRAS CLAVE PARA EL CONTROL DE FLUJO:
#BREAK:
contador = 0
while contador < 8:
      print(contador)
      if contador == 5:
          break            #Lo que hace es salir del bucle, corta el flujo.
      contador += 1

#CONTINUE:
#EXAMPLE:      
while contador < 8:
      print(contador)
      contador += 1
      if contador == 5:
          continue            #Lo que hace es saltar el bucle if
      
print(contador)

for i in range(10):    #No incluye el 10
    if i % 2 == 0:
        continue
    print(i)
    
#PASS:
#EXAMPLE:
edad = 25
if edad > 18:
    print("Pueden entrar al BAR")
elif edad == 18:
    pass
else:
    print("No tienes la e dad suficiente")