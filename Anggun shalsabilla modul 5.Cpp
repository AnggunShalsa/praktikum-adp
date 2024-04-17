#include <iostream>
#include <vector>
#include <iomanip> // Untuk menyesuaikan format output

using namespace std;

// Fungsi untuk menghitung nilai f(x)
double fungsi_f(int x) {
    if (x > 0) {
        return x*x + 2*x;
    } else if (x < 0) {
        return 1.0 / x;
    } else {
        return 10.0;
    }
}

int main() {
    vector<int> nilai_x;

    // Mengisi nilai_x dengan bilangan bulat dari -10 hingga 10
    for (int i = -10; i <= 10; ++i) {
        nilai_x.push_back(i);
    }

    // Menampilkan output dalam format tabel
    cout << setw(3) << "x" << setw(7) << "f(x)" << endl;
    cout << "----------" << endl;
    for (int x : nilai_x) {
        double f_x = fungsi_f(x);
        cout << setw(3) << x << setw(7) << fixed << setprecision(3) << f_x << endl;
    }

    return 0;
}
