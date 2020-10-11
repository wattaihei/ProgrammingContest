#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;


int N, M;
vector< vector<int> > PP;


void dfs(int m, vector<int> L) {
    if (L.size() == N){
        PP.push_back(L);
        return;
    }
    for (int i=0; i<m+2; i++){
        vector<int> P = L;
        P.push_back(i);
        dfs(max(m, i), P);
    }
}


int main() {
    cin >> N >> M;
    vector<string> Ss;
    for (int i=0; i<N; i++){
        string S;
        cin >> S;
        Ss.push_back(S);
    }

    bool A[N][N];
    for (int i=0; i<N; i++) for (int j=0; j<N; j++) A[i][j] = true;
    for (int i=0; i<N; i++){
        for (int j=i+1; j<N; j++){
            for (int k=0; k<M; k++){
                if (Ss[i][k] != Ss[j][k] && Ss[i][k] != '*' && Ss[j][k] != '*'){
                    A[i][j] = false;
                    A[j][i] = false;
                    break;
                }
            }
        }
    }
    dfs(-1, {});
    int ans = N+1;
    for (auto P : PP){
        map<int, vector<int> > dic;
        for (int i=0; i<N; i++){
            int p = P[i];
            dic[p].push_back(i);
        }
        bool ok = true;
        for (auto L:dic){
            for (int i=0; i<L.second.size(); i++){
                int i1 = L.second[i];
                for (int j=i+1; j<L.second.size(); j++){
                    int i2 = L.second[j];
                    if (!A[i1][i2]){
                        ok = false;
                        break;
                    }
                }
                if (!ok) break;
            }
            if (!ok) break;
        }
        if (ok) {
            ans = min(ans, (int)dic.size());
        }
    }
    cout << ans << endl;
}