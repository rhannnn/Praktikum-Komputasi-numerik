import sympy as sp

def secant_method(expr_str, var_str, x0, x1, tol, max_iter):
    x = sp.Symbol(var_str)
    f = sp.lambdify(x, sp.sympify(expr_str), 'math')

    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if f_x1 - f_x0 == 0:
            return None, i

        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        if abs(x2 - x1) < tol:
            return x2, i + 1

        x0 = x1
        x1 = x2

    return x2, max_iter

if __name__ == "__main__":
    print("="*45)
    print("   PROGRAM PENCARIAN AKAR - METODE SECANT")
    print("="*45)
    
    persamaan = input("Masukkan fungsi (contoh: x**2 - 4) : ")
    variabel = input("Masukkan variabel referensi        : ")
    x0 = float(input("Masukkan tebakan awal 1 (x0)       : "))
    x1 = float(input("Masukkan tebakan awal 2 (x1)       : "))
    toleransi = float(input("Masukkan batas toleransi error     : "))
    maks_iter = int(input("Masukkan batas maksimal iterasi    : "))

    print("-" * 45)
    
    akar, iterasi = secant_method(persamaan, variabel, x0, x1, toleransi, maks_iter)

    if akar is not None:
        print(f"Akar persamaan ditemukan : {akar:.6f}")
        print(f"Total iterasi            : {iterasi}")
    else:
        print("Gagal menemukan akar (terjadi pembagian dengan nol).")
    print("="*45)