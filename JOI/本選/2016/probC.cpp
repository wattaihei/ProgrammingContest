#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

const int MAX = 200000;

int N, M, Q;
vector<int> graph[MAX];
vector<pair<int, int>> Edge;

void solve() {
    cin >> N >> M >> Q;
    for (int i=0; i<M; i++) {
        int a, b; cin >> a >> b;
        graph[a-1].push_back(b-1);
        graph[b-1].push_back(a-1);
        Edge.push_back({a-1, b-1});
    }

    // bfs
    queue<int> q;
    vector<int> D(N, INFINT);
    D[0] = 0;
    q.push(0);
    while (!q.empty()) {
        int p = q.front(); q.pop();
        for (int np : graph[p]) {
            if (D[np] > D[p]+1) {
                D[np] = D[p]+1;
                q.push(np);
            }
        }
    }

    vector<unordered_set<int>> Childs(N);
    vector<int> Parent(N, 0);
    for (int i=0; i<M; i++) {
        pair<int, int> pa = Edge[i];
        int a = pa.first, b = pa.second;
        if (D[a] == D[b]+1) {
            swap(a, b);
        }
        if (D[b] == D[a]+1) {
            Parent[b]++;
            Childs[a].insert(b);
        }
    }

    int ans = 0;
    for (int iq=0; iq<Q; iq++) {
        int m; cin >> m; m--;
        pair<int, int> pa = Edge[m];
        int a = pa.first, b = pa.second;
        if (D[a] == D[b]+1) {
            swap(a, b);
        }
        if (D[b] == D[a]+1 && Childs[a].count(b)) {
            Parent[b]--;
            Childs[a].erase(b);
            if (Parent[b] == 0) {
                ans++;
                q.push(b);
                while (!q.empty()) {
                    int p = q.front(); q.pop();
                    for (int np : Childs[p]) {
                        Parent[np]--;
                        if (Parent[np] == 0) {
                            ans++;
                            q.push(np);
                        }
                    }
                    Childs[p].clear();
                }
            }
        }

        cout << ans << endl;
    }

    
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}