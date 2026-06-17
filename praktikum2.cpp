#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>

using namespace std;

int pilihan;

// Fungsi yang dipilih user
double f(double x) {
    switch (pilihan) {
        case 1: return sin(x);
        case 2: return cos(x);
        case 3: return x * x;
        case 4: return exp(x);
        default: return sin(x);
    }
}

// Metode Trapezoidal
double trapezoidal(double a, double b, int n) {
    double h = (b - a) / n;

    double sum = (f(a) + f(b)) / 2.0;

    for (int i = 1; i < n; i++) {
        sum += f(a + i * h);
    }

    return sum * h;
}

// Metode Romberg
void romberg(double a, double b, int maxIter) {
    vector<vector<double>> R(maxIter, vector<double>(maxIter, 0));

    for (int i = 0; i < maxIter; i++) {

        int n = pow(2, i);

        R[i][0] = trapezoidal(a, b, n);

        for (int j = 1; j <= i; j++) {
            R[i][j] = R[i][j - 1]
                + (R[i][j - 1] - R[i - 1][j - 1])
                / (pow(4, j) - 1);
        }
    }

    cout << "\nTABEL ROMBERG\n";
    cout << "=====================================================\n";

    for (int i = 0; i < maxIter; i++) {
        for (int j = 0; j <= i; j++) {
            cout << setw(15)
                 << fixed
                 << setprecision(10)
                 << R[i][j];
        }
        cout << endl;
    }

    cout << "\n=====================================================\n";
    cout << "HASIL INTEGRAL = "
         << fixed
         << setprecision(10)
         << R[maxIter - 1][maxIter - 1]
         << endl;
}

int main() {

    double a, b;
    int iterasi;

    cout << "=====================================\n";
    cout << " PROGRAM INTEGRASI ROMBERG\n";
    cout << "=====================================\n";

    cout << "\nPilih Fungsi:\n";
    cout << "1. sin(x)\n";
    cout << "2. cos(x)\n";
    cout << "3. x^2\n";
    cout << "4. e^x\n";
    cout << "Pilihan : ";
    cin >> pilihan;

    cout << "\nMasukkan batas bawah (a) : ";
    cin >> a;

    cout << "Masukkan batas atas (b) : ";
    cin >> b;

    cout << "Masukkan jumlah iterasi : ";
    cin >> iterasi;

    romberg(a, b, iterasi);

    return 0;
}
