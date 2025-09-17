'''
Hacer un programa que lea 10 datos, si el dato es un numero se almacenara en un arreglo,
si es un caracter o caracteres se almacenara en una lista, 
cuando finalice el programa nos mostrara cuantos numericos y cuantos caracteres hay en cada estructura
'''
arreglo = [0,0,0,0,0,0,0,0,0,0]  # Español: Inicializa un arreglo con 10 ceros.  # English: Initialize an array with 10 zeros.
lista = []  # Español: Inicializa una lista vacía.  # English: Initialize an empty list.
cn = 0  # Español: Inicializa contador para números.  # English: Initialize counter for numbers.
cc = 0  # Español: Inicializa contador para caracteres.  # English: Initialize counter for characters.

for i in range(0,10):  # Español: Bucle que se repite 10 veces.  # English: Loop that repeats 10 times.

    d = input('Escribe un dato: ')  # Español: Solicita al usuario un dato.  # English: Prompt user for data.
    if d.isdigit():  # Español: Verifica si el dato es numérico.  # English: Check if data is numeric.
        arreglo[i] = d  # Español: Almacena el número en el arreglo.  # English: Store number in array.
        cn += 1  # Español: Incrementa contador de números.  # English: Increment number counter.
    elif d.isalpha():  # Español: Verifica si el dato es alfabético.  # English: Check if data is alphabetic.
        lista.append(d)  # Español: Agrega caracteres a la lista.  # English: Add characters to list.
        cc += 1  # Español: Incrementa contador de caracteres.  # English: Increment character counter.

print(f'El arreglo tiene: {cn}\nLa lista tiene: {cc}')  # Español: Muestra cantidad de números y caracteres.  # English: Show count of numbers and characters.
print(arreglo)  # Español: Imprime el arreglo.  # English: Print the array.
print(lista)  # Español: Imprime la lista.  # English: Print the list.