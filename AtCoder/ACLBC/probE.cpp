#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

typedef tuple<int, int, int> T;

const int INFINT = 2e9;
const ll mod = 998244353;
const ll INFLL = 2e18;
const int MAXN = 5e5;
int N, Q;
int L[MAXN], R[MAXN], D[MAXN];


void solve() {
    multiset<T> P;
    P.insert({1, N, 1});

    vector<vector<ll>> Sum(10, vector<ll>(N+1, 0));
    for (int n=1; n<10; n++) {
        for (int i=0; i<N; i++) {
            Sum[n][i+1] = (Sum[n][i]*10 + n) % mod;
        }
    }

    ll ans = Sum[1][N];
    for (int i=0; i<Q; i++) {
        int l, r, d;
        l = N+1 - R[i]; r = N+1 - L[i]; d = D[i];
        auto itr = P.lower_bound({l, 0, 0});
        if (itr != P.begin()) {
            // cout << pl << " " << pr << " " << pd << endl;
            itr--;
        }
        vector<T> needInsert = {{l, r, d}};
        vector<T> needErase;
        //cout << i << endl;
        while (itr != P.end()) {
            int pl = get<0>(*itr);
            int pr = get<1>(*itr);
            int pd = get<2>(*itr);
            // cout << pl << " " << pr << " " << pd << endl;
            if (r < pl) break;
            if (pr > r) {
                needInsert.push_back({r+1, pr, pd});
                ans = (ans + mod + (Sum[pd][pr] - Sum[pd][r])) % mod;
            }
            if (pl < l) {
                needInsert.push_back({pl, l-1, pd});
                ans = (ans + mod + (Sum[pd][l-1] - Sum[pd][pl-1])) % mod;
            }
            if (pr >= l) {
                needErase.push_back(*itr);
            }
            ans = (ans + mod - (Sum[pd][pr] - Sum[pd][pl-1])) % mod;
            itr++;
        }
        ans = (ans + mod + Sum[d][r] - Sum[d][l-1]) % mod;
        cout << ans << endl;
        for (auto n : needInsert) {
            P.insert(n);
        }
        for (auto n : needErase) {
            P.erase(n);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> N >> Q;
    for (int i=0; i<Q; i++) {
        cin >> L[i] >> R[i] >> D[i];
    }
    solve();
}