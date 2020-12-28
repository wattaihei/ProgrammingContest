#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

struct point {
    ll x, y, s;
};

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    int K, N; cin >> K >> N;
    vector<point> Ps(N);

    for (int i=0; i<N; i++) {
        ll x, y; cin >> x >> y;
        char s; cin >> s;
        int t;
        if (s == 'J') {
            t = 0;
        } else if (s == 'O') {
            t = 1;
        } else {
            t = 2;
        }
        Ps[i] = {x-1, y-1, t};
    }

    int ans = INFINT;
    for (int i=0; i<N; i++) {
        point p = Ps[i];
        int dp[3][3][K];
        for (int k=0; k<K; k++) {
            for (int j=0; j<9; j++) {
                dp[j/3][j%3][k] = 0;
            }
        }
        for (int j=0; j<N; j++) {
            if (i==j) continue;
            point q = Ps[j];
            ll size = 2;
            for (int k=0; k<K; k++) {
                if (q.x/size == p.x/size && q.y/size == p.y/size) {
                    ll t = size/2;
                    int bit = 0;
                    if (q.x/t != p.x/t) {
                        bit |= 1;
                    }
                    if (q.y/t != p.y/t) {
                        bit |= 2;
                    }
                    dp[bit-1][q.s][k]++;
                    break;
                }
                size *= 2;
            }
        }

        int c = 0;
        for (int k=0; k<K; k++) {
            vector<vector<int>> Perms = {
                {0, 1, 2},
                {0, 2, 1},
                {1, 0, 2},
                {1, 2, 0},
                {2, 0, 1},
                {2, 1, 0}
            };
            int w = INFINT;
            for (auto P : Perms) {
                int l = 0;
                for (int i=0; i<3; i++) {
                    for (int j=0; j<3; j++) {
                        if (P[i] != j) {
                            l += dp[i][j][k];
                        }
                    }
                }
                w = min(w, l);
            }
            c += w;
        }
        ans = min(ans, c);
    }

    cout << ans << endl;

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}