#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

const int MAXM = 2e5;
const ll INF = 2e18;
int N, M, C;
vector<pair<ll, int>> graph[MAXM];


ll solve() {
    // dijkstra
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> q;
    q.push({0ll, 0});
    vector<ll> Dist(N, INF);
    Dist[0] = 0ll;
    while (!q.empty()) {
        pair<ll, int> p = q.top(); q.pop();
        if (Dist[p.second] < p.first) continue;
        for (auto np : graph[p.second]) {
            if (Dist[np.second] > Dist[p.second] + np.first) {
                Dist[np.second] = Dist[p.second] + np.first;
                q.push(np);
            }
        }
    }

    // sort
    map<ll, vector<ll>> Edges;
    //vector<ll> Vs = Dist;
    for (int i=0; i<N; i++) {
        for (auto p : graph[i]) {
            if (p.second > i) {
                ll d = max(Dist[p.second], Dist[i]);
                Edges[d].push_back(p.first);
            }
        }
    }

    ll ans = INF;
    ll s = 0;
    vector<ll> Keys;
    for (auto itr=Edges.begin(); itr!=Edges.end(); itr=next(itr)) {
        Keys.push_back(itr->first);
    }
    reverse(Keys.begin(), Keys.end());
    for (ll key : Keys) {
        ans = min(ans,  s + C*key);
        //cout << key << " ";
        for (ll e : Edges[key]) {
            //cout << e << " ";
            s += e;
        }
        //cout << endl;
    }
    ans = min(ans, s);
    return ans;
}

int main() {
    cin >> N >> M >> C;
    for (int i=0; i<M; i++) {
        int a, b; ll d;
        cin >> a >> b >> d;
        graph[a-1].push_back({d, b-1});
        graph[b-1].push_back({d, a-1});
    }
    cout << solve() << endl;
}