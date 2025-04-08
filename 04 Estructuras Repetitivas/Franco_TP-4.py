# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# for i in range (0, 101):
#     print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

# num = int(input('Ingrese un número entero: '));

# #abs para asegurarnos que acepte numeros negativos (lo transforma a su valor absluto)
# #str para transformar en string
# #len para contabilizar los caracteres
# cant_digitos= len(str(abs(num)));
# print(f'El número {num} contiene {cant_digitos} digitos');

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# num1 = int(input('Ingrese el primer número entero: '));
# num2 = int(input('Ingrese el segundo número entero: '));

# #variable para almacenar la sumatoria
# suma = 0;

# for i in range (num1+1, num2 ):
#     suma += i;

# print(f'La suma de los números entre {num1} y {num2}, excluyendo estos dos, es: {suma}');

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

# #variable para almacenar la sumatoria
# suma = 0;
# num = int(input('Ingrese un número entero: '));

# while (num != 0):
#     suma += num;
#     num = int(input('Ingrese un número entero (0 para detenerse): '));

# print(f'El total es: {suma}');    
    
# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.   

# import random;

# print('Adivine el número secreto')
# #genero numero aleatorio entre 0 y 9 (ambos incluidos)
# num_aleatorio = random.randint(0,9)
# num_usuario = int(input('Ingrese un número entre 0 y 9:'))
# intentos = 1; #inicializo intentos

# while num_aleatorio != num_usuario:
#     if (num_usuario > num_aleatorio):
#         print('Ingrese un número menor');
#     else:
#         print('Ingrese un número mayor');
        
# # Incremento los intentos y pido un nuevo número
#     intentos += 1
#     num_usuario = int(input('Ingrese un número entre 0 y 9: '))

# # Cuando el usuario adivina el número, se imprime el mensaje de éxito
# print(f'¡Acertaste! El número era {num_aleatorio}. Lo hiciste en {intentos} intentos.')

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# #coloco -2 para que descresca
# for i in range (100, -1, -2):
#     print(i);

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

# suma = 0;
# num = int(input('Ingrese un número entero: '));

# #nos asegruramos que el numero sea positivo
# if num > 0 :
#     for i in range(1, num+1):
#         suma += i;
#     print(f'La suma de todos los números entre 0 y {num} es: {suma}');
    
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).    

# es_par = 0;
# es_impar = 0;
# es_positivo = 0;
# es_negativo = 0;

# for i in range(1,101):
#     num = int(input(f'Ingrese un número entero {i}: '));
    
#     if num > 0:
#         es_positivo += 1;
#     elif num < 0:
#         es_negativo += 1;
        
#     if num % 2 == 0:
#         es_par += 1;
#     else:
#         es_impar += 1;1

# #se muestran los resultados        
# print(f'Números pares: {es_par}');
# print(f'Números impares: {es_impar}');
# print(f'Números positivos: {es_positivo}');
# print(f'Números negativos: {es_negativo}');      
        
# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).      

# from statistics import mean;

# #lista vacia para almacenar los numeros
# lista_numeros = [];

# for i in range(1,101):
#     num = int(input(f'Ingrese un número entero {i}: '));
#     lista_numeros.append(num); #agrego los numeros a la lista
   
# print(mean(lista_numeros));

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# # Solicitamos un número y lo dejamos como string para poder invertirlo  
# numero = input("Ingrese un número: ");

# # Invertimos usando slicing
# numero_invertido = numero[::-1]; #-1 para que recorra a la inversa

# print(f"El número invertido es: {numero_invertido}")
