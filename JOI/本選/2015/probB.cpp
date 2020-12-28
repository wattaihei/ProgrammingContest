#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

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

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    int N; cin >> N;
    vector<ll> A(N);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }

    vector<vector<ll>> dp(N+1, vector<ll>(N, 0ll));

    for (int s=0; s<N; s++) {
        for (int l=0; l<N; l++) {
            ll al = A[(l+N-1)%N], ar = A[(s+l)%N];
            if (s%2 == 0) {
                chmax(dp[s+1][(l+N-1)%N], dp[s][l] + al);
                chmax(dp[s+1][l], dp[s][l] + ar);
            } else if (al > ar) {
                chmax(dp[s+1][(l+N-1)%N], dp[s][l]);
            } else {
                chmax(dp[s+1][l], dp[s][l]);
            }
        }
    }

    ll ans = 0ll;
    for (int l=0; l<N; l++) {
        chmax(ans, dp[N][l]);
    }

    cout << ans << endl;

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}