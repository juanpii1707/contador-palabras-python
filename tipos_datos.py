# Tipos de Datos: Son datos que se asignan a una Variable y son:


# -------------------------------
# TEXTO
# ---------------------------------
#  -str :[Cadena de caracteres unicode(lleva simbolos y números)]
# example:
texto = "c@dena de caractere5"


# ----------------------------------
# NÚMERICOS:
# ----------------------------------
# - int(entero en inglés es integer)
# example:
numero_entero = 20

# - float(flotante)
# example:
numero_flotante = 5.789

# - complex(complejo)
# example:
numero_complejo = 5 + 4j


# ----------------------------------
# SECUENCIA:
# ----------------------------------

# - lists(lista)[coleción ordenada y mutable, puede contener texto u número]
# example:
lista = [4.5,6,"juan"]

# tuple(tupla)[coleción ordenada pero inmutable, puede contener texto u número]
# example:
tupla = (4,5,5,"jose")

# - range(rango)[Secuencia inmutable de números]
# example:
rango = range(0,10)

# ----------------------------------
# MAPPING TYPE:[Mapeo]
# ----------------------------------

# - dict(dicccionario, en inlgés 'dictionary')[Colección no ordenada de dos elementos pares llamados "clave-valor"]
# example:       clave :  valor
diccionario = {"nombre":"Juan pablo",
             "apellido":"Quispe Rojas",
                 "edad":34}


# ----------------------------------
# SET TYPES:(CONJUNTOS)
# ----------------------------------

# -set (conjunto) [Colección no ordenada y mutable de elementos únicos(no se puede repetir) ]
# example:
conjunto = {7,8,9,4,5,6} # No se repiten, y se puede mutar 

# - frozenset(conjunto inmutable, frozen es español es congelado)
# example:
conjunto_inmutable = frozenset({4,5,6,1,2,3})  # Es un conjunto inmutable y desordenado como el set

# ----------------------------------
# BOOLEAN TYPES:(BOOLEANO)
# ----------------------------------

# - boolean[puede ser verdadero o falso]
booleano = True
booleano2 = False

# ----------------------------------
# BINARY TYPES:(BINARIO)
# ----------------------------------

# - bytes[Representa una secuencia inmtable de bytes]
# example:
bytes_data = b"datos bytes"

# - bytearray(array de bytes) [Secuencia mutable de bytes]
# example:
bytes_array = bytearray(b"datos tipo bytes")

# - memoryview (vista de memoria)[Permite acceder a la memoria de objetos de bytes sin hacer una cópia]
# example:
memoria = memoryview(b"datos tipo bytes")

# ----------------------------------
# NONE/NULL:(NULO)
# ----------------------------------

# - Nonetype (nulo)[Representa la ausencia de valor o la no definición]
# example:
nulo = None
