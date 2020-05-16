#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
using namespace std;

int main() {
    int N; cin >> N;
    int sum = 0;
    int a[N]; REP(i, N) cin >> a[i];
    REP(i, N) sum += a[i];
    double dp[sum+1][N][4];
    REP(i, sum+1) REP(j, N) REP(k, 4) dp[i][j][k] = 0;
    REP(i, sum+1){
        REP(j, N){
            REP(k, 4){
                REP(l, )
                if (k != 0){
                    dp[i][j][k] += 
                }
            }
        }
    }

}