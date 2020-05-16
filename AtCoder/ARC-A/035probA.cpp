#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    string S; cin >> S;
    int l = S.length();
    string ans = "YES";
    for (int i=0; i<l; i++){
        if (S[i] == '*' || S[l-1-i] == '*'){
            continue;
        }
        else if (S[i] != S[l-1-i]){
            ans = "NO";
            break;
        }
    }
    cout << ans << endl;
}