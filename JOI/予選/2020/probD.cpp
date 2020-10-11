#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

const int INF = 1e9;
int M, R;
const int dist[10][10] = {
    {1, 2, 3, 4, 3, 4, 5, 4, 5, 6},
    {2, 1, 2, 3, 2, 3, 4, 3, 4, 5},
    {3, 2, 1, 2, 3, 2, 3, 4, 3, 4},
    {4, 3, 2, 1, 4, 3, 2, 5, 4, 3},
    {3, 2, 3, 4, 1, 2, 3, 2, 3, 4},
    {4, 3, 2, 3, 2, 1, 2, 3, 2, 3},
    {5, 4, 3, 2, 3, 2, 1, 4, 3, 2},
    {4, 3, 4, 5, 2, 3, 4, 1, 2, 3},
    {5, 4, 3, 4, 3, 2, 3, 2, 1, 2},
    {6, 5, 4, 3, 4, 3, 2, 3, 2, 1}
};

int Cost[40][10][100002];

int ansProb() {
    int ans = 0;
    int key = 0;
    for (char s : to_string(R)) {
        int nkey = (int)(s-'0');
        ans += dist[key][nkey];
        key = nkey;
    }
    return ans;
}

int solve() {
    int maxn = ansProb();

    //int Cost[maxn+1][10][M];
    for (int m=0; m<M; m++) {
        for (int i=0; i<10; i++) {
            for (int j=0; j<maxn+1; j++) {
                Cost[j][i][m] = INF;
            }
        }
    }
    //cout << "akoa" << endl;
    Cost[0][0][0] = 0;
    int ans = maxn, nextm;
    for (int cn=0; cn<maxn; cn++) {
        for (int m=0; m<M; m++) {
            for (int s=0; s<10; s++) {
                for (int t=0; t<10; t++) {
                    nextm = (m*10+t)%M;
                    Cost[cn+1][t][nextm] = min(Cost[cn+1][t][nextm], Cost[cn][s][m] + dist[s][t]);
                    if (nextm == R) ans = min(ans, Cost[cn+1][t][nextm]);
                }
            }
        }
    }
    return ans;
}

int main() {
    cin >> M >> R;
    cout << solve() << endl;
}