#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

typedef pair<int, int> T;

const int INFINT = 2e9;
const ll INFLL = 2e18;

const int MAXN = 2e5;

int N, M, K;
vector<T> graph[MAXN];


int dfs(int d) {
    for (int l=0; l<d; l++) {
        
        dfs(d+1);
    }
}

int solve() {
    vector<int> Es[K+1][K];
    for (int i=0; i<N; i++) {
        int l = graph[i].size();
        sort(graph[i].begin(), graph[i].end());
        for (int j=0; j<l; j++) {
            int b = graph[i][j].second;
            Es[l][j].push_back(b);
        }
    }
    for (int i=0; i<N; i++) {
        
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> N >> M >> K;
    for (int i=0; i<M; i++) {
        int a, b, d; cin >> a >> b >> d;
        graph[a-1].push_back({d, b-1});
    }
}