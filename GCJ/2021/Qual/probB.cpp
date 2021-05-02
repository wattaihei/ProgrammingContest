#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void print(int query, int ans) {
    cout << "Case #" << query+1 << ": " << ans << endl;
}

template <typename T>
bool chmax(T &a, const T& b) {
  if (a < b) {
    a = b;
    return true;
  }
  return false;
}

template <typename T>
bool chmin(T &a, const T& b) {
  if (a > b) {
    a = b;
    return true;
  }
  return false;
}

void solve(int query) {
    int X, Y; cin >> X >> Y;
    string S; cin >> S;
    int N = S.size();

    vector<vector<int>> dp(2, vector<int>(N+1, INFINT));
    dp[0][0] = 0;
    dp[1][0] = 0;
    for (int i=0; i<N; i++) {
        if (S[i] == 'C' || S[i] == '?') {
            chmin(dp[0][i+1], dp[0][i]);
            chmin(dp[0][i+1], dp[1][i] + Y);
        } 
        if (S[i] == 'J' || S[i] == '?') {
            chmin(dp[1][i+1], dp[0][i] + X);
            chmin(dp[1][i+1], dp[1][i]);
        }
    }

    print(query, min(dp[0][N], dp[1][N]));

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q; cin >> Q;
    for (int q=0; q<Q; q++) {
        solve(q);
    }
}