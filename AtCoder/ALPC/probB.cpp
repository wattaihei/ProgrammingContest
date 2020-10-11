#include <bits/stdc++.h>
#include <atcoder/fenwicktree>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;
using namespace atcoder;



int main() {
    cin.tie(nullptr);
    int N, Q; cin >> N >> Q;
    fenwick_tree<ll> bit(N+1);
    for (int i=0; i<N; i++) {
        int a; cin >> a;
        bit.add(i+1, a);
    }
    for (int q=0; q<Q; q++) {
        int d, l, r; cin >> d >> l >> r;
        if (d == 0) {
            bit.add(l+1, r);
        } else {
            cout << bit.sum(l+1, r+1) << "\n";
        }
    }
}