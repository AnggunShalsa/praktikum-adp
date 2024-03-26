#include <iostream>
using namespace std;

int main() {
    int counter = 1;

    for (int i = 1; i <= 5; ++i) {
        for (int j = 1; j <= 8; ++j) {
            if (counter % 8 == 4)
                cout << "PINTU ";
            else
                cout << counter << " ";
            counter++;
        }
        cout << endl;
    }

    return 0;
}