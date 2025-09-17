'''
Hacer un programa que en una lista se introduzca cadenas de caracteres con las siguientes restricciones
1 - las cadenas no deben de haber espacios
2- la cadena solo puede tener mayuscula la primer letra
3- obligatoriamente debe de tener todas las vocales
el programa no termina hasta que la lista tenga 5 elementos
'''

def vocales(cad):  # Español: Define función para verificar si contiene todas las vocales.  # English: Define function to check if contains all vowels.
    b = False  # Español: Inicializa bandera como falsa.  # English: Initialize flag as false.
    if 'a' in cad or 'A' in cad:  # Español: Verifica si contiene 'a' o 'A'.  # English: Check if contains 'a' or 'A'.
        if 'e' in cad or 'E' in cad:  # Español: Verifica si contiene 'e' o 'E'.  # English: Check if contains 'e' or 'E'.
            if 'i' in cad or 'I' in cad:  # Español: Verifica si contiene 'i' o 'I'.  # English: Check if contains 'i' or 'I'.
                if 'o' in cad or 'O' in cad:  # Español: Verifica si contiene 'o' o 'O'.  # English: Check if contains 'o' or 'O'.
                    if 'u' in cad or 'U' in cad:  # Español: Verifica si contiene 'u' o 'U'.  # English: Check if contains 'u' or 'U'.
                        b = True  # Español: Establece bandera como verdadera.  # English: Set flag as true.
                        return b  # Español: Retorna verdadero.  # English: Return true.
                    else:  # Español: Si no tiene 'u' o 'U'.  # English: If doesn't have 'u' or 'U'.
                        return b  # Español: Retorna falso.  # English: Return false.
                else:  # Español: Si no tiene 'o' o 'O'.  # English: If doesn't have 'o' or 'O'.
                    return b  # Español: Retorna falso.  # English: Return false.
            else:  # Español: Si no tiene 'i' o 'I'.  # English: If doesn't have 'i' or 'I'.
                return b  # Español: Retorna falso.  # English: Return false.
        else:  # Español: Si no tiene 'e' o 'E'.  # English: If doesn't have 'e' or 'E'.
            return b  # Español: Retorna falso.  # English: Return false.
    else:  # Español: Si no tiene 'a' o 'A'.  # English: If doesn't have 'a' or 'A'.
        return b  # Español: Retorna falso.  # English: Return false.
                   
def minusculas(cad):  # Español: Define función para verificar minúsculas después del primer carácter.  # English: Define function to check lowercase after first character.
    a = False  # Español: Inicializa bandera como falsa.  # English: Initialize flag as false.
    for i in cad[1:]:  # Español: Itera desde el segundo carácter hasta el final.  # English: Iterate from second character to end.
        if ord(i) >= 97 and ord(i) <=122:  # Español: Verifica si es minúscula (código ASCII).  # English: Check if lowercase (ASCII code).
                pass  # Español: No hace nada si es minúscula.  # English: Do nothing if lowercase.
        else:  # Español: Si no es minúscula.  # English: If not lowercase.
            return a  # Español: Retorna falso inmediatamente.  # English: Return false immediately.
    a = True  # Español: Si todos los caracteres son minúsculas.  # English: If all characters are lowercase.
    return a  # Español: Retorna verdadero.  # English: Return true.


def inicio():  # Español: Función principal que solicita y valida la entrada.  # English: Main function that requests and validates input.
    cad = input('Escribe una cadena: ')  # Español: Solicita una cadena al usuario.  # English: Prompt user for a string.
    
    rvoc = vocales(cad)  # Español: Verifica si tiene todas las vocales.  # English: Check if has all vowels.
    if rvoc == True:  # Español: Si tiene todas las vocales.  # English: If has all vowels.
        if not ' ' in cad:  # Español: Verifica que no tenga espacios.  # English: Check that it has no spaces.
            rmin = minusculas(cad)  # Español: Verifica minúsculas después del primer carácter.  # English: Check lowercase after first character.
            if rmin == True:  # Español: Si cumple regla de minúsculas.  # English: If follows lowercase rule.
                lista.append(cad)  # Español: Agrega cadena válida a la lista.  # English: Add valid string to list.
            else:  # Español: Si no cumple regla de minúsculas.  # English: If doesn't follow lowercase rule.
                print('Solo puede ser mayuscula el primer caracter')  # Español: Mensaje de error.  # English: Error message.
        else:  # Español: Si contiene espacios.  # English: If contains spaces.
            print('No debe de tener espacios')  # Español: Mensaje de error.  # English: Error message.
    else:  # Español: Si no tiene todas las vocales.  # English: If doesn't have all vowels.
        print('Necesita tener todas las vocales')  # Español: Mensaje de error.  # English: Error message.

lista = []  # Español: Inicializa lista vacía.  # English: Initialize empty list.
if __name__=='__main__':  # Español: Punto de entrada del programa.  # English: Program entry point.
    while(True):  # Español: Bucle infinito.  # English: Infinite loop.
        inicio()  # Español: Llama a función inicio.  # English: Call inicio function.
        if len(lista) >= 5:  # Español: Verifica si la lista tiene 5 elementos.  # English: Check if list has 5 elements.
            print(lista)  # Español: Imprime la lista.  # English: Print the list.
            break  # Español: Termina el bucle.  # English: End loop.