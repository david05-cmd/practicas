def resultados():
    c2 = 0  # Español: Inicializa el contador c2 en 0.  # English: Initialize the counter c2 to 0.
    print(f'La lista tiene {len(lis)}')  # Español: Imprime la longitud de la lista 'lis'.  # English: Print the length of the list 'lis'.
    for i in ar:  # Español: Recorre cada elemento del arreglo 'ar'.  # English: Iterate over each element of array 'ar'.
        if i !=-1:  # Español: Comprueba si el elemento no es -1 (valor marcador).  # English: Check if the element is not -1 (marker value).
            c2 += 1  # Español: Si no es -1, incrementa el contador c2.  # English: If it's not -1, increment counter c2.
    print(f'El arreglo tiene {c2}')  # Español: Imprime cuántos elementos distintos de -1 hay en 'ar'.  # English: Print how many elements different from -1 are in 'ar'.
    print(ar)  # Español: Imprime el contenido completo del arreglo 'ar'.  # English: Print the full contents of the array 'ar'.
    print(lis)  # Español: Imprime el contenido de la lista 'lis'.  # English: Print the contents of the list 'lis'.

def hola(): # definicion de metodo o funcion
    # Español: Define la función 'hola' que leerá hasta 10 entradas y las catalogará en 'ar' o 'lis'.
    # English: Define the 'hola' function that will read up to 10 inputs and categorize them into 'ar' or 'lis'.
    c = 0  # Español: Inicializa el índice/contador 'c' en 0 para usar como posición en 'ar'.  # English: Initialize index/counter 'c' to 0 to use as position in 'ar'.
    while(True):  # Español: Bucle que leerá datos repetidamente hasta alcanzar 10 entradas.  # English: Loop that will read data repeatedly until reaching 10 entries.
        a = input('Escribe un dato o valor ')  # Español: Pide al usuario un dato y lo guarda en 'a' como cadena.  # English: Ask the user for a datum and store it in 'a' as a string.
        if a.isdigit():  # Español: Si la entrada contiene solo dígitos (número positivo sin signo).  # English: If the input contains only digits (positive number without sign).
            ar[c] = int(a)  # Español: Convierte a entero y lo almacena en la posición c del arreglo 'ar'.  # English: Convert to int and store it at position c of array 'ar'.
        elif a.isalpha():  # Español: Si la entrada contiene solo letras.  # English: If the input contains only letters.
            lis.append(a)  # Español: Añade la cadena a la lista 'lis'.  # English: Append the string to the list 'lis'.
        c += 1  # Español: Incrementa el índice/contador para la siguiente posición del arreglo.  # English: Increment the index/counter for the next array position.
        if c >=10:  # Español: Si se han leído 10 entradas, sale del bucle.  # English: If 10 entries have been read, exit the loop.
            break  # Español: Rompe el while.  # English: Break the while loop.
    resultados()  # Español: Llama a la función 'resultados' para mostrar salidas.  # English: Call the 'resultados' function to display outputs.

ar  = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]  # Español: Arreglo con 10 posiciones inicializadas a -1 como marcador.  # English: Array with 10 positions initialized to -1 as marker.
lis = []  # Español: Lista vacía donde se almacenarán entradas alfabéticas.  # English: Empty list where alphabetic entries will be stored.

if __name__ == "__main__":  # Español: Comprueba si el archivo se ejecuta directamente.  # English: Check if the file is executed directly.
    hola()  # Español: Si la condición anterior se cumple, llama a 'hola()'.  # English: If the above condition holds, call 'hola()'.
