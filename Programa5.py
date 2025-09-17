'''
Hacer un programa que lea 10 datos, si el dato es un numero se almacenara en un arreglo,
si es un caracter o caracteres se almacenara en una lista, 
cuando finalice el programa nos mostrara cuantos numericos y cuantos caracteres hay en cada estructura
'''

ar = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]  # Español: Inicializa un arreglo con 10 elementos establecidos en -1.  # English: Initialize an array with 10 elements set to -1.
lis = []  # Español: Crea una lista vacía para valores de cadena.  # English: Create an empty list for string values.
c = 0  # Español: Inicializa el contador para entradas totales.  # English: Initialize the counter for total inputs.
c2 = 0  # Español: Inicializa el contador para números válidos en el arreglo.  # English: Initialize the counter for valid numbers in the array.

while(True):  # Español: Inicia un bucle infinito.  # English: Start an infinite loop.
    a = input('Escribe un dato o valor ')  # Español: Solicita al usuario un valor.  # English: Prompt the user for input.
    if a.isdigit():  # Español: Verifica si la entrada es numérica.  # English: Check if input is numeric.
        ar[c] = int(a)  # Español: Convierte a entero y almacena en el arreglo.  # English: Convert to integer and store in array.
    elif a.isalpha():  # Español: Verifica si la entrada es alfabética.  # English: Check if input is alphabetic.
        lis.append(a)  # Español: Agrega la cadena a la lista.  # English: Add string to list.
    c += 1  # Español: Incrementa el contador de entradas.  # English: Increment input counter.
    if c >=10:  # Español: Verifica si se han recolectado 10 entradas.  # English: Check if 10 inputs have been collected.
        break  # Español: Sale del bucle.  # English: Exit loop.

print(f'La lista tiene {len(lis)}')  # Español: Muestra la cantidad de elementos de cadena.  # English: Display count of string elements.

for i in ar:  # Español: Itera a través del arreglo.  # English: Iterate through array.
    if i !=-1:  # Español: Verifica número válido (no -1).  # English: Check for valid number (not -1).
        c2 += 1  # Español: Cuenta números válidos.  # English: Count valid numbers.

print(f'El arreglo tiene {c2}')  # Español: Muestra la cantidad de elementos numéricos.  # English: Display count of numeric elements.
print(ar)  # Español: Imprime el arreglo.  # English: Print the array.
print(lis)  # Español: Imprime la lista.  # English: Print the list.


'''
for i in range(0,10):
    a = input('Escribe un numero: ')
    if a.isdigit():
        ar[i]=a
    if a.isalpha():
        lis.append(a)
'''