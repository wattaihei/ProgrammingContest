#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

const int maxN = 600000;

int N, a, b;
vector<int> graph[maxN];
bool checked[maxN];
int L[maxN], R[maxN], nowright[maxN], nowleft[maxN];

int dfs(int p, int last_end) {
    checked[p] = true;
    int s = graph[p].size() + last_end;
    nowright[p] = s;
    R[p] = s;
    nowleft[p] = s;
    for (int i=0; i<graph[p].size(); i++){
        int np = graph[p][i];
        if (!checked[np]){
            nowright[p] -= 1;
            L[np] = nowright[p];
            nowleft[p] = dfs(np, nowleft[p]);
        }
    }
    return nowleft[p];
}

int main(){
    cin >> N;
    for (int i=0; i<N-1; i++){
        cin >> a >> b;
        graph[a-1].push_back(b-1);
        graph[b-1].push_back(a-1);
    }
    L[0] = 1;
    dfs(0, 2);
    for (int i=0; i<N; i++){
        cout << L[i] << " " << R[i] << "\n";
    }
}