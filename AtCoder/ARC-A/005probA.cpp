#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int N; cin >> N;
    string S;
    int ans = 0;
    string T[3] = {"TAKAHASHIKUN", "Takahashikun", "takahashikun"};
    for (int i=0; i<N; i++){
        cin >> S;
        if (i==N-1){
            S = S.substr(0, S.length()-1);
        }
        for (int j=0; j<3; j++){
            if (S == T[j]){
                ans += 1;
            }
        }
    }
    cout << ans << endl;
}