#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

const ll INF = 10000000000;
int N, K;
ll A[1010101];
vector<ll> A1(1010101), A2(1010101);


bool solve(vector<ll> B, int border, ll m) {

    ll dp[B.size()+1][2];
    dp[0][0] = 0; dp[0][1] = 0;
    for (int i=0; i<B.size(); i++){
        //cout << B[i] << " ";
        if (B[i] > m) {
            dp[i+1][0] = max(dp[i][0], dp[i][1]);
            dp[i+1][1] = 0;
        } else {
            dp[i+1][0] = max(dp[i][0], dp[i][1]);
            dp[i+1][1] = dp[i][0] + 1;
        }
    }
    //cout << endl;
    //cout << dp[B.size()][0] << " " << dp[B.size()][1] << endl;
    return max(dp[B.size()][0], dp[B.size()][1]) >= border;
    // def solve(B, border, m):
    //     dp = [[0, 0] for _ in range(len(B)+1)]
    //     for i, a in enumerate(B):
    //         if a > m:
    //             dp[i+1][0] = max(dp[i])
    //         else:
    //             dp[i+1][0] = max(dp[i])
    //             dp[i+1][1] = dp[i][0] + 1
    //     return max(dp[-1]) >= border
}


int main() {
    cin >> N >> K;
    for (int i=0; i<N; i++) cin >> A[i];


    if (K%2 == 0) {
        A1.resize(N-1);
        A2.resize(N-1);
        for (int i=0; i<N-1; i++){
            A1[i] = A[i];
        }
        for (int i=1; i<N; i++) {
            A2[i-1] = A[i];
        }
    } else {
        A2.resize(N-2);
        A1.resize(N);
        for (int i=0; i<N; i++){
            A1[i] = A[i];
        }
        for (int i=1; i<N-1; i++) {
            A2[i-1] = A[i];
        }
    }


    //cout << A1.size() << endl;
    ll l = 0;
    ll r = INF;
    ll m;
    bool ok;
    while (r-l > 1){
        m = (r+l)/2;
        if (K%2 == 0) {
            ok = solve(A1, K/2, m) || solve(A2, K/2, m);
        } else {
            ok = solve(A1, (K+1)/2, m) || solve(A2, K/2, m);
        }
        //cout << ok << " " << m  << endl;
        if (ok) {
            r = m;
        } else {
            l = m;
        }
    }
    cout << r << endl;
    return 0;
}