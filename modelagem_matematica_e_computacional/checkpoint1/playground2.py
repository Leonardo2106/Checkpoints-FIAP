import numpy as np
import matplotlib.pyplot as plt

def Function(a, b):
    x = np.linspace(-10, 10, 100)
    y = a * x + b

    plt.plot(x, y, label=f'f(x) = {a}x + {b}', color='r')
    plt.grid()
    plt.legend()
    plt.title(f"f(x) = {a}x + {b}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

numA = int(input("Digite o valor de a: "))
numB = int(input("Digite o valor de b: "))

Function(numA, numB)