# Hacer un programa que lea 10 numeros y los almacene en una lista

a = []  # Español: Crea una lista vacía para almacenar números.  # English: Create an empty list to store numbers.
s = 0  # Español: Inicializa la variable para la suma de números.  # English: Initialize variable for sum of numbers.
n = 0  # Español: Inicializa el contador de números válidos.  # English: Initialize counter for valid numbers.
numeros = "0,1,2,3,4,5,6,7,8,9"  # Español: Define los caracteres numéricos permitidos.  # English: Define allowed numeric characters.

while(n < 10):  # Español: Bucle mientras no se hayan recolectado 10 números.  # English: Loop until 10 numbers are collected.
    b = input('Escribe un numero: ')  # Español: Solicita al usuario un número.  # English: Prompt user for a number.
    x = 0  # Español: Inicializa contador de dígitos válidos.  # English: Initialize counter for valid digits.
    for i in b:  # Español: Itera sobre cada carácter de la entrada.  # English: Iterate over each character in input.
        #if (ord(i) >=48 and ord (i)<=57): #El ord se utiliza para obtener el valor ASCII 
            #he ord function is used to get the ASCII value
        if i in numeros:  # Español: Verifica si el carácter es numérico.  # English: Check if character is numeric.
            x += 1  # Español: Incrementa contador de dígitos válidos.  # English: Increment valid digit counter.
    if len(b) == x:  # Español: Verifica si todos los caracteres son numéricos.  # English: Check if all characters are numeric.
        a.append(int(b))  # Español: Convierte a entero y añade a la lista.  # English: Convert to integer and add to list.
        n += 1  # Español: Incrementa contador de números válidos.  # English: Increment valid number counter.
    else:  # Español: Maneja entrada no válida.  # English: Handle invalid input.
        print('El valor no es numero')  # Español: Mensaje de error.  # English: Error message.
        

for i in a:  # Español: Itera sobre cada número en la lista.  # English: Iterate over each number in list.
    print(i)  # Español: Imprime el número.  # English: Print the number.
    s += i  # Español: Suma el número al total.  # English: Add number to total.

print(f'La suma es: {s}')  # Español: Muestra la suma total.  # English: Display total sum.