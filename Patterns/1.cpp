#include <iostream>
using namespace std;

void problem1(int n) {
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            cout << "*";
        }
        cout << endl;
    }
}

void problem2(int n) {
    for(int i=1; i<=n; i++) {
        for(int j=1; j<=i; j++) {
            cout << "*";
        }
        cout << endl;
    }
}

void problem3(int n) {
    for(int i=1; i<=n; i++) {
        int count=1;
        for(int j=1; j<=i; j++) {
            cout << count++;
        }
        cout << endl;
    }
}

int main() {

    // problem1(4);
    // problem2(4);
    problem3(4);
    return 0;

}