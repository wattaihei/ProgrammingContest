#include <bits/stdc++.h>
using namespace std;

int main() {
    long long  A, B, K ,L; cin >> A >> B >> K >> L;
    cout << (K/L)*B + min((K%L)*A, B) << endl;
}