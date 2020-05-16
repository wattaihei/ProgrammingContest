#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    char a; cin >> a;
    string S; cin >> S;
    string ans = "";
    for (int i=0; i<S.length(); i++){
        if (S[i] == a){
            continue;
        }
        ans += S[i];
    }
    cout << ans << endl;
}