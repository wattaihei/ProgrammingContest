#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

struct train {
    int a, b, c, ind;
};

class comp {
    public:
    
    bool operator() (train a, train b) {
        return a.c > b.c;
    }
};

struct dsu {
  public:
    dsu() : _n(0) {}
    dsu(int n) : _n(n), parent_or_size(n, -1) {}

    int merge(int a, int b) {
        assert(0 <= a && a < _n);
        assert(0 <= b && b < _n);
        int x = leader(a), y = leader(b);
        if (x == y) return x;
        if (-parent_or_size[x] < -parent_or_size[y]) std::swap(x, y);
        parent_or_size[x] += parent_or_size[y];
        parent_or_size[y] = x;
        return x;
    }

    bool same(int a, int b) {
        assert(0 <= a && a < _n);
        assert(0 <= b && b < _n);
        return leader(a) == leader(b);
    }

    int leader(int a) {
        assert(0 <= a && a < _n);
        if (parent_or_size[a] < 0) return a;
        return parent_or_size[a] = leader(parent_or_size[a]);
    }

    int size(int a) {
        assert(0 <= a && a < _n);
        return -parent_or_size[leader(a)];
    }

    std::vector<std::vector<int>> groups() {
        std::vector<int> leader_buf(_n), group_size(_n);
        for (int i = 0; i < _n; i++) {
            leader_buf[i] = leader(i);
            group_size[leader_buf[i]]++;
        }
        std::vector<std::vector<int>> result(_n);
        for (int i = 0; i < _n; i++) {
            result[i].reserve(group_size[i]);
        }
        for (int i = 0; i < _n; i++) {
            result[leader_buf[i]].push_back(i);
        }
        result.erase(
            std::remove_if(result.begin(), result.end(),
                           [&](const std::vector<int>& v) { return v.empty(); }),
            result.end());
        return result;
    }

  private:
    int _n;
    // root node: -1 * component size
    // otherwise: parent
    std::vector<int> parent_or_size;
};

void solve() {
    int N, M, K; cin >> N >> M >> K;
    vector<train> V;
    for (int i=0; i<M; i++) {
        train t;
        cin >> t.a >> t.b >> t.c;
        t.a--; t.b--;
        t.ind = i;
        V.push_back(t);
    }
    vector<int> ans(M);
    sort(V.begin(), V.end(), comp());
    vector<dsu> D(K, dsu(N));

    for (int i=0; i<M; i++) {
        train t = V[i];
        int ok = K, ng = -1;
        while (abs(ok-ng) > 1) {
            int m = (ok+ng)/2;
            if (D[m].same(t.a, t.b)) {
                ng = m;
            } else {
                ok = m;
            }
        }
        if (ok == K) {
            ans[t.ind] = 0; 
        } else {
            D[ok].merge(t.a, t.b);
            ans[t.ind] = ok+1;
        }
    }

    for (int i=0; i<M; i++) {
        cout << ans[i] << endl;
    }

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}