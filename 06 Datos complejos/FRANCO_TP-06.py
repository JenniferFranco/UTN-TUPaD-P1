# Actividades
# # 1)
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# #agregrar nuevos par key-value
# precios_frutas['Naranja'] = 1200
# precios_frutas['Manzana'] = 1500
# precios_frutas['Pera'] = 2300

# print(precios_frutas)

# # 2) 

# #modificar valores de keys existentes
# precios_frutas['Banana'] = 1330
# precios_frutas['Manzana'] = 1700
# precios_frutas['Melón'] = 2800

# print(precios_frutas)

# # 3)
# #lista que contenga únicamente las frutas sin los  precios
# frutas = precios_frutas.keys()
# print(frutas)

# # 4) 

# #Crear diccinario vacio para almacenar los contactos 
# contactos = {} 

# #Cargar  contactos
# for i in range (3):
#     nombre = input('Ingrese el nombre del contacto: ')
#     numero = input('Ingrese el número del contacto: ')
#     contactos[nombre] = numero
    
# #Consultar por un contacto
# consulta = input('\nIngrese el nombre del contacto por el cual quiere consultar : ')  

# #Mostrar el resultado de la consulta

# if consulta in contactos:
#     print(f"El número de {consulta} es: {contactos[consulta]}")
# else:
#     print(f"No se encontró ningún contacto con el nombre {consulta}.")

## 5) 

# #se solicita la frase
# frases = input('Ingrese una frase: ')

# #se crea el conjunto con set() y se usa split() para separar por los espacios
# set_frase = set(frases.split())

# #se crea un diccionario vacio
# contador_palabra = {} 

# #se recorre cada palabra en la frase original no el set
# for palabra in frases.split():
#     #si la palabra ya esta en el contador se suma 1
#     if palabra in contador_palabra:
#         contador_palabra[palabra] += 1
#     else:
#         #si aparece por primera vez se le asigna 1
#         contador_palabra[palabra] = 1
    
# print("\nCantidad de veces que aparece cada palabra:")

# #.items() devuelve una lista de tuplas, cada una con una clave (palabra) y su valor (la cantidad de veces que aparece).
# # Al usar for palabra, cantidad, estamos desempaquetando la tupla en dos variables: palabra y cantidad.
# for palabra, cantidad in contador_palabra.items():
#     print(f"{palabra}: {cantidad}")

# 6)

# def promedio (a, b, c):
#     return (a + b + c)/3

# promedios = {} 

# for estudiante in range(3):
#     estudiante = input('Ingrese el nombre del estudiante: ')
#     a = float(input('Ingrese nota 1: '))
#     b = float(input('Ingrese nota 2: '))
#     c = float(input('Ingrese nota 3: '))
    
#     promedio_estudiante = promedio(a, b, c)
#     promedios[estudiante] = promedio_estudiante
    
# print(promedios)    
# # Mostramos los promedios
# print("\nPromedios de los estudiantes:")
# for estudiante, promedio in promedios.items():
#     print(f"{estudiante}: {promedio:.2f}")   
    
# 7)    
    
# def ingreso_notas(parcial_num):
#     aprobados = set () #conunto vacio
#     print(f"\nIngresá los nombres de quienes aprobaron el Parcial {parcial_num}. Escribí 'n' para terminar.")
#     while True:
#         estudiante = input("Nombre del estudiante: ").strip().lower()
#         if estudiante == 'n':
#             break
#         aprobados.add(estudiante)
#     return aprobados

# def analizar_notas(parcial1, parcial2):
     
#     ambos = parcial1 & parcial2
#     uno_solo = parcial1 ^ parcial2
#     al_menos_uno = parcial1 | parcial2
    
#     print ("\nAprobaron ambos parciales:", ambos)
#     print ("\nAprobaron un solo parcial:", uno_solo)
#     print ("\nAprobaron al menos un parcial:", al_menos_uno)

# #programa principal

# aprobados1 = ingreso_notas(1)
# aprobados2 = ingreso_notas(2)
# analizar_notas(aprobados1, aprobados2)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe

# def normalizar_nombre(nombre):
#     return nombre.strip().lower()

# def mostrar_cant_pro(lista, producto):
#     print(f"Hay {lista[producto]} unidades de {producto}.")

# def agregar_stock (lista):
   
#     if producto in lista:
#         print(f"Hay {producto.value} ")





# #programa principal

# stock_prod = { "remera": 10,
#                "camiseta": 5,
#                "campera": 20
#                }

#  producto = input("Ingrese el nombre del producto que quiere consultar: ")