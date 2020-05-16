#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;
ll mod = 1E9+7;

int main() {
    string K; cin >> K;
    int L = K.length();
    int D; cin >> D;
    int R[10]; REP(i, 10) R[i] = 0;
    REP(i, 10){
        R[i%D] += 1;
    }

    ll dp[L][10][D];
    REP(i, L) REP(j, 10) REP(k, D) dp[i][j][k] = 0;
    REP(i, 10) dp[0][i][i%D] = 1;
    REP(i, L-1){
        REP(j, 10){
            REP(k, D){
                REP(l, 10){
                    dp[i+1][l][(k+j)%D] += dp[i][l][k]*R[j];
                }
            }
        }
    }

    ll dp2[L][D];
    REP(i, L) REP(k, D) dp2[i][k] = 0;
    int n;
    REP(i, L){
        n = (int)(K[L-i-1]-'0');
        dp2[i][] = dp[i][n][]
    }



}