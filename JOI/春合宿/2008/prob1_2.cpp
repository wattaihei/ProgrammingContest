#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

struct point {
    int h;
    int w;
};

struct zone {
    int h0 = 101;
    int h1 = 0;
    int w0 = 101;
    int w1 = 0;
};

int N, W, H;
int state[101][101];
vector<point> loc[1001];


vector<int> solve() {
    zone Z[N+1]; // dominating zone for each n
    for (int h=0; h<H; h++) {
        for (int w=0; w<W; w++) {
            int n = state[h][w];
            Z[n].h0 = min(Z[n].h0, h);
            Z[n].h1 = max(Z[n].h1, h+1);
            Z[n].w0 = min(Z[n].w0, w);
            Z[n].w1 = max(Z[n].w1, w+1);
        }
    }

    vector<int> graph[N+1];
    int inEdges[N+1];
    for (int n=1; n<=N; n++) {
        inEdges[n] = 0;
        for (int m=1; m<=N; m++) {
            if (n==m) continue;
            for (point p : loc[n]) {
                if (Z[m].h0 <= p.h && p.h < Z[m].h1 && Z[m].w0 <= p.w && p.w < Z[m].w1) {
                    graph[m].push_back(n);
                    inEdges[n]++;
                    break;
                }
            }
        }
    }

    // topological sort
    vector<int> topologicalSort, stack;
    for (int n=1; n<=N; n++) {
        if (inEdges[n] == 0) stack.push_back(n);
    }

    while (!stack.empty()) {
        int n = stack.back(); stack.pop_back();
        topologicalSort.push_back(n);
        for (int m : graph[n]) {
            inEdges[m]--;
            if (inEdges[m] == 0) {
                stack.push_back(m);
            }
        }
    }

    return topologicalSort;
}

int main() {
    cin >> N >> W >> H;
    for (int h=0; h<H; h++) {
        for (int w=0; w<W; w++) {
            int n; cin >> n;
            state[h][w] = n;
            loc[n].push_back({h, w});
        }
    }
    vector<int> ans = solve();
    for (int i=0; i<ans.size(); i++) {
        cout << ans[i];
        if (i != ans.size()-1) cout << " ";
    }
    cout << endl;
}