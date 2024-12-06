def f(x, y):
    # Define la ecuación diferencial aquí. Por ejemplo: dy/dx = x + y
    return x + y

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
        y = y + h * f(x, y)
        x = x + h
        results.append((x, y))
    
    return results

# Solicitar al usuario los parámetros
x0 = float(input("Ingresa el valor inicial de x (x0): "))
y0 = float(input("Ingresa el valor inicial de y (y0): "))
h = float(input("Ingresa el tamaño del paso (h): "))
x_end = float(input("Ingresa el valor final de x: "))

# Resolver la EDO con el método de Euler
solution = euler_method(f, x0, y0, h, x_end)

# Imprimir los resultados
print("\nSolución aproximada (Método de Euler):")
for x, y in solution:
    print(f"x = {x:.4f}, y = {y:.4f}")
