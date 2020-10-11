#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

typedef pair<int, int> T;

const int MAXN = 5000, INF = 2e9;
int N, M;
vector<int> graph[MAXN];
int C[MAXN], R[MAXN];

vector<int> bfs(int start) {
    vector<int> ret, used(N, 0);
    vector<int> q, qq;
    q.push_back(start);
    used[start] = 1;
    for (int c=0; c<R[start]; c++) {
        qq.clear();
        for (int n : q) {
            for (int nn : graph[n]) { 
                if (!used[nn]) {
                    used[nn] = 1;
                    qq.push_back(nn);
                    ret.push_back(nn);
                }
            }
        }
        q = qq;
    }
    return ret;
}

int solve() {
    // make graph
    vector<T> ngraph[N];
    for (int n=0; n<N; n++) {
        vector<int> es = bfs(n);
        for (int e : es) {
            ngraph[n].push_back({C[n], e});
        }
    }

    // dijkstra
    vector<int> D(N, INF);
    priority_queue<T, vector<T>, greater<T>> q;
    q.push({0, 0});
    D[0] = 0;
    while (!q.empty()) {
        T t = q.top(); q.pop();
        int p = t.second;
        if (t.first > D[p]) continue;
        for (T nt : ngraph[p]) {
            int np = nt.second, nd = nt.first;
            if (D[np] > D[p] + nd) {
                D[np] = D[p] + nd;
                q.push({D[np], np});
            }
        }
    }

    return D[N-1];
}

int main() {
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        cin >> C[i] >> R[i];
    }
    for (int i=0; i<M; i++) {
        int a, b;
        cin >> a >> b;
        graph[a-1].push_back(b-1);
        graph[b-1].push_back(a-1);
    }
    cout << solve() << endl;
}