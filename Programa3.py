# Hacer un progrma que lea 10 numeros y los almacene en un arreglo

a = [0,0,0,0,0,0,0,0,0,0]  # Español: Inicializa un arreglo con 10 ceros.  # English: Initialize an array with 10 zeros.

for i in range(0,10):  # Español: Bucle que se repite 10 veces (de 0 a 9).  # English: Loop that repeats 10 times (from 0 to 9).
    a[i] = int(input(f'Ingresa un numero \n'))  # Español: Solicita un número, convierte a entero y almacena en posición i.  # English: Prompt for a number, convert to integer and store at position i.

for i in a:  # Español: Itera sobre cada elemento del arreglo.  # English: Iterate over each element in the array.
    print(i)  # Español: Imprime el elemento actual.  # English: Print the current element.