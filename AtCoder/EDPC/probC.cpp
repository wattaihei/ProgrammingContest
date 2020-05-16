#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int N; cin >> N;
    int a[N], b[N], c[N];
    for (int i=0; i<N; i++){
        cin >> a[i] >> b[i] >> c[i];
    }
    int dp[N][3];
    dp[0][0] = a[0];
    dp[0][1] = b[0];
    dp[0][2] = c[0];

    for (int i=1; i<N; i++){
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + a[i];
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + b[i];
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + c[i];
    }
    cout << max({dp[N-1][0], dp[N-1][1], dp[N-1][2]}) << endl;
}