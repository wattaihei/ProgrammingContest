#include <bits/stdc++.h>
#include <atcoder/dsu>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;
using namespace atcoder;

const int INFINT = 2e9;
const ll INFLL = 2e18;

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


void solve() {
    int N, M; cin >> N >> M;
    vector<ll> A(N);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }

    // dsu D(N);
    vector<vector<int>> G1(N), G2(N);
    for (int i=0; i<M; i++) {
        int x, y; cin >> x >> y;
        x--; y--;
        G1[y].push_back(x);
        G2[x].push_back(y);
    }

    ll ans = -INFLL;
    vector<ll> D1(N+1, -INFLL), D2(N+1, INFLL);
    
    for (int i=N-1; i>=0; i--) {
        chmax(D1[i], A[i]);
        for (int np : G1[i]) {
            chmax(D1[np], D1[i]);
        }    
    }

    for (int i=0; i<N; i++) {
        chmin(D2[i], A[i]);
        for (int np : G2[i]) {
            chmin(D2[np], D2[i]);
        }
    }

    for (int i=0; i<N; i++) {
        for (int np : G2[i]) {
            chmax(ans, D1[np]-D2[i]);
        }
    }

    cout << ans << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}