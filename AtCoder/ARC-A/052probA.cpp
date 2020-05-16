#include <bits/stdc++.h>
using namespace std;

int main() {
    string S; cin >> S;
    string NUM = "0123456789";
    string ans = "";
    for (int i=0; i<S.length(); i++){
        for (int j=0; j<NUM.length(); j++){
            if (S[i] == NUM[j]){
                ans += S[i];
            }
        }
    }
    cout << ans << endl;
}