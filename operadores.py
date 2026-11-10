#OPERADORES: SON SIMBOLOS O CONJUNTO DE SIMBOLOS QUE REALIZAN UNA OPERACIÓN ESPECÍFICA CON UNO Ó MÁS OPERADORES

#Tipos de operadores:

#Aritméticos: '+', '-', '*' and '/'.

a = 7
b = 4
c = a + b
print(c)
print(type(c))

a = 7
b = 4
c = a / b
print(c)
print(type(c))             #Return un float uppon division two integer
# If i want that return an integer; i use floor division [//] and for rest- module[%]
a = 7
b = 4
c = a // b  # for division integer, return only integer
d = a % b   # for division integer, return fraction or rest
print(c)
print(d)

#exponenciación
a = 2
b = 4
c = a ** b
print(c)

#--------------------------------------------------------------------------------
#De operación


#--------------------------------------------------------------------------------
#De asignación: '=',
a = "es el igual a"

x = 5
x = 8
# 'x' toma el ultimo valor
#Sumatorio: a un número base se le va sumando los valores que le asignemos
x = 9
sumatorio = 3
x += sumatorio    #x = x + sumatorio
print(x)


#--------------------------------------------------------------------------------
#De Comparación: '=='(no es lo mismo que '=') muestra equivalencia, '!=' muestra si son distintos, '<', '>','<=' and '>='
x = 5
y = 6
print(x==y)   #compara las dos variables sí son iguales

x = 5
y = 6
print(x!=y)   #compara las dos variables sí son distintos

x = 5
y = 6
print(x < y)   #compara si la variable de la izquierda es mayor al de la derecha

#--------------------------------------------------------------------------------
#Lógicos: 'and', 'or', 'not'

x = 5
booleano = x > 7 and x < 10
print(booleano)

booleano = x > 7 or x < 10
print(booleano)

booleano = not x !=0
print(booleano)

#--------------------------------------------------------------------------------
#De Identidad: 'is', 'is not'
a = 5
b = 5
booleano = a is b
print(booleano)

a = 5
b = 5
booleano = a is not b
print(booleano)

#--------------------------------------------------------------------------------
#De pertenencia: 'in', 'not in'.
a = "banana,fresa, naranja, mandarina, lucuma"
print("banana" in a)
print("palta" not in a)
#Tnener cuidado con las mayúsculas y minúsculas en un texto, por que son casesensitive, para solucionarlo:
a = "banana,fresa, naranja, mandarina, lucuma"
aminúsculas = a.lower()
abuscar = "banana".lower().strip()      #lower para que lo buscque en mínuscula y strip para los espacios
print(abuscar in aminúsculas)