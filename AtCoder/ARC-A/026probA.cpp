#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int N, A, B; cin >> N >> A >> B;
    if (N > 5){
        cout << (N-5)*A + 5*B << endl;
    }
    else{
        cout << N*B << endl;
    }
}