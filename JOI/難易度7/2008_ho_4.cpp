#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

const int MAXK = 10;
const int INF = 2e9;
int N, M, k, x, d;
int dp[200][MAXK][100]; // n行目のk番目の石にm回の飛ばしジャンプで到達

int main() {
    cin >> N >> M;
    vector<pair<int, int> > A[N];
    for (int i=0; i<N; i++) {
        cin >> k;
        for (int j=0; j<k; j++){
            cin >> x >> d;
            A[i].push_back({x, d});
        }
    }
    int x1, x2, d1, d2;
    for (int n=0; n<N; n++){ 
        for (int m=0; m<=M; m++) {
            for (int k=0; k<A[n].size(); k++) {
                dp[n][k][m] = INF;
                x1 = A[n][k].first; d1 = A[n][k].second;
                if (n == 0) {
                    dp[n][k][m] = 0;
                } else {
                    for (int l=0; l<A[n-1].size(); l++) {
                        x2 = A[n-1][l].first; d2 = A[n-1][l].second;
                        dp[n][k][m] = min(dp[n][k][m], dp[n-1][l][m] + abs(x1-x2)*(d1+d2));
                    }
                    if (n > 1 && m > 0) {
                        for (int l=0; l<A[n-2].size(); l++){
                            x2 = A[n-2][l].first; d2 = A[n-2][l].second;
                            dp[n][k][m] = min(dp[n][k][m], dp[n-2][l][m-1] + abs(x1-x2)*(d1+d2));
                        }
                    } else if (n == 1 && m > 0) {
                        dp[n][k][m] = 0;
                    }
                }
            }
        }
    }

    int ans = INF;
    for (int k=0; k<A[N-1].size(); k++) {
        ans = min(ans, dp[N-1][k][M]);
    }
    if (M > 0) {
        for (int k=0; k<A[N-2].size(); k++) {
            ans = min(ans, dp[N-2][k][M-1]);
        }
    }
    cout << ans << endl;
}