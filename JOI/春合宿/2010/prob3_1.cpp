#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

const int MAXN = 1e5;
struct edge {
    int d;
    int x;
    int y;
};

// union by size + path having
class UnionFind {
public:
    vector <ll> par; // 各元の親を表す配列
    vector <ll> siz; // 素集合のサイズを表す配列(1 で初期化)

    // Constructor
    UnionFind(ll sz_): par(sz_), siz(sz_, 1LL) {
        for (ll i = 0; i < sz_; ++i) par[i] = i; // 初期では親は自分自身
    }
    void init(ll sz_) {
        par.resize(sz_);
        siz.assign(sz_, 1LL);  // resize だとなぜか初期化されなかった
        for (ll i = 0; i < sz_; ++i) par[i] = i; // 初期では親は自分自身
    }

    // Member Function
    // Find
    ll root(ll x) { // 根の検索
        while (par[x] != x) {
            x = par[x] = par[par[x]]; // x の親の親を x の親とする
        }
        return x;
    }

    // Union(Unite, Merge)
    bool merge(ll x, ll y) {
        x = root(x);
        y = root(y);
        if (x == y) return false;
        // merge technique（データ構造をマージするテク．小を大にくっつける）
        if (siz[x] < siz[y]) swap(x, y);
        siz[x] += siz[y];
        par[y] = x;
        return true;
    }

    bool issame(ll x, ll y) { // 連結判定
        return root(x) == root(y);
    }

    ll size(ll x) { // 素集合のサイズ
        return siz[root(x)];
    }
};


int N, M, K;
vector<edge> Edges;

int solve() {
    UnionFind uni(N);
    sort(Edges.begin(), Edges.end(), [](edge a, edge b) { return a.d < b.d; });
    int partial = N;
    int ans = 0;
    for (int i=0; partial>K && i<M; i++) {
        edge ed = Edges[i];
        if (uni.issame(ed.x, ed.y)) continue;
        ans += ed.d;
        uni.merge(ed.x, ed.y);
        partial--;
    }
    return ans;
}

int main() {
    cin >> N >> M >> K;
    for (int n=0; n<M; n++) {
        int a,b,c;
        cin >> a >> b >> c;
        Edges.push_back({c, a-1, b-1});
    }
    cout << solve() << endl;
}