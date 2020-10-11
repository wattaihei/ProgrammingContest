#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

typedef pair<int, int> Tp;

const int MAXN = 2e5+3;
int N, M;
vector<ll> A;
vector<int> Ls[MAXN];

ll solve() {
    int maxr = 0, minl;
    vector<ll> dp(N+1, 0ll);
    priority_queue<Tp, vector<Tp>, greater<Tp>> q;
    vector<int> f(N+1, 0);
    for (int n=1; n<N+1; n++) {
        maxr = max(maxr, n);
        for (int r : Ls[n]) {
            q.push({n, r});
            maxr = max(maxr, r);
        }
        while (!q.empty() && q.top().second < n) q.pop();
        dp[n] = max(dp[n], dp[n-1]);
        if (q.empty()) {
            dp[n] = max(dp[n], dp[n-1] + A[n-1]);
        } else {
            minl = q.top().first;
            //cout << n << " " << minl << " " << maxr << endl;
            dp[n] = max(dp[n], dp[min(f[n-1], minl-1)] + A[n-1]);
        }
        f[maxr] = n;
        f[n] = max(f[n], f[n-1]);
        //cout << n << " " << dp[n] << endl;
    }
    return dp[N];
}

ll solve2() {
    vector<pair<int, int>> Es;
    for (int i=1; i<N+1; i++) {
        for (int j : Ls[i]) {
            Es.push_back({i, j});
        }
    }
    ll ans = 0;
    for (int bit=0; bit<(1<<N); bit++) {
        bool ok = true;
        for (pair<int, int> p : Es) {
            int cnt = 0;
            for (int i=0; i<N; i++) {
                if (bit&(1<<i) && p.first <= i+1 && i+1 <= p.second) cnt++;
            }
            if (cnt > 1) {
                ok = false;
                break;
            }
        }
        if (ok) {
            ll score = 0;
            vector<int> V;
            for (int i=0; i<N; i++) {
                if (bit&(1<<i)) {
                    V.push_back(i);
                    score += A[i];
                }
            }
            if (ans < score) {
                cout << score << " ";
                for (int v : V) cout << v+1 << " ";
                cout << endl;
            }
            ans = max(ans, score);
        }
    }
    return ans;
}

int main() {
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        ll a; cin >> a;
        A.push_back(a);
    }
    for (int i=0; i<M; i++) {
        int l, r; cin >> l >> r;
        Ls[l].push_back(r);
    }
    cout << solve() << endl;
    //cout << solve2() << endl;
}