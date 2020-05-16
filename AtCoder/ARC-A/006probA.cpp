#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int E[6], L[6];
    int b;
    for (int i=0; i<6; i++){
        cin >> E[i];
    }
    cin >> b;
    for (int i=0; i<6; i++){
        cin >> L[i];
    }
    int c = 0;
    bool ok;
    bool bonus = false;
    for (int i=0; i<6; i++){
        ok = false;
        for (int j=0; j<6; j++){
            if (L[i] == E[j]){
                ok = true;
                break;
            }
        }
        if (ok){
            c += 1;
        }
        else if (L[i] == b){
            bonus = true;
        }
    }
    if (c==6){
        cout << 1 << endl;
    }
    else if (c==5 && bonus){
        cout << 2 << endl;
    }
    else if (c==5){
        cout << 3 << endl;
    }
    else if (c==4){
        cout << 4 << endl;
    }
    else if (c==3){
        cout << 5 << endl;
    }
    else{
        cout << 0 << endl;
    }
}