#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    string S; cin >> S;
    string ans = "YES";
    for (int i=0; i<S.length(); i++){
        if (S[i] != S[S.length()-1-i]){
            ans = "NO";
        }
    }
    cout << ans << endl;
}