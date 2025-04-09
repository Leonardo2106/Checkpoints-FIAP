import numpy as np
import matplotlib.pyplot as plt

def Funcao(x):
    return (x * x) - 6

x = np.linspace(-10, 10, 100)
y = Funcao(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label="f(x) = x^2 - 6", color = "b")

zero1 = np.sqrt(6)
zero2 = -np.sqrt(6)
plt.plot([zero1, zero2], [0, 0], "ro", label="Zeros (x = ±√6)")

plt.xlabel("x")
plt.ylabel("y")
plt.title("f(x) = x^2 - 6")
plt.legend()
plt.grid()
plt.show()
