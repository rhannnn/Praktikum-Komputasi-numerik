import matplotlib.pyplot as plt
import numpy as np
a = float(input("masukan nilai awal a = "))
b = float(input("masukan nilai awal b = "))
max_iter = 4
c_list = []

#fungsinya adalah x^3-x-2

fa = a**3 - a - 2
fb = b**3 - b - 2

print("=" * 75)
print(f"{'Iter':>4} {'a':>10} {'b':>10} {'f(a)':>10} {'f(b)':>10} {'c':>10} {'f(c)':>10} {'Error%':>10}")
print("=" * 75)

c_prev = None

for i in range(1, 5):
    fa = a**3 - a - 2
    fb = b**3 - b - 2

    c = (a * fb - b * fa) / (fb - fa)
    fc = c**3 - c - 2

    if c_prev is None or c == 0:
        error_str = "—"
    else:
        error = abs((c - c_prev) / c) * 100
        error_str = f"{error:.6f}%"

    print(f"{i:>4} {a:>10.6f} {b:>10.6f} {fa:>10.6f} {fb:>10.6f} {c:>10.6f} {fc:>10.6f} {error_str:>10}")

    c_prev = c

    if fa * fc < 0:
        b = c
    else:
        a = c

print("=" * 75)
print(f"\nPerkiraan akar setelah {max_iter} iterasi: x ≈ {c:.6f}")
print(f"Nilai f(x) ≈ {fc:.6f}")

x = np.linspace(0.5, 2.5, 400)
y = x**3 - x - 2
 
plt.plot(x, y, label='f(x)')
plt.axhline(0, color='black', linewidth=0.8)
plt.scatter(c_list, [ci**3 - ci - 2 for ci in c_list], color='red', zorder=5, label='Titik c')
plt.title('Regula Falsi')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()