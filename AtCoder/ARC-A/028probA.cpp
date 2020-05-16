#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int N, A, B; cin >> N >> A >> B;
    int amari = N%(A+B);
    if (amari > 0 && amari <= A){
        cout << "Ant" << endl;
    }    
    else{
        cout << "Bug" << endl;
    }
}