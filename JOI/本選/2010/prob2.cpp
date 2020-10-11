#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

const int MAXN = 1e4, INF = 2e9;
int N;
int A[MAXN];

int solve() {
    // count of color 0
    vector<vector<int>> dp = {{INF, 0}, {INF, INF}};
    for (int i=0; i<N-1; i++) {
        int maxj = min(i+2, N/2);
        vector<vector<int>> ndp(2, vector<int>(maxj+1, INF));
        for (int j=0; j<maxj; j++) {
            ndp[0][j+1] = min(dp[1][j] + A[i], dp[0][j]);
            ndp[1][j] = min(dp[1][j], dp[0][j] + A[i]);
        }
        if (dp[0].size() == maxj+1) {
            ndp[1][maxj] = min(dp[1][maxj], dp[0][maxj] + A[i]);
        }
        dp = ndp;
        //for (auto ddp : dp) cout << ddp[0] << " " << ddp[1] << endl;
        //cout << endl;
    }
    return min(dp[0][N/2], dp[1][N/2]);
}

int main() {
    cin >> N;
    for (int i=0; i<N-1; i++) {
        cin >> A[i];
    }
    cout << solve() << endl;
}
