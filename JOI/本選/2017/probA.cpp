#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

int N, Q;
ll S, T;

ll score(ll a) {
    if (a >= 0) {
        return -(a*S);
    } else {
        return -a*T;
    }
}

void solve() {
    cin >> N >> Q >> S >> T;
    vector<ll> A(N);
    ll pa, a, tmp = 0ll;
    cin >> pa;
    for (int i=0; i<N; i++) {
        cin >> a;
        A[i] = a - pa;
        tmp += score(A[i]);
        pa = a;
    }

    for (int q=0; q<Q; q++) {
        int l, r;
        ll x;
        cin >> l >> r >> x;
        l--;
        tmp -= score(A[l]);
        A[l] += x;
        tmp += score(A[l]);
        if (r < N) {
            tmp -= score(A[r]);
            A[r] -= x;
            tmp += score(A[r]);
        }
        cout << tmp << endl;

    }


    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}