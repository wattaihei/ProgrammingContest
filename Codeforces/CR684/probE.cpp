#include <bits/stdc++.h>
#include <atcoder/lazysegtree>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

int N, Q;
int x;
ll y; 

struct S {
    ll a;
    int l;
};

S op(S a, S b) {
    return {a.a+b.a, a.l+b.l};
}

S e() {
    return {0ll, 0};
}

struct F {
    ll v;
    int s;
};

S mapping(F f, S a) {
    if (f.s == -1) {
        return a;
    }
    return {f.v, a.l};
}

F composition(F f, F g) {
    if (f.s > g.s) {
        return f;
    }
    return g;
}

F id() {
    return {0ll, -1};
}


bool g(S x) {
    return x.a <= y;
}

void solve() {
    cin >> N >> Q;
    vector<S> A(N);
    for (int i=0; i<N; i++) {
        ll s; cin >> s;
        A[i] = {s, 1};
    }
    atcoder::lazy_segtree<S, op, e, F, mapping, composition, id> lsg(A);

    for (int i=0; i<Q; i++) {
        int q; cin >> q;
        if (q == 1) {
            cin >> x >> y;
            int ok = 0, ng = N;
            while (abs(ok-ng) > 1) {
                int m = (ok+ng)/2;
                if (lsg.get(m).a >= y) {
                    ok = m;
                } else {
                    ng = m;
                }
            }
            if (ng < x) {
                lsg.apply(ok, x, {y, i});
            }
        } else {
            cin >> x >> y;
            x = max(x-1, lsg.min_left<g>(N));
            cout << (N-x) << endl;
        }
    }

    
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}