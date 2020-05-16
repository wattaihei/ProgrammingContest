#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int N, M; cin >> N >> M;
    vector<int> g1[N], g2[N];
    for (int i=0; i<M; i++){
        int s, t; cin >> s >> t;
        g1[s-1].push_back(t-1);
        g2[t-1].push_back(s-1);
    }
    queue<int> q;
    for (int i=0; i<N; i++){
        if (g2[i].size() == 0){
            q.push(i);
        }
    }
    vector<int> D(N);
    for (int i=0; i<N; i++){
        D[i] = 0;
    }
    int checked[N];
    for (int i=0; i<N; i++){
        checked[i] = 0;
    }
    int p;
    while (q.size()){
        p = q.front(); q.pop();
        for (int np : g1[p]){
            D[np] = max(D[np], D[p]+1);
            checked[np] += 1;
            if (checked[np] == g2[np].size()){
                q.push(np);
            }
        }
    }
    cout << *max_element(D.begin(), D.end()) << endl;
}