#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

const int INF = 2e9;
int N, M, K;
vector<pair<int, int>> graph[4000];

int solve() {
    // dijkstra
    vector<int> Dist(N+1, INF);
    priority_queue<pair<int, int>> q;
    int d, p;
    q.push({0, N});
    Dist[N] = 0;
    while (q.size() > 0) {
        pair<int, int> pa = q.top();
        q.pop();
        p = pa.second; d = -pa.first;
        //cout << p << endl;
        if (Dist[p] < d) continue;
        for (auto npa : graph[p]) {
            int np = npa.second, nd = npa.first;
            //cout << Dist[np] << " " << Dist[p] << " " << nd << endl;
            if (Dist[np] > Dist[p] + nd) {
                //cout << Dist[np] << endl;
                Dist[np] = Dist[p] + nd;
                q.push({-Dist[np], np});
            }
        }
    }

    // get ans
    int ans = 0;
    for (int n=0; n<N; n++) {
        //cout << Dist[n] << " ";
        for (auto pa : graph[n]) {
            p = pa.second; d = pa.first;
            ans = max(ans, (Dist[p] + Dist[n] + d + 1) / 2);
        }
    }

    return ans;
}


int main() {
    cin >> N >> M >> K;
    int a, b, d;
    for (int i=0; i<M; i++) {
        cin >> a >> b >> d;
        graph[a-1].push_back({d, b-1});
        graph[b-1].push_back({d, a-1});
    }
    
    for (int i=0; i<K; i++) {
        int k; cin >> k;
        graph[N].push_back({0, k-1});
        //graph[k-1].push_back({0, N});
    }

    cout << solve() << endl;

}