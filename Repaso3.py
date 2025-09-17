def validar(a):
    # Español: Define la función 'validar' que recibe el parámetro 'a'.
    # English: Define the function 'validar' that receives the parameter 'a'.
    c = 0
    # Español: Inicializa la variable entera 'c' con 0.
    # English: Initialize the integer variable 'c' to 0.
    d = 0.0
    # Español: Inicializa la variable decimal 'd' con 0.0.
    # English: Initialize the float variable 'd' to 0.0.
    try:
        # Español: Intenta ejecutar el bloque que sigue (intentar conversión a entero).
        # English: Try to execute the following block (attempt conversion to int).
        c = int(a)
        # Español: Convierte 'a' a entero y lo asigna a 'c'.
        # English: Convert 'a' to an integer and assign it to 'c'.
        print('Es un valor numerico sin decimales')
        # Español: Muestra mensaje indicando que es un número sin decimales.
        # English: Print message indicating it is a number without decimals.
    except ValueError:
        # Español: Si ocurre un ValueError (no se puede convertir a int), entra aquí.
        # English: If a ValueError occurs (cannot convert to int), enter here.
        print('No es un valor numerico sin decimales')
        # Español: Muestra mensaje indicando que no es un número entero.
        # English: Print message indicating it is not an integer number.

    try:
        # Español: Intenta ejecutar el bloque que sigue (intentar conversión a float).
        # English: Try to execute the following block (attempt conversion to float).
        d = float(a)
        # Español: Convierte 'a' a float y lo asigna a 'd'.
        # English: Convert 'a' to a float and assign it to 'd'.
        print('Es un valor numerico con decimales')
        # Español: Muestra mensaje indicando que es un número con decimales.
        # English: Print message indicating it is a number with decimals.
    except ValueError:
        # Español: Si ocurre un ValueError (no se puede convertir a float), entra aquí.
        # English: If a ValueError occurs (cannot convert to float), enter here.
        print('No es un valor numerico con decimales')
        # Español: Muestra mensaje indicando que no es un número con decimales.
        # English: Print message indicating it is not a number with decimals.

def listas(d):
    # Español: Define la función 'listas' que intenta reconocer el tipo de dato y devolverlo en su tipo.
    # English: Define the function 'listas' that tries to recognize the data type and return it in its type.
    en = 0
    # Español: Inicializa la variable entera 'en' con 0.
    # English: Initialize the integer variable 'en' to 0.
    dec = 0.0
    # Español: Inicializa la variable decimal 'dec' con 0.0.
    # English: Initialize the float variable 'dec' to 0.0.

    try:
        # Español: Intenta convertir 'd' a entero.
        # English: Try to convert 'd' to an integer.
        en = int(d)
        # Español: Asigna el entero convertido a 'en'.
        # English: Assign the converted integer to 'en'.
        return en
        # Español: Devuelve el entero si la conversión fue exitosa.
        # English: Return the integer if conversion succeeded.
    except ValueError:
        # Español: Si falla la conversión a entero, se captura aquí.
        # English: If integer conversion fails, it is caught here.
        print('No es un entero')
        # Español: Informa que no es un entero.
        # English: Inform that it is not an integer.

    try:
        # Español: Intenta convertir 'd' a float.
        # English: Try to convert 'd' to a float.
        dec = float(d)
        # Español: Asigna el float convertido a 'dec'.
        # English: Assign the converted float to 'dec'.
        return dec
        # Español: Devuelve el float si la conversión fue exitosa.
        # English: Return the float if conversion succeeded.
    except ValueError:
        # Español: Si falla la conversión a float, se captura aquí.
        # English: If float conversion fails, it is caught here.
        print('No es un numero con decimales')
        # Español: Informa que no es un número con decimales.
        # English: Inform that it is not a number with decimals.

    return d
    # Español: Si no es ni entero ni float, devuelve el valor original (como string).
    # English: If it's neither int nor float, return the original value (as string).

def leer():
    # Español: Define la función 'leer' que solicita un dato al usuario y lo procesa.
    # English: Define the function 'leer' that requests data from the user and processes it.
    d = input('Escribe un dato: ')
    # Español: Lee una entrada del usuario y la guarda en 'd'.
    # English: Read user input and store it in 'd'.
    dato = listas(d)
    # Español: Llama a 'listas' para convertir 'd' a su tipo si es posible; guarda el resultado en 'dato'.
    # English: Call 'listas' to convert 'd' to its type if possible; store the result in 'dato'.
    lista.append(dato)
    # Español: Añade el dato (convertido o no) a la lista global 'lista'.
    # English: Append the data (converted or not) to the global list 'lista'.

# Español: Inicializa la lista vacía global donde se almacenarán los datos.
# English: Initialize the empty global list where data will be stored.
lista = []

if __name__ == '__main__':
    # Español: Comprueba si el script está siendo ejecutado directamente (no importado).
    # English: Check if the script is being run directly (not imported).
    while True:
        # Español: Bucle infinito que permite leer repetidamente datos del usuario.
        # English: Infinite loop that allows repeatedly reading user data.
        leer()
        # Español: Llama a la función 'leer' para solicitar y almacenar un dato.
        # English: Call the 'leer' function to request and store one datum.

        res = input('Deseas otro dato (S/N): ')
        # Español: Pregunta al usuario si desea ingresar otro dato y guarda la respuesta en 'res'.
        # English: Ask the user if they want to enter another datum and save the response in 'res'.
        if res == 'n' or res == 'N':
            # Español: Si la respuesta es 'n' o 'N', termina el bucle.
            # English: If the response is 'n' or 'N', break the loop.
            print(lista)
            # Español: Imprime la lista con todos los datos almacenados.
            # English: Print the list with all stored data.
            break
            # Español: Rompe el bucle 'while' terminando la ejecución principal.
            # English: Break the 'while' loop ending main execution.
