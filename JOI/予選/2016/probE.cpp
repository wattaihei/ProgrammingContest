#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

typedef pair<ll, int> T;
const int MAXN = 1e5, MAXM = 2e5;
const ll INF = 1e12;
int N, M, K, S;
ll P, Q;
vector<int> C;
vector<int> graph[MAXN];


ll solve() {
    // bfs
    vector<int> Dist(N, -1);
    queue<int> q;
    for (int c : C) {
        Dist[c] = 0;
        q.push(c);
    }
    while (!q.empty()) {
        int p = q.front(); q.pop();
        for (int np : graph[p]) {
            if (Dist[np] == -1) {
                Dist[np] = Dist[p] + 1;
                q.push(np);
            }
        }
    }

    // Cost
    vector<ll> Cost(N);
    for (int i=1; i<N-1; i++) {
        if (Dist[i] <= S) {
            Cost[i] = Q;
        } else {
            Cost[i] = P;
        }
    }
    Cost[0] = 0;
    Cost[N-1] = 0;
    for (int c : C) {
        Cost[c] = INF;
    }

    // dijkstra

    priority_queue<T, vector<T>, greater<T>> que;
    vector<ll> R(N, INF);
    que.push({0ll, 0});
    R[0] = 0;
    while (!que.empty()) {
        T p = que.top(); que.pop();
        int n = p.second;
        if (R[n] < p.first) continue;
        //cout << n << " " << R[n] << endl;
        for (int np : graph[n]) {
            //cout << np << endl;
            if (R[np] > R[n] + Cost[np]) {
                R[np] = R[n] + Cost[np];
                que.push({R[np], np});
            }
        }
    }

    return R[N-1];
}


int main() {
    cin >> N >> M >> K >> S;
    cin >> P >> Q;
    for (int i=0; i<K; i++){
        int c; cin >> c;
        C.push_back(c-1);
    }
    for (int i=0; i<M; i++) {
        int a, b;
        cin >> a >> b;
        graph[a-1].push_back(b-1);
        graph[b-1].push_back(a-1);
    }

    cout << solve() << endl;
}