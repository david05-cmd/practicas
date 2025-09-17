'''
Hacer un programa que en una lista se introduzca cadenas de caracteres con las siguientes restricciones
1 - las cadenas no deben de haber espacios
2- la cadena solo puede tener mayuscula la primer letra
3- obligatoriamente debe de tener todas las vocales
el programa no termina hasta que la lista tenga 5 elementos
'''
def vocales(cad):
    ba = False  # Español: Inicializa bandera para la vocal 'a'.  # English: Initialize flag for vowel 'a'.
    be = False  # Español: Inicializa bandera para la vocal 'e'.  # English: Initialize flag for vowel 'e'.
    bi = False  # Español: Inicializa bandera para la vocal 'i'.  # English: Initialize flag for vowel 'i'.
    bo = False  # Español: Inicializa bandera para la vocal 'o'.  # English: Initialize flag for vowel 'o'.
    bu = False  # Español: Inicializa bandera para la vocal 'u'.  # English: Initialize flag for vowel 'u'.
    if 'a' in cad or 'A' in cad:
        ba = True  # Español: Si 'a' o 'A' está en la cadena, marca ba True.  # English: If 'a' or 'A' is in the string, set ba True.
    if 'e' in cad or 'E' in cad:
        be = True  # Español: Si 'e' o 'E' está en la cadena, marca be True.  # English: If 'e' or 'E' is in the string, set be True.
    if 'i' in cad or 'I' in cad:
        bi = True  # Español: Si 'i' o 'I' está en la cadena, marca bi True.  # English: If 'i' or 'I' is in the string, set bi True.
    if 'o' in cad or 'O' in cad:
        bo = True  # Español: Si 'o' o 'O' está en la cadena, marca bo True.  # English: If 'o' or 'O' is in the string, set bo True.
    if 'u' in cad or 'U' in cad:
        bu = True  # Español: Si 'u' o 'U' está en la cadena, marca bu True.  # English: If 'u' or 'U' is in the string, set bu True.
    if ba==True and be==True and bi==True and bo==True and bu==True:
        lista.append(cad)  # Español: Si todas las vocales están, añade la cadena a la lista.  # English: If all vowels are present, append the string to the list.
    print(lista)  # Español: Muestra el contenido actual de la lista.  # English: Show the current content of the list.

def minusculas(c1):
    cm = 0  # Español: Contador de minúsculas (excepto la primera) inicializado a 0.  # English: Counter for lowercase letters (except first) initialized to 0.
    print(c1)  # Español: Imprime la cadena recibida.  # English: Print the received string.
    for i in c1[1:]:
        if ord(i) >= 97 and ord(i) <=122:
            cm += 1  # Español: Si el caracter es letra minúscula (ascii 97-122), incrementa el contador.  # English: If the character is lowercase letter (ascii 97-122), increment the counter.
    if cm == len(c1)-1 :
        print(f'La cadena son minusculas expecto la primera {cm}')  # Español: Indica que todas las letras (excepto la primera) son minúsculas.  # English: Indicate that all letters (except the first) are lowercase.
        vocales(cm)  # Español: Llama a la función 'vocales' pasando 'cm' (nota: en el código original se pasa un entero).  # English: Call 'vocales' passing 'cm' (note: original code passes an integer).
    else:
        print('Error la cadena no cumple')  # Español: Indica que la cadena no cumple la restricción de mayúsculas/minúsculas.  # English: Indicate that the string does not meet the uppercase/lowercase restriction.

def inicio():
    ncadena = ""  # Español: Inicializa una cadena vacía que se usará para formar una versión sin caracteres no alfabéticos.  # English: Initialize an empty string to build a version without non-alphabetic characters.
    cadena = input('Escribe una cadena ')  # Español: Pide al usuario que escriba una cadena y la guarda en 'cadena'.  # English: Ask the user to enter a string and store it in 'cadena'.
    for i in cadena:
        if ord(i) != 32: # validar sin espacios
            if cadena.isalpha():
                minusculas(cadena)  # Español: Si toda la cadena es alfabética, llama a 'minusculas' con la cadena original.  # English: If the whole string is alphabetic, call 'minusculas' with the original string.
            else:
                for i in cadena:
                    if ord(i)>=48 and ord(i)>=57:
                        pass  # Español: Si el caracter cumple la condición (según el código original), no hace nada.  # English: If the character meets the condition (as in original code), do nothing.
                    else:
                        ncadena+= i  # Español: Si no, concatena el caracter en 'ncadena'.  # English: Otherwise, concatenate the character into 'ncadena'.
                minusculas(ncadena)  # Español: Llama a 'minusculas' con la cadena filtrada 'ncadena'.  # English: Call 'minusculas' with the filtered string 'ncadena'.

lista = []  # Español: Inicializa la lista vacía donde se almacenarán las cadenas válidas.  # English: Initialize the empty list where valid strings will be stored.
if __name__=='__main__':
    while(True):
        inicio()  # Español: Llama a 'inicio' repetidamente hasta que la lista alcance 5 elementos.  # English: Call 'inicio' repeatedly until the list reaches 5 elements.
        if len(lista) >= 5:
            break  # Español: Si la lista tiene 5 o más elementos, sale del bucle y termina el programa.  # English: If the list has 5 or more elements, exit the loop and end the program.
