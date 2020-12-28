#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;
const int MAXN = 2000;

int N, M;
vector<vector<int>> graph1(MAXN), graph2(MAXN), table(MAXN, vector<int>(MAXN, 0)); 

void dfs2(int p1, int p2, int q1, int q2) {
    if (q1 != -1 && q2 != -1) {
        table[p1][p2] += table[p1][q2] + table[q1][p2] - table[q1][q2];
    } else if (q1 != -1) {
        table[p1][p2] += table[q1][p2];
    } else if (q2 != -1) {
        table[p1][p2] += table[p1][q2];
    }
    for (int np2 : graph2[p2]) {
        dfs2(p1, np2, q1, p2);
    }
}

void dfs1(int p1, int p2, int q1, int q2) {
    dfs2(p1, p2, q1, q2);
    for (int np1 : graph1[p1]) {
        dfs1(np1, p2, p1, q2);
    }
}

void solve() {
    cin >> N >> M;
    int r1, r2;
    for (int i=0; i<N; i++) {
        int j1, j2; cin >> j1 >> j2;
        if (j1 == 0) {
            r1 = i;
        } else {
            graph1[j1-1].push_back(i);
        }
        if (j2 == 0) {
            r2 = i;
        } else {
            graph2[j2-1].push_back(i);
        }
    }

    for (int i=0; i<M; i++) {
        int s1, s2; cin >> s1 >> s2;
        table[s1-1][s2-1]++;
    }

    dfs1(r1, r2, -1, -1);

    for (int i=0; i<N; i++) {
        cout << table[i][i] << endl;
    }
    
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}