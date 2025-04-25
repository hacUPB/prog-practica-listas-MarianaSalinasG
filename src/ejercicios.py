# Ejercicio 1: Suma de elementos en una lista de listas
def suma_matriz(matriz):
    fil = len(matriz) #La filas son cuantas listas hay dentro de la matriz
    col = len(matriz[0]) #La columnas son cuantas entradas hay dentro de una lista.
    contador = 0
    for i in range(fil):
        for j in range(col):
            contador += matriz[i][j]
    return contador

# Ejercicio 2: Encontrar el valor máximo en una matriz
def maximo_matriz(matriz):
    fil = len(matriz) #La filas son cuantas listas hay dentro de la matriz
    col = len(matriz[0]) #La columnas son cuantas entradas hay dentro de una lista.
    max = None
    for i in range(fil):
        for j in range(col):
            valor = matriz[i][j]
            if max == None or valor > max:
                max = valor
    return max

# Ejercicio 3: Verificar si un número es primo
def es_primo(n):    
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Ejercicio 4: Transponer una matriz
def transponer_matriz(matriz):
    traspuesta = []
    for i in range(len(matriz[0])): 
       nueva_fila = []
       for j in range(len(matriz)):
            nueva_fila.append(matriz[j][i])
       traspuesta.append(nueva_fila)
    return traspuesta

# Ejercicio 5: Filtrar números pares
def filtrar_pares(lista):
   pares = []
   for numero in lista:
       if numero % 2 == 0:
           pares.append(numero)
   return pares

# Ejercicio 6: Contar la cantidad de palabras en una frase
def contar_palabras(frase):
    palabras = frase.split()
    return len(palabras)

# Ejercicio 7: Crear una tabla de multiplicar
def tabla_multiplicar(n):
    tabla_multiplicar = []
    for i in range(1, 11):
        tabla_multiplicar.append(n*i)
    return tabla_multiplicar

# Ejercicio 8: Contar números negativos en una lista
def contar_negativos(lista):
    contador = 0
    for numero in lista:
        if numero < 0:
            contador += 1
    return contador

# Ejercicio 9: Determinar si una lista está ordenada
def lista_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

# Ejercicio 10: Cifrar un texto con el cifrado César
def cifrado_cesar(texto, desplazamiento):
    cifrado = ""
    for char in texto:
        if char.isalpha():
            desplazamiento_base = ord('A') if char.isupper() else ord('a')
            nuevo_char = chr((ord(char) - desplazamiento_base + desplazamiento) % 26 + desplazamiento_base)
            cifrado += nuevo_char
        else:   
            cifrado += char
    return cifrado

#Aquí comienza el progrma principal. No modifiques el código debajo de esta línea.
def main():
    pass


if __name__ == "__main__":
    main()