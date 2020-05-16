#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    string S; cin >> S;
    string ans = "";
    for (int i=0; i<S.length(); i++){
        if (S[i] == 'O' || S[i] == 'D'){
            ans += '0';
        }
        else if (S[i] == 'I'){
            ans += '1';
        }
        else if (S[i] == 'Z'){
            ans += '2';
        }
        else if (S[i] == 'S'){
            ans += '5';
        }
        else if (S[i] == 'B'){
            ans += '8';
        }
        else{
            ans += S[i];
        }
    }
    cout << ans << endl;
}