#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main() {
    int N, L; cin >> N >> L;
    string S; cin >> S;
    int tab = 1;
    int ans = 0;
    for (int i=0; i<S.length(); i++){
        if (S[i] == '+'){
            tab += 1;
        }
        else if (tab > 1){
            tab -= 1;
        }
        if (tab > L){
            tab = 1;
            ans += 1;
        }
    }
    cout << ans << endl;
}