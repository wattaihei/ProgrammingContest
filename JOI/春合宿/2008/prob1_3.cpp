#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

const int MAX = 1e5, MX = 1e3;
int N, M, D, K;
int X[MAX], Y[MAX];

int solve() {
    // block
    vector<int> B[MX/D+2][MX/D+2];
    pair<int, int> loc[N];
    for (int i=0; i<N; i++) {
        B[X[i]/D][Y[i]/D].push_back(i);
        loc[i] = {X[i]/D, Y[i]/D};
    }
    // check and make graph
    vector<int> graph[N];
    for (int i=0; i<N; i++) {
        int ix = loc[i].first, iy = loc[i].second;
        for (int jx=max(ix-1,0); jx<=ix+1; jx++) {
            for (int jy=max(iy-1,0); jy<=iy+1; jy++) {
                for (int k : B[jx][jy]) {
                    if (i != k && (X[i]-X[k])*(X[i]-X[k]) + (Y[i]-Y[k])*(Y[i]-Y[k]) <= D*D) {
                        //cout << i << " " << k << endl;
                        graph[i].push_back(k);
                    }
                }
            }
        }
    }

    // bfs
    vector<int> Dist(N, -1);
    Dist[0] = 0;
    queue<int> q;
    q.push(0);
    while (!q.empty()) {
        int p = q.front(); q.pop();
        for (int np : graph[p]) {
            if (Dist[np] == -1) {
                Dist[np] = Dist[p] + 1;
                q.push(np);
            }
        }
    }

    int ans = 0;
    for (int i=0; i<N; i++) {
        //cout << i << " " <<  Dist[i] << endl;
        if (Dist[i] != -1 && Dist[i] <= K && Dist[i]+M > K) {
            ans++;
        }
    }

    return ans;
}

int main() {
    cin >> N;
    cin >> M;
    cin >> D;
    cin >> K;
    for (int i=0; i<N; i++) {
        cin >> X[i] >> Y[i];
    }
    cout << solve() << endl;
}