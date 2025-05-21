#1.Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esafunción para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

# def factorial (num):
#     return 1 if num == 0 else factorial(num-1)*num

# #programa principal
# num = int(input("Ingrese un numero: "))
# print(f"l factorial de todos los números enteros entre 1 y {num} es: {factorial(num)}")

#2.Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

# def serie_fibonacci (posicion ):
#     if posicion == 0:
#         return 0
#     elif posicion == 1:
#         return 1
#     else:
#         return serie_fibonacci(posicion-1) + serie_fibonacci(posicion-2)
    
# # programa principal 
# num =  int(input("Ingrese un numero: "))
# print(f'el valor de la serie de Fibonacci en la posición indicada: {serie_fibonacci(num)}')

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 

# def calcular_potencia(n,m):
#     if m == 0: #caso base (todo num elevado a 0 es 1) 
#         return 1
#     else:  
#         return n * (calcular_potencia(n, m-1))
    
# print(calcular_potencia(3,2))    
    
#4)Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto. 

#funcion para convertir numero decimal a binario
# def convertir_a_binario(num):
#     #caso base: si el num es 0 o 1, lo devolvemos como cadena
#     if num < 2:
#         return str(num)
#     else:
#         #num//2: calcula el cociente entero de dividir el número por 2.
#         #num%2: Calcula el resto de dividir el número entre 2 (siempre sera 0 o 1 )
#         #str(): Lo convertimos en string para poder concatenar
#         return convertir_a_binario(num//2) + str(num%2)

# #programa principal
# num_decimal = int(input('Ingrese un numero decimal: '))
# print(f'El número {num_decimal} en binario es: {convertir_a_binario(num_decimal)}')


# 5)   Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().    

#Un palíndromo es una palabra, número, frase o secuencia de caracteres que se lee igual hacia adelante que hacia atrás, ignorando espacios, signos de puntuación y mayúsculas/minúsculas 

# def norm_texto(palabra):
#     palabra = palabra.lower()
#     palabra = palabra.replace(" ","")
    

# def es_palindromo(palabra):
    

#6)   Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.    

# def suma_digitos(num):
#     if num < 10: #CASO BASE: Cuando  num es menor que 10 solo tiene un digito por lo que devuelve el mismo num 
#         return num
#     else:
#         #Con num%10: se obtiene el ultimo digito (el cual se suma) 
#         #Con num//10: devuelve el número sin ese último dígito, sin decimales
#         return suma_digitos(num//10) + (num%10) 
    
# print(suma_digitos(305))   

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.


# def contar_bloques(n):
#     if n == 1: #CASO BASE
#         return 1
#     elif n == 0: #CASO BASE
#         return 0
#     else:
#         return  n +contar_bloques(n-1)
    
# print(contar_bloques(2))    

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

# def contar_digito(numero, digito):
#     if numero == 0: # Caso base: cuando ya no hay más dígitos
#         return 0
#     else:
#         ultimo_digito = numero%10
#         if ultimo_digito == digito:
#             return 1 + contar_digito(numero//10, digito) #sumamos 1 y llamamos nuevamnete a la funcion
#         else:
#             return contar_digito(numero//10, digito) # si no es igual no sumamos, solo llamamos a la funcion.
        
# print(contar_digito(5,5))        