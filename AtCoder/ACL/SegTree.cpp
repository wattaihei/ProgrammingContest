#include <bits/stdc++.h>
#include <atcoder/segtree>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

int op(int a, int b) {
    return max(a, b);
}

int e() {
    return -1;
}

int target;

bool f(int a){
    return a < target;
}

void solve() {
    int N, Q; cin >> N >> Q;
    vector<int> A(N);
    for (int i=0; i<N; i++) {
        cin >> (A[i]);
    }
    atcoder::segtree<int, op, e> st(A);
    int t, x, v, l, r;
    for (int j=0; j<Q; j++) {
        cin >> t;
        if (t == 1){
            cin >> x >> v;
            st.set(x-1, v);
        } else if (t == 2) {
            cin >> l >> r;
            cout << st.prod(l-1, r) << endl;
        } else if (t == 3) {
            cin >> x >> target;
            cout << (st.max_right<f>(x-1) + 1) << endl;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}