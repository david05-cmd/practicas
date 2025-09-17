



a = 1
# Español: Asigna el valor entero 1 a la variable 'a' (coeficiente cuadrático).
# English: Assign the integer 1 to variable 'a' (quadratic coefficient).

b = 2
# Español: Asigna el valor entero 2 a la variable 'b' (coeficiente lineal).
# English: Assign the integer 2 to variable 'b' (linear coefficient).

c = -15
# Español: Asigna el valor entero -15 a la variable 'c' (término independiente).
# English: Assign the integer -15 to variable 'c' (constant term).

p = 0
# Español: Inicializa la variable 'p' con 0; aquí se usará para b**2.
# English: Initialize variable 'p' to 0; here it will be used for b**2.

m = 0
# Español: Inicializa la variable 'm' con 0; aquí se usará para 4*a*c.
# English: Initialize variable 'm' to 0; here it will be used for 4*a*c.

r = 0
# Español: Inicializa la variable 'r' con 0; representará el discriminante (b^2 - 4ac).
# English: Initialize variable 'r' to 0; it will represent the discriminant (b^2 - 4ac).

ra = 0.0
# Español: Inicializa 'ra' como float; se usará para la raíz cuadrada del discriminante.
# English: Initialize 'ra' as float; it will be used for the square root of the discriminant.

d = 0.0
# Español: Inicializa 'd' como float; se usará para el denominador 2*a.
# English: Initialize 'd' as float; it will be used for the denominator 2*a.

x1 = 0.0
# Español: Inicializa 'x1' como float; contendrá la primera raíz.
# English: Initialize 'x1' as float; it will hold the first root.

x2 = 0.0
# Español: Inicializa 'x2' como float; contendrá la segunda raíz.
# English: Initialize 'x2' as float; it will hold the second root.



p = b**2
# Español: Calcula b al cuadrado y lo asigna a 'p'.
# English: Compute b squared and assign it to 'p'.

m = 4*a*c
# Español: Calcula 4*a*c y lo asigna a 'm'.
# English: Compute 4*a*c and assign it to 'm'.

r = p - m
# Español: Calcula el discriminante r = b^2 - 4ac.
# English: Compute the discriminant r = b^2 - 4ac.

if r > 0:
    # Español: Si el discriminante es mayor que 0 hay dos raíces reales distintas.
    # English: If the discriminant is greater than 0 there are two distinct real roots.
    print('Si se puede')
    # Español: Imprime mensaje indicando que sí es posible calcular raíces reales.
    # English: Print a message indicating it's possible to compute real roots.
    ra = r ** (1/2)
    # Español: Calcula la raíz cuadrada del discriminante y la guarda en 'ra'.
    # English: Calculate the square root of the discriminant and store it in 'ra'.
    d = 2*a
    # Español: Calcula el denominador 2*a y lo guarda en 'd'.
    # English: Compute the denominator 2*a and store it in 'd'.
    x1 = (-b + ra) / d
    # Español: Calcula la primera raíz usando la fórmula (-b + sqrt(r)) / (2a).
    # English: Calculate the first root using the formula (-b + sqrt(r)) / (2a).
    x2 = (-b - ra) / d
    # Español: Calcula la segunda raíz usando la fórmula (-b - sqrt(r)) / (2a).
    # English: Calculate the second root using the formula (-b - sqrt(r)) / (2a).
    print(f'El valor de x1 es {x1:.2f} y de x2 es {x2:.2f}')
    # Español: Imprime los valores de x1 y x2 formateados con 2 decimales.
    # English: Print the values of x1 and x2 formatted with 2 decimal places.
else:
    # Español: Si r no es mayor que 0 (es 0 o negativo) entra aquí.
    # English: If r is not greater than 0 (it is 0 or negative) enter here.
    print('No se puede')
    # Español: Imprime mensaje indicando que no es posible calcular dos raíces reales distintas.
    # English: Print a message indicating it's not possible to compute two distinct real roots.
