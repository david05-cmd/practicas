# Hacer un programa que lea nombre, edad, y sexo de 5 personas, estos elementos tienen que estar dentro de una lista

def inicio():  # Español: Define la función 'inicio' que controla el flujo principal.  # English: Define the 'inicio' function that controls the main flow.
    c= 0  # Español: Inicializa el contador 'c' en 0.  # English: Initialize the counter 'c' to 0.
    while (True):  # Español: Inicia un bucle infinito que repetirá la lectura hasta alcanzar 5 registros.  # English: Start an infinite loop that will repeat the reading until 5 records are reached.
        nombre()  # Español: Llama a la función 'nombre' para leer y validar un nombre.  # English: Call the 'nombre' function to read and validate a name.
        edad()  # Español: Llama a la función 'edad' para leer y validar una edad.  # English: Call the 'edad' function to read and validate an age.
        sexo()  # Español: Llama a la función 'sexo' para leer y validar el sexo (M/F).  # English: Call the 'sexo' function to read and validate sex (M/F).
        c+=1  # Español: Incrementa el contador 'c' después de leer un registro completo.  # English: Increment the counter 'c' after reading a complete record.
        if c >= 5:  # Español: Comprueba si se han leído 5 o más registros.  # English: Check if 5 or more records have been read.
            break  # Español: Si el contador llega a 5, rompe el bucle y termina la función.  # English: If the counter reaches 5, break the loop and end the function.
    


def nombre():  # Español: Define la función 'nombre' para pedir y validar un nombre.  # English: Define the 'nombre' function to request and validate a name.
    while(True):  # Español: Bucle que se repetirá hasta recibir un nombre válido.  # English: Loop that repeats until a valid name is received.
        n=input('Escribe un nombre ')  # Español: Pide al usuario que escriba un nombre y lo guarda en 'n'.  # English: Ask the user to write a name and store it in 'n'.
        if n.isalpha():  # Español: Verifica que 'n' solo contenga letras (sin espacios ni dígitos).  # English: Verify that 'n' contains only letters (no spaces or digits).
            lis.append(n)  # Español: Si es válido, añade el nombre a la lista 'lis'.  # English: If valid, append the name to the list 'lis'.
            break  # Español: Sale del bucle una vez añadido el nombre.  # English: Exit the loop once the name has been appended.
        else:
            print('Nombre no valido')  # Español: Mensaje si el nombre no es válido.  # English: Message shown if the name is not valid.


def edad():  # Español: Define la función 'edad' para pedir y validar la edad.  # English: Define the 'edad' function to request and validate age.
    while(True):  # Español: Bucle que se repetirá hasta recibir una edad válida.  # English: Loop that repeats until a valid age is received.
        e=input('Escribe una edad ')  # Español: Pide al usuario que escriba una edad y la guarda en 'e'.  # English: Ask the user to write an age and store it in 'e'.
        if e.isdigit():  # Español: Verifica que 'e' esté compuesta solo por dígitos.  # English: Verify that 'e' is composed only of digits.
            lis.append(e)  # Español: Si es válido, añade la edad a la lista 'lis'.  # English: If valid, append the age to the list 'lis'.
            break  # Español: Sale del bucle una vez añadida la edad.  # English: Exit the loop once the age has been appended.
        else:
            print('Edad no valida')  # Español: Mensaje si la edad no es válida.  # English: Message shown if the age is not valid.
    
def sexo():  # Español: Define la función 'sexo' para pedir y validar el sexo (M/F).  # English: Define the 'sexo' function to request and validate sex (M/F).
    while(True):  # Español: Bucle que se repetirá hasta recibir un sexo válido.  # English: Loop that repeats until a valid sex is received.
        s=input('Escribe un sexo (M/F) ')  # Español: Pide al usuario que indique el sexo y lo guarda en 's'.  # English: Ask the user to indicate sex and store it in 's'.
        if s=='M' or s=='F':  # Español: Verifica que la entrada sea exactamente 'M' o 'F'.  # English: Verify that the input is exactly 'M' or 'F'.
            lis.append(s)  # Español: Si es válido, añade el sexo a la lista 'lis'.  # English: If valid, append the sex to the list 'lis'.
            break  # Español: Sale del bucle una vez añadido el sexo.  # English: Exit the loop once the sex has been appended.
        else:
            print('Sexo no valido')  # Español: Mensaje si la entrada no es 'M' ni 'F'.  # English: Message shown if the input is not 'M' or 'F'.


def resultados():  # Español: Define la función 'resultados' (en el código actual imprime desde la lista).  # English: Define the 'resultados' function (currently prints from the list).
    i = 0  # Español: Inicializa el índice 'i' en 0.  # English: Initialize the index 'i' to 0.
    while(True):  # Español: Bucle infinito que imprimirá elementos de 'lis' (tal como está, no incrementa 'i').  # English: Infinite loop that will print elements of 'lis' (as written, it does not increment 'i').
        print(lis[i])  # Español: Imprime el elemento de la lista en la posición 'i'.  # English: Print the element of the list at position 'i'.


    


lis = []  # Español: Inicializa la lista vacía 'lis' donde se almacenarán nombres, edades y sexos.  # English: Initialize the empty list 'lis' where names, ages and sexes will be stored.
inicio()  # Español: Llama a la función 'inicio' para comenzar el proceso de ingreso.  # English: Call the 'inicio' function to start the input process.
