#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    string S; cin >> S;
    int p = 0;
    for (int i=0; i<S.length(); i++){
        if (p == 0 && (S[i] == 'i' || S[i] == 'I')){
            p += 1;
        }
        else if (p == 1 && (S[i] == 'c' || S[i] == 'C')){
            p += 1;
        }
        else if (p == 2 && (S[i] == 't' || S[i] == 'T')){
            p += 1;
        }
    }
    if (p == 3){
        cout << "YES" << endl;
    }
    else{
        cout << "NO" << endl;
    }
}