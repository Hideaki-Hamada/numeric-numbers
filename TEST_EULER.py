import math

# Definir la ecuación diferencial como la raíz cuadrada de (x + y)
def f(x, y):
    """
    Define la ecuación diferencial dy/dx = sqrt(x + y).
    
    Parámetros:
        x: variable independiente.
        y: variable dependiente.
        
    Retorna:
        sqrt(x + y), si x + y >= 0.
    """
    if x + y < 0:
        raise ValueError("La raíz cuadrada no está definida para valores negativos de x + y.")
    return math.sqrt(x)*(x*y)

# Método de Euler
def euler_method(f, x0, y0, h, x_end):
    """
    Resuelve una EDO utilizando el método de Euler.
    
    Parámetros:
        f: función que representa dy/dx = f(x, y).
        x0: valor inicial de x.
        y0: valor inicial de y.
        h: tamaño del paso.
        x_end: valor final de x hasta donde se resolverá.
        
    Retorna:
        Una lista de pares (x, y) que representan la solución aproximada.
    """
    results = [(x0, y0)]  # Lista para almacenar los puntos (x, y)
    x, y = x0, y0
    
    while x < x_end:
        try:
            y = y + h * f(x, y)  # Actualización de y según el método de Euler
        except ValueError as e:
            print(f"Error en x = {x:.4f}, y = {y:.4f}: {e}")
            break  # Detener el cálculo si ocurre un error
        x = x + h
        results.append((x, y))
    
    return results

# Solicitar al usuario los parámetros
x0 = float(input("Ingresa el valor inicial de x (x0): "))
y0 = float(input("Ingresa el valor inicial de y (y0): "))
h = float(input("Ingresa el tamaño del paso (h): "))
x_end = float(input("Ingresa el valor final de x: "))

# Resolver la EDO con el método de Euler
try:
    solution = euler_method(f, x0, y0, h, x_end)
except ValueError as e:
    print(f"Error: {e}")
    exit()

# Imprimir los resultados
print("\nSolución aproximada (Método de Euler):")
for x, y in solution:
    print(f"x = {x:.4f}, y = {y:.4f}")
1
