#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

int N, M;

int solve(string S, string T) {
    //reverse(S.begin(), S.end());
    //reverse(T.begin(), T.end());

    int ans = 0;

    int dp[N+1][M+1][2];
    int l = 0;
    for (int i=0; i<N; i++) {
        if (l%2 == 0) {
            if (S[i] == 'I') {
                l += 1;
            } else {
                l = 0;
            }
        } else {
            if (S[i] == 'O') {
                l += 1;
            } else {
                l = 1;
            }
        }
        dp[i+1][0][l%2] = l;
        dp[i+1][0][(l+1)%2] = (l+1)%2 * (-1);
        if (l%2 == 1) ans = max(ans, l);
    }
    l = 0;
    for (int i=0; i<M; i++) {
        if (l%2 == 0) {
            if (T[i] == 'I') {
                l += 1;
            } else {
                l = 0;
            }
        } else {
            if (T[i] == 'O') {
                l += 1;
            } else {
                l = 1;
            }
        }
        dp[0][i+1][l%2] = l;
        dp[0][i+1][(l+1)%2] = (l+1)%2 * (-1);
        if (l%2 == 1) ans = max(ans, l);
    }


    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            dp[i+1][j+1][0] = 0;
            dp[i+1][j+1][1] = -1;
            if (T[j] == 'I') {
                dp[i+1][j+1][1] = max(dp[i+1][j+1][1], dp[i+1][j][0] + 1);
            } else {
                dp[i+1][j+1][0] = max(dp[i+1][j+1][0], dp[i+1][j][1] + 1);
            }
            if (S[i] == 'I') {
                dp[i+1][j+1][1] = max(dp[i+1][j+1][1], dp[i][j+1][0] + 1);
            } else {
                dp[i+1][j+1][0] = max(dp[i+1][j+1][0], dp[i][j+1][1] + 1);
            }
            //cout << dp[i+1][j+1][0] << " " << dp[i+1][j+1][1] << "  ";
            ans = max(ans, dp[i+1][j+1][1]);
        }
        //cout << endl;
    }

    return ans;
}

int main() {
    cin >> N >> M;
    string S,T;
    cin >> S; cin >> T;
    cout << solve(S, T) << endl;
}