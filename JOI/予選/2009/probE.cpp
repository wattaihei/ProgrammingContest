#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

typedef pair<ll, ll> T;

const int INFINT = 2e9;
const ll INFLL = 2e18;

int M;
ll N, p, q, r;
ll X[5050], Y[5050];

ll solve() {
    vector<T> A = {{1ll, r}};

    for (int i=0; i<M; i++) {
        ll x = X[i], y = Y[i];
        vector<T> AA;
        for (auto &[s, t] : A) {
            if (t <= x) {
                AA.push_back({s+(N-x), t+(N-x)});
            } else if (t <= y) {
                if (s <= x) {
                    AA.push_back({s+(N-x), N});
                    AA.push_back({1+(N-y), t-x+(N-y)});
                } else {
                    AA.push_back({s-x+(N-y), t-x+(N-y)});
                }
            } else {
                if (s <= x) {
                    AA.push_back({s+(N-x), N});
                    AA.push_back({1+(N-y), (N-x)});
                    AA.push_back({1, t-y});
                } else if (s <= y) {
                    AA.push_back({s-x+(N-y), N-x});
                    AA.push_back({1, t-y});
                } else {
                    AA.push_back({s-y, t-y});
                }
            }
        }
        A = AA;
    }

    ll ans = 0;
    for (auto &[s, t] : A) {
        ans += max(min(t, q) - max(s, p) + 1, 0ll);
    }

    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> N;
    cin >> M;
    cin >> p >> q >> r;
    for (int i=0; i<M; i++) {
        cin >> X[i] >> Y[i];
    }
    cout << solve() << endl;
}