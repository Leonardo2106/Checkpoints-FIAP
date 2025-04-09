import numpy as np
import matplotlib.pyplot as plt

def Function(a, b, c):
    delta = (b * b) - 4 * a * c

    if delta <= 0:
        print("\nDigite outros valores para que Delta seja maior que 0\n")
    else:
        print(f"\nDelta = {delta}")

    x = np.linspace(-10, 10, 100)
    y = a * (x * x) + b * x + c

    plt.plot(x, y, label=f'f(x) = {a}x² + {b}x + {c}', color='r')
    plt.grid()
    plt.legend()
    plt.title(f"f(x) = {a}x² + {b}x + {c}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

numA = int(input("Digite o valor de a: "))
numB = int(input("Digite o valor de b: "))
numC = int(input("Digite o valor de c: "))

Function(numA, numB, numC)
