'''
Hacer un programa que lea una cadena y que muestre en pantalla cuantos numeros tiene, cuantas mayusculas, cuantas minusculas
y cuantos espacios 
'''
def inicio():
    n=0  # Español: Inicializa el contador de números en 0.  # English: Initialize the numbers counter to 0.
    e=0  # Español: Inicializa el contador de espacios en 0.  # English: Initialize the spaces counter to 0.
    min=0  # Español: Inicializa el contador de minúsculas en 0.  # English: Initialize the lowercase counter to 0.
    may=0  # Español: Inicializa el contador de mayúsculas en 0.  # English: Initialize the uppercase counter to 0.
    numeros = "0123456789"  # Español: Cadena con todos los dígitos usada para comprobaciones.  # English: String with all digits used for checks.
    cadena = input('Escribe una cadena ')  # Español: Solicita una cadena al usuario y la guarda en 'cadena'.  # English: Prompt the user for a string and store it in 'cadena'.
    for i in cadena:  # Español: Recorre cada carácter de la cadena.  # English: Iterate over each character in the string.
        if i in numeros:  # Español: Comprueba si el carácter es un dígito (está en 'numeros').  # English: Check if the character is a digit (is in 'numeros').
            print('Es numero')  # Español: Imprime que el carácter es un número.  # English: Print that the character is a number.
            n+=1  # Español: Incrementa el contador de números.  # English: Increment the numbers counter.
        if i == ' ':  # Español: Comprueba si el carácter es un espacio.  # English: Check if the character is a space.
            e+=1  # Español: Incrementa el contador de espacios.  # English: Increment the spaces counter.
        if ord(i)>=97 and ord(i)<=122:  # Español: Comprueba si el carácter es una minúscula según su código ASCII.  # English: Check if the character is a lowercase letter by its ASCII code.
            min+=1  # Español: Incrementa el contador de minúsculas.  # English: Increment the lowercase counter.
        if ord(i)>=65 and ord(i)<=90:  # Español: Comprueba si el carácter es una mayúscula según su código ASCII.  # English: Check if the character is an uppercase letter by its ASCII code.
            may+=1  # Español: Incrementa el contador de mayúsculas.  # English: Increment the uppercase counter.
    print(f'Los numeros son: {n} \nLos espacios son: {e} \nLas minusculas son: {min} \nLas mayusculas son: {may}')  # Español: Muestra en pantalla los cuatro conteos formateados.  # English: Display the four counts formatted on screen.



if __name__=='__main__':
    inicio()  # Español: Llama a la función inicio para ejecutar el programa si el archivo se ejecuta directamente.  # English: Call the inicio function to run the program if the file is executed directly.