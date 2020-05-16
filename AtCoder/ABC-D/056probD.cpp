#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

int main() {
    int N, K; cin >> N >> K;
    int A[N]; REP(i, N) cin >> A[i];

    int dp1[N][K];
    REP(i, K) dp1[0][i] = 0;
    dp1[0][0] = 1;
    REP(n, N-1) REP(k, K){
        if (k < A[n]){
            dp1[n+1][k] = dp1[n][k];
        }
        else{
            dp1[n+1][k] = dp1[n][k] | dp1[n][k-A[n]];
        }
    }

    int dp2[N][K];
    REP(i, K) dp2[N-1][i] = 0;
    dp2[N-1][0] = 1;
    for (int n=N-1; n>0; n--) REP(k, K){
        if (k < A[n]){
            dp2[n-1][k] = dp2[n][k];
        }
        else{
            dp2[n-1][k] = dp2[n][k] | dp2[n][k-A[n]];
        }
    }

    int ans = 0;
    REP(n, N){
        if (K-A[n] <= 0) continue;
        bool need = false;
        int k2 = K-1;
        REP(k1, K){
            if (!dp1[n][k1]) continue;
            while (!dp2[n][k2] || k1+k2>=K){
                k2 -= 1;
            }
            if (k1+k2 >= K-A[n]){
                need = true;
                break;
            }
        }
        if (!need) ans += 1;
    }
    cout << ans << endl;
    
}