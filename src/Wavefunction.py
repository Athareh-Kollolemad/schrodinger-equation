import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(5, 10), dpi=110)
pi = np.pi
L = 2*pi
x_val = np.linspace(0, L, 100)
b = (2/L)**(0.5)


def sy(n, x):
    return b*np.sin(n*pi*x/L)


for n in range(1, 5):
    plt.subplot(4, 1, 5-n)
    y = sy(n, x_val)
    plt.plot(x_val, y)
    plt.axvline(x=L, color='red', lw=1, ls="-", label="L=2π")
    plt.axvline(x=0, color='red', lw=1, ls="-")
    plt.axhline(0, color="black", lw=1, ls="-")
    plt.ylabel(f"ψ(x){n}")

    if n == 1:
        plt.xlabel("x")
        plt.legend(loc="lower right")
plt.suptitle("Wavefunction from Schrodinger equation")
plt.savefig("./src/Wavefunction.png", dpi=300, facecolor="w", edgecolor="w")
plt.show()
