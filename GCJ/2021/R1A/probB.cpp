#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

ull MAX;
int M;

void print(int query, ull ans) {
    cout << "Case #" << query+1 << ": " << ans << endl;
}

ull subsolve(vector<pair<ull, ull>>& V, int ind, ull sum, ull prod) {
    if (ind == M) {
        if (sum == prod) return sum;
        return 0;
    }
    ull a = V[ind].first;
    ull b = V[ind].second;
    ull s = sum + a*b;
    ull p = prod;
    ull ret = 0;
    while (s >= sum && p <= MAX) {
        ret = max(ret, subsolve(V, ind+1, s, p));
        if (p > MAX/a+1) {
            break;
        }
        p *= a;
        s -= a;
    }
    return ret;
}

void solve(int q) {
    cin >> M;
    vector<pair<ull, ull>> V;
    ull s = 0;
    for (int i=0; i<M; i++) {
        ull a, b; cin >> a >> b;
        V.push_back({a, b});
        s += a*b;
    }
    MAX = s;
    ull ans = subsolve(V, 0, 0, 1);

    print(q, ans);
    
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