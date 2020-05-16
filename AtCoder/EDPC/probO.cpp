#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;
ll mod = 1E9+7;

int main() {
    int N; cin >> N;
    int A[N][N];
    REP(i, N) REP(j, N) {
        cin >> A[i][j];
    }
    int N_2 = 1, p[N+1]; 
    p[0] = 1;
    REP(i, N) {
        N_2 *= 2;
        p[i+1] = N_2;
    }
    ll dp[N_2];
    REP(i, N_2) dp[i] = 0;
    dp[0] = 1;
    REP(i, N) REP(k, N_2){
        if (__builtin_popcount(k) != i+1){
            continue;
        }
        REP(j, N){
            if (A[i][j] == 0 || !(p[j] & k)){
                continue;
            }
            dp[k] += dp[k-p[j]];
            dp[k] %= mod;
        }
    }
    cout << dp[N_2-1] << endl;
}