#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main() {
    ll A, B; cin >> A >> B;
    if (A < 0 && B > 0){
        cout << B-A-1 << endl;
    }
    else{
        cout << B-A << endl;
    }
}