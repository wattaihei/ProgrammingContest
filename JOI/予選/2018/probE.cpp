#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

typedef tuple<int, int, int, int> Tp; 

const int MAX = 30, INF = 1e9;
int H, W;
int A[MAX][MAX];

vector<pair<int, int>> nexts(int h, int w) {
    vector<pair<int, int>> ret;
    if (h != 0) ret.push_back({h-1, w});
    if (h != H-1) ret.push_back({h+1, w});
    if (w != 0) ret.push_back({h, w-1});
    if (w != W-1) ret.push_back({h, w+1});
    return ret;
}


int solve() {
    // dijkstra
    priority_queue<Tp, vector<Tp>, greater<Tp>> q;
    int dp[H][W][H*W]; // dp[h][w][s] : min cost when take s path to (h, w)
    for (int h=0; h<H; h++) {
        for (int w=0; w<W; w++) {
            for (int s=0; s<H*W; s++) {
                dp[h][w][s] = INF;
            }
        }
    }
    dp[0][0][0] = 0;
    q.push({0, 0, 0, 0});
    int h,w,s,d,nh,nw;
    while (!q.empty()) {
        Tp p = q.top(); q.pop();
        d = get<0>(p);
        h = get<1>(p);
        w = get<2>(p);
        s = get<3>(p);
        if (dp[h][w][s] < d || s == H*W-1) continue;
        for (auto np : nexts(h, w)) {
            nh = np.first; nw = np.second;
            if (dp[nh][nw][s+1] > dp[h][w][s] + (2*s+1)*A[nh][nw]) {
                dp[nh][nw][s+1] = dp[h][w][s] + (2*s+1)*A[nh][nw];
                q.push({dp[nh][nw][s+1], nh, nw, s+1});
            }
        }
    }

    int ans = INF;
    for (int s=0; s<H*W; s++) {
        ans = min(ans, dp[H-1][W-1][s]);
    }
    return ans;
}

int main() {
    cin >> H >> W;
    for (int h=0; h<H; h++) {
        for (int w=0; w<W; w++) {
            cin >> A[h][w];
        }
    }
    cout << solve() << endl;
}