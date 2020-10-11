#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;
const int MAXN = 1e5;

int N, M;
int P[MAXN], H[MAXN];

bool solve(vector<vector<int> > graph) {
    vector<int> stack = {};
    vector<int> Par(N, -1), S(N, 0), MAX(N, 0);
    stack.push_back(0);
    Par[0] = -2;
    while (!stack.empty()) {
        int p = stack[stack.size()-1]; stack.pop_back();
        if (p >= 0) {
            stack.push_back(~p);
            for (auto np : graph[p]) {
                if (Par[np] == -1) {
                    Par[np] = p;
                    stack.push_back(np);
                }
            }
        } else {
            p = ~p;
            S[p] -= P[p];
            MAX[p] += P[p];
            if (S[p] > H[p] || H[p] > MAX[p] || (MAX[p] - H[p])%2 == 1) {
                return false;
            }
            S[p] = max(S[p], H[p]);
            if (p != 0) {
                S[Par[p]] += S[p];
                MAX[Par[p]] += MAX[p];
            }
        }
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q; cin >> Q;
    for (int q=0; q<Q; q++) {
        cin >> N >> M;
        for (int i=0; i<N; i++) {
            cin >> P[i];
        }
        for (int i=0; i<N; i++) {
            cin >> H[i];
        }
        vector<vector<int> > graph(N);
        for (int i=0; i<N-1; i++) {
            int a, b; cin >> a >> b;
            graph[a-1].push_back(b-1);
            graph[b-1].push_back(a-1); 
        }
        cout << (solve(graph) ? "YES" : "NO") << endl;
    }
}