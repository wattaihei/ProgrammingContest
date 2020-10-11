#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;
const int MAXN = 1e5;

int N, M;
vector<int> graph[MAXN], igraph[MAXN];


vector<vector<int>> grouping() {
    // make new graph
    vector<int> D(N, -1), Seq;
    for (int i=0; i<N; i++) {
        if (D[i] != -1) continue;
        vector<int> stack = {i};
        D[i] = Seq.size();
        Seq.push_back(i);
        while (!stack.empty()) {
            int p = stack[stack.size()-1]; stack.pop_back();
            if (p >= 0) {
                stack.push_back(~p);
                for (int np : graph[p]) {
                    if (D[np] == -1) {
                        D[np] = -2;
                        stack.push_back(np);
                    }
                }
            } else {
                p = ~p;
                D[p] = Seq.size();
                Seq.push_back(p);
            }
        }
    }

    reverse(Seq.begin(), Seq.end());
    vector<vector<int>> groups;
    vector<int> Index(N, -1);
    for (int i : Seq) {
        if (Index[i] != -1) continue;
        vector<int> gp = {i};
        vector<int> stack = {i};
        Index[i] = groups.size();
        while (!stack.empty()) {
            int p = stack[stack.size()-1]; stack.pop_back();
            if (p >= 0) {
                stack.push_back(~p);
                for (int np : igraph[p]) {
                    if (Index[np] == -1) {
                        Index[np] = -2;
                        stack.push_back(np);
                    }
                }
            } else {
                p = ~p;
                Index[p] = groups.size();
                gp.push_back(p);
            }
        }
        groups.push_back(gp);
    }

    return groups;
}

int solve() {
    vector<vector<int>> groups = grouping();

    int ans = 0;
    for (auto gp : groups) {
        unordered_set<int> gps;
        for (int p : gp) {
            gps.insert(p);
        }
        bool mustCount = true;
        for (int p : gp) {
            for (int np : igraph[p]) {
                if (!gps.count(np)) mustCount = false;
            }
        }
        if (mustCount) {
            ans++;
        } 
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> N >> M;
    for (int i=0; i<M; i++) {
        int a, b; cin >> a >> b;
        graph[a-1].push_back(b-1);
        igraph[b-1].push_back(a-1);
    }

    cout << solve() << endl;
}