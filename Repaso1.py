# Instrucciones de entrada y salida
# print() o print(f)
#print('Hola Mundo')
#print(f'Hola mundo numeros {10}')
# Entrada de datos
#input('Escribe un numero') # se introducen solo letras
# casting para convertir a valores especificos
#f = 0.0
#f = float(input('Escribe un numero con decimales'))
#a = 0
#a = int(input('Escribe un numero con decimales'))
#c = 120
#print(str(c))
#v = ""
#v = str(c)
#NOTA: solo las variables que no se introducen por teclado se obliga a inicializarlas

'''
Hacer un programa que lea nombre y precio de un producto, el programa calculara el costo y precio de venta
El costo involucra el 12% y IVA 16%
'''

# for i in range(1,5): #rango valor inicial hasta valor final sin incluirlo

while(True):  # Español: Inicia un bucle infinito que repetirá el bloque hasta encontrar un break.  # English: Start an infinite loop that repeats the block until a break is found.
    n = input('Escribe el nombre de tu producto: ')  # Español: Lee el nombre del producto como cadena y lo guarda en `n`.  # English: Read the product name as a string and store it in `n`.
    p = float(input('Escribe el precio del producto: '))  # Español: Lee el precio (texto) y lo convierte a float, luego lo asigna a `p`.  # English: Read the price (text), convert it to float, then assign it to `p`.
    c = p * 1.12  # Español: Calcula el costo aplicando un 12% (c = p * 1.12).  # English: Calculate the cost applying 12% (c = p * 1.12).
    pv = c * 1.16  # Español: Calcula el precio de venta aplicando IVA del 16% sobre el costo (pv = c * 1.16).  # English: Calculate the selling price applying 16% VAT on the cost (pv = c * 1.16).
    print(f'El costo es: {c:.2f}')  # Español: Imprime el costo con 2 decimales.  # English: Print the cost with 2 decimal places.
    print(f'El precio de venta es: {pv:.2f}')  # Español: Imprime el precio de venta con 2 decimales.  # English: Print the selling price with 2 decimal places.

    res = input('Deseas otro numero (s/n) \n')  # Español: Pregunta si desea procesar otro producto; guarda la respuesta en `res`.  # English: Ask if the user wants to process another product; store the response in `res`.
    if res == 'n' or res == 'N':  # Español: Si la respuesta es 'n' o 'N', se sale del bucle.  # English: If the response is 'n' or 'N', exit the loop.
        break  # Español: Rompe el while y termina el programa.  # English: Break the while and end the program.
