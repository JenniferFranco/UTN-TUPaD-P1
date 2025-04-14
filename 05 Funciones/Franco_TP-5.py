#Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

# def imprimir_mensaje (mensaje):
#     print(mensaje);

# #programa principal
# imprimir_mensaje ('Hola Mundo!');

# Crear  una  función  llamada  saludar_usuario(nombre)  que  reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de- volver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

# def saludar_usuario (nombre):
#     print(f'Hola {nombre}!');

# #programa principal
# nombre = input('Ingrese su nombre:')
# saludar_usuario(nombre);

# Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe- dir los datos al usuario y llamar a esta función con los valores in- gresados.

# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}');

# #programa principal
# #defino variables
# nombre = input('Ingrese su nombre: ');
# apellido = input('Ingrese su apellido: ');
# edad = int(input('Ingrese su edad: '));
# residencia = input('Ingrese su residencia: ');

# informacion_personal(nombre, apellido, edad, residencia);

# Crear dos funciones: calcular_area_circulo(radio) que reciba el ra- dio como parámetro y devuelva el área del círculo. calcular_peri- metro_circulo(radio) que reciba el radio como parámetro y devuel- va el perímetro del círculo. Solicitar el radio al usuario y llamar am- bas funciones para mostrar los resultados.

# import math;

# def calcular_area_circulo(r):
#     return math.pi * (r)**2;  

# def calcular_perimetro_circulo(r):
#     return 2 * math.pi * r;

# def imprimir_valores (r):
#     area = calcular_area_circulo(r);
#     perimetro = calcular_perimetro_circulo(r);
#     print (f'El area es: {area:.2f} y el perimetro es: {perimetro:.2f}') 

# #programa principal
# radio = int(input('Ingrese el radio del círculo: '));
# imprimir_valores(radio);

# Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mos- trar el resultado usando esta función.

# def validar_numero (mensaje, min= float('-Inf'), max= float('Inf')):
#     numero = float(input((f'{mensaje} ')));
#     while numero < min or numero > max:
#         numero = float(input((f'ERROR. {mensaje} ')));
#     return numero;    

# def segundos_a_horas(segundos):
#     cantidad_horas = round(segundos / 3600, 2);
#     print(cantidad_horas);
    
# #programa principal
# segundos = validar_numero('Ingrese la cantidad de segundos: ', 1);
# segundos_a_horas(segundos);

# Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

# def validar_numero (mensaje, min= float('-Inf'), max= float('Inf')):
#     numero = float(input((f'{mensaje} ')));
#     while numero < min or numero > max:
#         numero = float(input((f'ERROR. {mensaje} ')));
#     return numero;  

# def tabla_multiplicar(numero):
#     print(f"\nTabla de multiplicar del {numero}:\n")
#     for i in range (11): # del 0 al 10
#         numero_multiplicado = numero*i
#         print(f'{numero} x {i} = {numero_multiplicado}')

# #programa principal
# num = validar_numero('Ingrese un número: ', 1 );
# tabla_multiplicar(num);

# Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resulta- do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re- sultados de forma clara.

# def suma_numeros (a, b):
#     return a + b;

# def resta_numeros (a, b):
#     return a - b;

# def multiplicacion_numeros (a, b):
#     return a * b;

# def division_numeros (a, b):
#     return a / b if b != 0 else 'No se puede dividir por cero'; #si b es 0

# def operaciones_basicas(a, b):
#     resultado_suma = suma_numeros(a,b);
#     resultado_resta = resta_numeros(a,b);
#     resultado_division = division_numeros(a,b);
#     resultado_multiplicacion = multiplicacion_numeros(a,b);
#     return (resultado_suma, resultado_resta, resultado_multiplicacion, resultado_division)

# #programa principal
# num1 = int(input('Ingrese el primer número: '));
# num2 = int(input('Ingrese el segundo número: '));

# resultados = operaciones_basicas(num1, num2);

# print("Resultados:")
# print(f"Suma: {resultados[0]}")
# print(f"Resta: {resultados[1]}")
# print(f"Multiplicación: {resultados[2]}")
# print(f"División: {resultados[3]}")

# Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun- ción para mostrar el resultado con dos decimales.

# def validar_numero (mensaje, min= float('-Inf'), max= float('Inf')):
#     numero = float(input((f'{mensaje} ')));
#     while numero < min or numero > max:
#         numero = float(input((f'ERROR. {mensaje} ')));
#     return numero;  

# def calcular_imc(peso, altura):
#     imc = round(peso / (altura**2), 2);
#     print(f"Su IMC es de: {imc}.")

# #programa principal
# peso = validar_numero('Ingrese su peso en kilogramos: ', 1);
# altura = validar_numero('Ingrese su altura metros: ', 0.5);

# calcular_imc(peso, altura);

# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

# def validar_numero (mensaje, min= float('-Inf'), max= float('Inf')):
#     numero = float(input((f'{mensaje} ')));
#     while numero < min or numero > max:
#         numero = float(input((f'ERROR. {mensaje} ')));
#     return numero;  

# def celsius_a_fahrenheit(celsius):
#     temp_fahrenheit = round((9/5)*celsius+32, 2)
#     print(f"{celsius} °C equivalen a {temp_fahrenheit} °F.")

# #programa principal
# temp_celsius = validar_numero('Ingrese una temperatura en grados Celsius: ');
# celsius_a_fahrenheit(temp_celsius);

# Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

# def validar_numero (mensaje, min= float('-Inf'), max= float('Inf')):
#     numero = float(input((f'{mensaje} ')));
#     while numero < min or numero > max:
#         numero = float(input((f'ERROR. {mensaje} ')));
#     return numero;  

# def suma_numeros (a, b, c):
#     return a + b + c;

# def calcular_promedio(a, b, c):
#     total_notas = suma_numeros(a, b, c) / 3
#     print (f'El promedio es {total_notas}');

# #programa principal
# nota1 = validar_numero('Ingrese una nota: ', 1, 10);
# nota2 = validar_numero('Ingrese una nota: ', 1, 10);
# nota3 = validar_numero('Ingrese una nota: ', 1, 10);

# calcular_promedio(nota1, nota2, nota3);

