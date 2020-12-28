#include <bits/stdc++.h>
#include <atcoder/lazysegtree>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;
using namespace atcoder;

const int INFINT = 2e9;
const ll INFLL = 2e18;

struct S {
    ll sum0, sum1, rev;
};

S op(S a, S b) {
    return S{
        a.sum0 + b.sum0,
        a.sum1 + b.sum1,
        a.rev + b.rev + (b.sum0 * a.sum1)
    };
}

S e() {
    return S{0, 0, 0};
}

struct F {
    int a;
};

S mapping(F f, S a) {
    ll size = a.sum0 + a.sum1;
    if ((f.a)%2 == 0) return a;
    return S{
        a.sum1,
        a.sum0,
        size*(size-1)/2 - (a.sum0)*(a.sum0-1)/2 - a.sum1*(a.sum1-1)/2 - a.rev 
    };
}

F composition(F f1, F f2) {
    return {(f1.a + f2.a) % 2};
}

F id() {
    return {0};
}

void solve() {
    int N, Q; cin >> N >> Q;
    vector<S> A(N);
    int a;
    for (int i=0; i<N; i++) {
        cin >> a;
        if (a == 0) {
            A[i] = S{1, 0, 0};
        } else {
            A[i] = S{0, 1, 0};
        }
    }
    lazy_segtree<S, op, e, F, mapping, composition, id> lseg(A);

    int t, l, r;
    for (int q=0; q<Q; q++) {
        cin >> t >> l >> r;
        if (t == 1) {
            lseg.apply(l-1, r, {1});
        } else {
            cout << lseg.prod(l-1, r).rev << endl;
        }
    }

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}