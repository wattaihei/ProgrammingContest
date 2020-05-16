#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;
ll mod = 1E9+7;

int N;
vector<int> g[1000000];
ll dp[1000000][2];
bool checked[1000000];

void dfs(int p) {
    dp[p][0] = 1;
    dp[p][1] = 1;
    for (int q : g[p]){
        if (!checked[q]){
            checked[q] = true;
            dfs(q);
            dp[p][0] = dp[p][0] * (dp[q][0] + dp[q][1]) % mod;
            dp[p][1] = dp[p][1] * dp[q][0] % mod;
        }
    }
    return;
}

int main() {
    cin >> N;
    int x, y;
    REP(i, N-1){
        cin >> x >> y;
        g[x-1].push_back(y-1);
        g[y-1].push_back(x-1);
    }
    REP(i, N) checked[i] = false;
    checked[0] = true;
    dfs(0);
    cout << (dp[0][0] + dp[0][1]) % mod << endl;

}