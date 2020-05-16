#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    string S;
    int c = 0;
    while (cin >> S){
        if (c != 0) cout << ' ';
        if (S == "Left") cout << '<';
        if (S == "Right") cout << '>';
        if (S == "AtCoder") cout << 'A';
        c++;
        if (S == ""){
            break;
        }
    }
    cout << endl;
}