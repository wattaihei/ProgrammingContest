#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

typedef pair<ll, int> T;

const ll INF = 1e18;
int N, M;
vector<ll> S, V, C;


int solve() {
    sort(C.begin(), C.end());
    priority_queue<T> B;
    for (int i=0; i<N; i++) {
        int ind = lower_bound(C.begin(), C.end(), S[i]) - C.begin();
        B.push({V[i], ind});
        //cout << V[i] << " " << ind << endl;
    }

    int ans = 0;
    for (int i=M-1; i>=0; i--) {
        while (!B.empty() && B.top().second > i) B.pop();
        if (!B.empty()) {
            B.pop();
            ans++;
        }
    }
    return ans;
}


int main() {
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        ll s, v;
        cin >> s >> v;
        S.push_back(s);
        V.push_back(v);
    }
    for (int i=0; i<M; i++) {
        ll c; cin >> c;
        C.push_back(c);
    }
    cout << solve() << endl;
}