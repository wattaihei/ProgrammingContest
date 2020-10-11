#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

const int MAX = 100001;
const int MAX_N = (1<<18);
const int A = 1024;

ll V[MAX_N];
int W[MAX_N], S[MAX], L[MAX];
int N, Q;

ll dp[A+1][MAX+1] = {};

int main() {
    cin >> N;
    for (int i=0; i<N; i++){
        cin >> V[i] >> W[i];
    }
    cin >> Q;
    for (int i=0; i<Q; i++){
        cin >> S[i] >> L[i];
    }

    int nw, w;
    ll nv, v;
    for (int k=1; k<=min(N, A); k++){
        nv = V[k-1]; nw = W[k-1];
        for (int w=0; w<MAX; w++){
            if (w >= nw && (dp[k][w] < dp[k/2][w-nw]+nv)){
                dp[k][w] = dp[k/2][w-nw] + nv;
            }
            if (dp[k][w] < dp[k/2][w]) {
                dp[k][w] = dp[k/2][w];
            }
        }
    }

    int s, l;
    for (int ind=0; ind<Q; ind++){
        s = S[ind]; l = L[ind];
        vector< pair<ll, int> > dp2 = {};
        while (s >= A){
            dp2.push_back({V[s-1], W[s-1]});
            s /= 2;
        }

        ll ans = dp[s][l];
        vector< pair<ll, int> > dp3 = {}, ndp = {};
        dp3.push_back({0ll, 0ll});
        for (auto NVW : dp2){
            nv = NVW.first; nw = NVW.second;
            ndp = {};
            for (auto VW : dp3) {
                v = VW.first; w = VW.second;
                if (w + nw <= l) {
                    ndp.push_back({v+nv, w+nw});
                    ans = max(ans, dp[s][l-(w+nw)]+ (v+nv));
                }
            }
            for (auto VW : ndp) {
                dp3.push_back(VW);
            }
        }
        cout << ans << "\n";
    }

}