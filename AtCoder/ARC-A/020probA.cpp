#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int A, B; cin >> A >> B;
    if (abs(A) > abs(B)){
        cout << "Bug" << endl;
    }
    else if (abs(A) < abs(B)){
        cout << "Ant" << endl;
    }
    else{
        cout << "Draw" << endl;
    }
}