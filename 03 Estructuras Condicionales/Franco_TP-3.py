# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# edad = int(input('Ingrese su edad, por favor.'));
# if edad >= 18: 
#     print('Es mayor de edad');
# else: #si ingresa un numero menor de 18
#     print('Es menor de edad'); 

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”

# nota = float(input('Ingrese su nota, por favor.'));
# if nota >= 6:
#     print('Aprobado');
# else:
#     print('Desaprobado');

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar

# numero = int(input('Ingrese un número par, por favor'));
# if numero % 2 == 0:
#     print('Ha ingresado un número par.');
# else: 
#     print('Por favor, ingrese un número par.');    

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ●   Niño/a: menor de 12 años.
# ●   Adolescente: mayor o igual que 12 años y menor que 18 años. ●   Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ●   Adulto/a: mayor o igual que 30 años.

# edad = int(input('Ingrese su edad, por favor.'));
# if edad < 12:
#     print('Es niño/a.');
# elif edad >= 12 and edad < 18:
#     print('Es adolescente.');
# elif edad >= 18 and edad < 30:
#     print('Es adulto/a joven.');
# elif edad >= 30:
#     print('Es adulto.');

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

# password = input('Ingrese una contraseña entre 8 y 14 caracteres, por favor.');
# longitud_password = len (password);
# if longitud_password >= 8 and longitud_password <=14:
#     print('Ha ingresado una contraseña correcta');
# else:
#     print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres');

# 6)escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

# from statistics import mode, median, mean;
# import random;

# numeros_aleatorios = [random.randint(1, 100) for i in range(50)];

# moda_lista = mode(numeros_aleatorios);
# mediana_lista = median(numeros_aleatorios);
# media_lista = mean(numeros_aleatorios);

# #se muestra los numeros de la lista
# print (numeros_aleatorios);
# #se muestran los valores de la media, mediana y la moda
# print(f'La media de la lista es {media_lista}');
# print(f'La mediana de la lista es {mediana_lista}');
# print(f'La moda de la lista es {moda_lista}');

# #se analiza el sesgo
# if media_lista > mediana_lista and mediana_lista > moda_lista:
#     print('Hay sesgo positivo');
# elif media_lista < mediana_lista and mediana_lista < moda_lista:
#     print('Hay sesgo negativo');
# elif media_lista == mediana_lista and media_lista == moda_lista and mediana_lista == moda_lista:
#     print('No hay sesgo');
# else:
#     print('No se cumple las condiciones de sesgo');

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# mensaje = input('Ingrese una palabra o frase, por favor');

# #defino las vocales
# vocales = 'aeiouAEIoU';

# #analizo si el ultimo caracter contiene vocales
# if mensaje[-1] in vocales:
#     print(f'{mensaje}!');
# else:
#     print(mensaje); 

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1.   Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2.   Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3.   Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.

# nombre = input('Ingrese su nombre, por favor. ');
# opcion = int(input('''Elija una opcion: \n 1.Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. \n 2.Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n 3.Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.'''));

# if opcion == 1:
#     print(nombre.upper());
# elif opcion == 2:
#     print(nombre.lower());
# elif opcion == 3:
#     print(nombre.title());
# else:
#     print('Seleccine una opcion valida, por favor.');  

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ●   Menor que 3: "Muy leve" (imperceptible).
# ●   Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible).
# ●   Mayor  o  igual  que  4    y  menor  que  5:  "Moderado"  (sentido  por personas, pero generalmente no causa daños).
# ●   Mayor o igual que 5   y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ●   Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). ●   Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# magnitud_terremoto = int(input('Ingrrese la magnitud del terremoto, por favor.'));

# if magnitud_terremoto < 3:
#     print('"Muy leve" (imperceptible)');
# elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
#     print('"Leve" (ligeramente perceptible).');
# elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
#     print('"Moderado" (sentido  por personas, pero generalmente no causa daños).');
# elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
#     print('"Fuerte" (puede causar daños en estructuras débiles).');
# elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
#     print('"Muy Fuerte" (puede causar daños significativos).');
# elif magnitud_terremoto >= 7:
#     print('"Extremo" (puede causar graves daños a gran escala)');
# else:
#     print('Por favor, ingrese un número.');

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

# hemisferio = input('¿En qué hemisferio se encuentra (N/S)?: ');
# mes = int(input ('¿Qué mes del año es? (ingrese un número del 1 al 12): '));
# dia = int(input('¿Qué día es? '));

# invierno = mes

# if hemisferio == 'N' or hemisferio == 'n':
#     if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes <= 3 and dia <=20):
#         print('Se encuentra en invierno');
#     elif (mes >= 3 and dia >=21) or (4 <= mes <= 5) or (mes <= 6 and dia <=20):
#         print('Se encuentra en primavera');
#     elif (mes >= 6 and dia >=21) or (7 <= mes <= 8) or (mes<=9 and dia <=20):
#         print('Se encuentra en otoño');
#     elif (mes >= 9 and dia >=21) or (10 <= mes <= 11) or (mes ==12 and dia <=20):
#         print('Se encuentra en verano');
#     else:
#             print('Ingrese una fecha correcta.')   

# elif hemisferio == 'S' or hemisferio == 's':
#     if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes <= 3 and dia <=20):
#         print('Se encuentra en verano');
#     elif (mes >= 3 and dia >=21) or (4 <= mes <= 5) or (mes <= 6 and dia <=20):
#         print('Se encuentra en otoño');
#     elif (mes >= 6 and dia >=21) or (7 <= mes <= 8) or (mes<=9 and dia <=20):
#         print('Se encuentra en primavera');
#     elif (mes >= 9 and dia >=21) or (10 <= mes <= 11) or (mes ==12 and dia <=20):
#         print('Se encuentra en invierno'); 
#     else:
#         print('Ingrese una fecha correcta.');
        
# else:
#     print('Ingrese un hemisferio valido.')
              
        
        
                       