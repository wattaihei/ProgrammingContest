#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void print(int query, double ans) {
    cout << "Case #" << query+1 << ": ";
    cout << ans << endl;
}

// void print_imp(int query) {
//     cout << "Case #" << query+1 << ": IMPOSSIBLE" << endl;
// }

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
    int N; cin >> N;
    ll K; cin >> K;
    set<ll> S;
    for (int i=0; i<N; i++) {
        ll t; cin >> t;
        S.insert(t);
    }
    S.insert(K+1);
    ll pre = 0;
    ll dans = 0;
    vector<ll> T1;
    for (ll s : S) {
        ll d = s - pre - 1;
        if (pre == 0 || s == K+1) {
            T1.push_back(d);
        } else {
            T1.push_back((d+1)/2);
        }
        chmax(dans, d);
        pre = s;
    }

    sort(T1.begin(), T1.end(), greater<ll>());
    if (T1.size() > 1) {
        chmax(dans, T1[0] + T1[1]);
    }

    print(query, (double)dans / (double)K );

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