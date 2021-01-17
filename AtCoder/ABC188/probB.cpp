#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    int N; cin >> N;
    vector<ll> A(N), B(N);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }
    for (int i=0; i<N; i++) {
        cin >> B[i];
    }

    ll s = 0ll;
    for (int i=0; i<N; i++) {
        s += A[i]*B[i];
    }

    cout << (s== 0 ? "Yes" : "No") << endl;

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}