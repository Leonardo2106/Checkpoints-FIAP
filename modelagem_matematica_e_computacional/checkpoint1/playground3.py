import numpy as np
import matplotlib.pyplot as plt

def Function(a, b, c, a1, b1):
    delta = (b * b) - 4 * a * c

    if delta <= 0:
        print("\nDigite outros valores para que Delta seja maior que 0\n")
    else:
        print(f"\nDelta = {delta}")

    x = np.linspace(-10, 10, 100)
    y = a * (x * x) + b * x + c

    x1 = np.linspace(-10, 10, 100)
    y1 = a1 * x + b1

    plt.plot(x, y, label = f'f(x) = {a}x² + {b}x + {c}', color = "r")
    plt.plot(x1, y1, label = f"f(x) = {a1}x + {b1}", color = "b")
    plt.grid()
    plt.legend()
    plt.title(f"f(x) = {a}x² + {b}x + {c}\nf(x) = {a1}x + {b1}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

numA = int(input("Digite o valor de a: "))
numB = int(input("Digite o valor de b: "))
numC = int(input("Digite o valor de c: "))

numA1 = int(input("\nDigite o valor de a1: "))
numB1 = int(input("Digite o valor de b1: "))

Function(numA, numB, numC, numA1, numB1)