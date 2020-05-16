#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

ll mod = 1E9+7;

int main() {
    int H, W; cin >> H >> W;
    char state[H][W];
    for (int i=0; i<H; i++){
        string S; cin >> S;
        for (int j=0; j<W; j++){
            state[i][j] = S[j];
        }
    }
    ll dp[H][W];
    dp[0][0] = 1;
    for (int i=1; i<H; i++){
        if (state[i][0] == '.' && dp[i-1][0] == 1){
            dp[i][0] = 1;
        }
        else{
            dp[i][0] = 0;
        }
    }
    for (int j=1; j<W; j++){
        if (state[0][j] == '.' && dp[0][j-1] == 1){
            dp[0][j] = 1;
        }
        else{
            dp[0][j] = 0;
        }
    }

    for (int i=1; i<H; i++){
        for (int j=1; j<W; j++){
            if (state[i][j] == '#'){
                dp[i][j] = 0;
            }
            else{
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod;
            }
        }
    }
    cout << dp[H-1][W-1] << endl;
}