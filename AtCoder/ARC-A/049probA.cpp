#include <bits/stdc++.h>
using namespace std;

int main() {
    string S; cin >> S;
    int A, B, C, D; cin >> A >> B >> C >> D;
    for (int i=0; i<S.length(); i++){
        if (i == A || i == B || i == C || i == D){
            cout << "\"";
        }
        cout << S[i];
    }
    if (D == S.length()){
        cout << "\"";
    }
    cout << endl;
}