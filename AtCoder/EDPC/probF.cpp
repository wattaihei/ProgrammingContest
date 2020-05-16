#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    string S, T; cin >> S >> T;
    int ls = S.length(), lt = T.length();
    int dp[ls+1][lt+1];
    for (int i=0; i<=ls; i++){
        dp[i][0] = 0;
    }
    for (int i=0; i<=lt; i++){
        dp[0][i] = 0;
    }
    for (int i=1; i<=ls; i++){
        for (int j=1; j<=lt; j++){
            if (S[i-1] == T[j-1]){
                dp[i][j] = dp[i-1][j-1] + 1;
            }
            else{
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }

    int i = ls-1, j = lt-1;
    bool update;
    string ans = "";
    while (i >= 0 && j >= 0){
        if (S[i] == T[j]) {
            ans = S[i] + ans;
            i -= 1;
            j -= 1;
        }
        else {
            if (dp[i][j+1] > dp[i+1][j]){
                i -= 1;
            }
            else {
                j -= 1;
            }
        }
    }
    cout << ans << endl;
}