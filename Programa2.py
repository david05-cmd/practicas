a = [10]  # Español: Inicializa un arreglo con un elemento [10].  # English: Initialize an array with one element [10].
b = [ ]  # Español: Inicializa una lista vacía.  # English: Initialize an empty list.

a[0] = 10  # Español: Asigna el valor 10 al primer elemento del arreglo.  # English: Assign value 10 to the first element of array.

b = {'Hola', 10, 100.05, False, 'm', {1, 2, 3, 4, 5, 6, 7}}  # Español: Intenta crear un conjunto con varios tipos de datos.  # English: Attempt to create a set with various data types.
# una lista permite guardar cualquier tipo de dato sin importa su categoria
# a list allows storing any type of data regardless of its category

#b.append(10)  # Español: Esto está comentado, no se ejecuta.  # English: This is commented, not executed.

#ciclos y condiciones
# cycles and conditions
if(len(a) > len(b)):  # Español: Compara la longitud del arreglo 'a' con la del conjunto 'b'.  # English: Compare length of array 'a' with set 'b'.
    print('A es mayor')  # Español: Imprime si 'a' es mayor.  # English: Print if 'a' is larger.

else:  # Español: Caso contrario.  # English: Otherwise.
    print('B es mayor')  # Español: Imprime si 'b' es mayor.  # English: Print if 'b' is larger.
    

for i in a:  # Español: Itera sobre cada elemento en 'a'.  # English: Iterate over each element in 'a'.
    print(i)  # Español: Imprime el elemento actual.  # English: Print the current element.