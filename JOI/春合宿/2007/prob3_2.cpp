#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

struct edge {
    int np;
    int d;
};

struct node {
    int d;
    int p0;
    int p1;
};

const int MAXN = 110, INF = 2e9;
int N, M;
int X[MAXN], Y[MAXN];
vector<edge> graph[MAXN];


int solve() {
    // dijkstra
    vector<vector<int>> Dist(N, vector<int>(N+1, INF));
    priority_queue<tuple<int, int, int>> q;
    q.push({0, 0, N});
    Dist[0][N] = 0;

    while (!q.empty()) {
        tuple<int, int, int> t = q.top(); q.pop();
        node n = {-get<0>(t), get<1>(t), get<2>(t)};
        if (Dist[n.p0][n.p1] < n.d) continue;
        for (edge n1 : graph[n.p0]) {
            if ((n.p1 == N || (X[n.p1] - X[n.p0])*(X[n1.np] - X[n.p0]) + (Y[n.p1] - Y[n.p0])*(Y[n1.np] - Y[n.p0]) <= 0) 
                    && Dist[n1.np][n.p0] > Dist[n.p0][n.p1] + n1.d) {
                Dist[n1.np][n.p0] = Dist[n.p0][n.p1] + n1.d;
                q.push({-Dist[n1.np][n.p0], n1.np, n.p0});
            }
        }
    }
    int ans = INF;
    for (int d : Dist[1]) {
        ans = min(ans, d);
    }
    if (ans == INF) return -1;
    return ans;
}

int main() {
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        cin >> X[i] >> Y[i];
    }
    for (int i=0; i<M; i++) {
        int a, b, d;
        cin >> a >> b >> d;
        graph[a-1].push_back({b-1, d});
        graph[b-1].push_back({a-1, d});
    }

    cout << solve() << endl;
}