#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;
const ll mod = 1000000007;

vector<int> graph[1010101];
vector<int> checked, childs;

int dfs(int p) {
    int c = 1;
    for (int np : graph[p]) {
        if (!checked[np]) {
            checked[np] = 1;
            c += dfs(np);
        }
    }
    if (p != 0){ 
        childs.push_back(c);
    }
    return c;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q; cin >> Q;
    for (int q=0; q<Q; q++) {
        int N; cin >> N;
        checked.clear();
        childs.clear();
        for (int i=0; i<N; i++) {
            graph[i].clear();
            checked.push_back(0);
        }
        
        for (int i=0; i<N-1; i++) {
            int a, b; cin >> a >> b;
            graph[a-1].push_back(b-1);
            graph[b-1].push_back(a-1);
        }
        int M; cin >> M;
        vector<ll> A;
        for (int i=0; i<M; i++) {
            ll a; cin >> a;
            A.push_back(a);
        }

        checked[0] = 1;
        dfs(0);
        // cout << childs.size() << endl;
        vector<ll> scores;
        for (ll c : childs) {
            scores.push_back(c*((ll)N-c));
            // cout << c << " ";
        }
        // cout << endl;
        sort(scores.begin(), scores.end());
        for (int i=0; i<N-1-M; i++) {
            A.push_back(1ll);
        }
        sort(A.begin(), A.end());
        ll t = 1ll;
        while (A.size() > N-2) {
            ll a = A[A.size()-1]; A.pop_back();
            t = (t * a) % mod;
        }
        A.push_back(t);

        ll ans = 0ll;
        for (int i=0; i<N-1; i++) {
            ans = (ans + (A[i] * (scores[i] % mod))%mod) % mod;
        }

        cout << ans << endl;

    }
}