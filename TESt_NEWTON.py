# Importamos las librerías necesarias
import numpy as np
from time import *
import matplotlib.pyplot as plt

# Inicializamos listas para guardar las iteraciones y los valores de X
gx = []  # Lista para el número de iteraciones
gy = []  # Lista para los valores de X en cada iteración

# Introducción al método Newton-Raphson
print('MÉTODO NEWTON-RAPHSON\n')
print("Este método linealiza la función a cada paso utilizando su derivada,")
print("para hallar la raíz de la ecuación en las proximidades de un punto inicial.\n")

# Definimos el método Newton-Raphson
def newton_rapshon_method(x, f, df, maxiter, tol):
    """
    Método de Newton-Raphson para encontrar la raíz de una función.

    Args:
    x: Valor inicial.
    f: Función cuya raíz se desea encontrar.
    df: Derivada de la función.
    maxiter: Número máximo de iteraciones.
    tol: Tolerancia del error.

    Returns:
    Una lista con la raíz aproximada y el número de iteraciones realizadas.
    """
    for n in range(maxiter):
        y = x  # Guardamos el valor anterior de x
        x = x - f(x) / df(x)  # Fórmula de Newton-Raphson
        gy.append(x)  # Guardamos el nuevo valor de x
        gx.append(n + 1)  # Guardamos la iteración actual
        print(f"Para la iteración {n+1}: X = {x:.10f}\tError: {abs(x-y):.10e}")

        # Verificamos si el error absoluto es menor o igual a la tolerancia
        if abs(x - y) <= tol:
            grafico(gx, gy)  # Mostramos el gráfico si converge
            return [x, n]  # Retornamos la raíz y el número de iteraciones

    return maxiter  # Retornamos el número máximo de iteraciones si no converge

# Función para graficar el método Newton-Raphson
def grafico(x, y):
    """
    Grafica el número de iteraciones vs los valores de X.

    Args:
    x: Lista de iteraciones.
    y: Lista de valores de X.
    """
    plt.plot(gx, gy, 'r')  # Línea roja
    plt.title('Método de Newton-Raphson')  # Título del gráfico
    plt.xlabel("Número de iteraciones")  # Etiqueta del eje X
    plt.ylabel("Valor de X")  # Etiqueta del eje Y
    plt.show()  # Muestra el gráfico

# Definimos la función cuya raíz se desea encontrar
def f(x):
    return x ** 2 - 1  # Ejemplo: f(x) = x^2 - 1

# Definimos la derivada de la función
def df(x):
    return 2 * x  # Derivada: f'(x) = 2x

# Solicitamos los valores al usuario
Xo = float(input("Ingrese el valor inicial Xo: "))  # Valor inicial
maxite = int(input("Ingrese el número máximo de iteraciones: "))  # Número máximo de iteraciones
tol = float(input("Ingrese la tolerancia (cota del error): "))  # Tolerancia

# Agregamos el valor inicial a las listas
gy.append(Xo)
gx.append(0)

# Mostramos información inicial
print("\nTenemos la función f(x) = x^2 - 1\n")
print("Iniciamos con un valor Xo =", Xo, "\n")

# Ejecutamos el método Newton-Raphson
[x, k] = newton_rapshon_method(Xo, f, df, maxite, tol)

# Verificamos si el método converge o no
if k == maxite:
    print("El método diverge o no converge para la cota de error pedida")
else:
    print("\nLa raíz buscada es:", x)
