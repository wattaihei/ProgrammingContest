#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
using namespace std;

int main() {
    int N, K; cin >> N >> K;
    int a[N]; REP(i, N) cin >> a[i];
    int dp[K+1]; REP(i, K+1) dp[i] = 0;
    bool can;
    REP(i, K+1){
        can = false;
        REP(j, N){
            if (i-a[j] < 0){
                continue;
            }
            if (dp[i-a[j]] == 0){
                can = true;
            }
        }
        if (can){
            dp[i] = 1;
        }
    }
    if (dp[K] == 1){
        cout << "First" << endl;
    }
    else{
        cout << "Second" << endl;
    }
}