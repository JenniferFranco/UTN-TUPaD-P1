#Instrucciones:
# 1. Analiza cada algoritmo y determina su orden de complejidad T(n) y O(n).
# 2. Justifica tu respuesta indicando los pasos relevantes en el análisis.
# 3. En los ejercicios 1 y 2, compara ambas soluciones y argumenta cuál es más eficiente.

# Ejercicio 1: Suma de los primeros n números
def suma_numeros(n):
    suma = 0 #T(n)=1                   
    for i in range(1, n + 1): #T(n)= 2*n
        suma += i #T(n)= 2
    return suma #T(n)= 1

#Pregunta: ¿Cuál es el orden de complejidad de esta función? Explica tu respuesta.
#T(n)= 2 + 2*n
#O(n) = n

# Ejercicio 2: Suma de los primeros n números
def suma_numeros_formula(n):
    return (n * (n + 1)) // 2 #T(n)= 1 + 1 + 1 + 1 = 4

# Pregunta: ¿Cuál es el orden de complejidad de esta función? ¿Cuál de las dos soluciones (Ejercicio 1 o 2) es más eficiente? Explica por qué.
#T(n)=4
#O(n) = 4
# Esta funcin es lineal, es mas eficiente  porque su tiempo de ejecución no depende de n.Mientras que la primera función se vuelve más lenta cuanto más grande es n, la segunda es igual de rápida siempre.

# Ejercicio 3: Búsqueda de un elemento en una lista desordenada
def buscar_elemento(lista, objetivo):
    for elemento in lista:  #T(n)=   2*n
        if elemento == objetivo: #T(n)= 1
            return True #T(n)= 1
    return False #T(n)= 1

# Pregunta: Determina el peor caso y la complejidad temporal de este algoritmo. El peor caso es T(n)= 2n + 1 cuando no se encuentra elemento en la lista
#T(n)= 2n + 1
#O(n)= n 


# Ejercicio 4: Encontrar el número máximo en una lista
def encontrar_maximo(lista):
    maximo = lista[0] #T(n)= 1
    for elemento in lista: #T(n)=    2*n
        if elemento > maximo: #T(n)= 1
            maximo = elemento #T(n)= 1
    return maximo #T(n)= 1

# Pregunta: ¿Cuál es el orden de complejidad de este algoritmo?
#T(n)= 2n + 2
#O(n)= n 


# Ejercicio 5: Ordenamiento por selección
def ordenamiento_seleccion(lista):
    n = len(lista) #T(n)= 1
    for i in range(n):#T(n)=     *n
        min_idx = i #T(n)= 1
        for j in range(i + 1, n): #T(n)=  *n
            if lista[j] < lista[min_idx]: #T(n)= 1
                min_idx = j #T(n)= 1
        lista[i], lista[min_idx] = lista[min_idx], lista[i] #T(n)= 1
    return lista #T(n)= 1

# Pregunta: Determina la complejidad temporal de este algoritmo y explica su comportamiento en el peor caso.
#T(n)=
#O(n)= n^2 

#El peor caso sucede cuando el arreglo está en orden totalmente inverso o en un orden tal que cada vez que buscas el mínimo, debes recorrer casi toda la lista para encontrarlo.