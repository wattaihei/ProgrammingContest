#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

template <typename T>
bool chmax(T &a, const T& b) {
  if (a < b) {
    a = b;
    return true;
  }
  return false;
}

template <typename T>
bool chmin(T &a, const T& b) {
  if (a > b) {
    a = b;
    return true;
  }
  return false;
}

const int INFINT = 2e9;
const ll INFLL = 2e18;
const int MAX = 1000;


int H, W;
int A[MAX+2][MAX+2];


void solve() {
    cin >> H >> W;
    for (int h=0; h<H+2; h++) {
        for (int w=0; w<W+2; w++) {
            if (h == 0 || h == H+1 || w == 0 || w == W+1) {
                A[h][w] = 0;
            } else {
                char s; cin >> s;
                A[h][w] = (s == '.' ? 0 : s-'0');
            }

        }
    }


    int M = 1<<5;
    int dp[M][H+2][W+2];
    for (int bit=0; bit<M; bit++) for (int h=0; h<H+2; h++) for (int w=0; w<W+2; w++) dp[bit][h][w] = INFINT;

    dp[7][1][1] = 0;
    int u, d, l, r, s, nbit;
    for (int h=1; h<=H; h++) {
        for (int w=1; w<=W; w++) {
            for (int bit=0; bit<(1<<3); bit++) {
                for (int dir=0; dir<4; dir++) {
                    int a = dp[(dir<<3)+bit][h][w];
                    // right
                    if (w < W) {
                        u = (bit&1) ? A[h-1][w+1] : 0;
                        d = (bit&2) ? A[h+1][w+1] : 0;
                        r = A[h][w+2];
                        s = (dir == 1) ? A[h][w+1] : 0;
                        nbit = (dir == 2) ? 7 : 3;
                        chmin(dp[nbit+(0<<3)][h][w+1], a+s+d+r);
                        chmin(dp[nbit+(1<<3)][h][w+1], a+s+u+d);
                        chmin(dp[nbit+(2<<3)][h][w+1], a+s+u+r);
                    }
                    // down
                    if (h < H) {
                        l = (bit&4) ? A[h+1][w-1] : 0;
                        r = (bit&2) ? A[h+1][w+1] : 0;
                        d = A[h+2][w];
                        s = (dir == 2) ? A[h+1][w] : 0;
                        nbit = (dir == 1) ? 7 : 6;
                        chmin(dp[nbit+(1<<3)][h+1][w], a+s+l+d);
                        chmin(dp[nbit+(2<<3)][h+1][w], a+s+l+r);
                        chmin(dp[nbit+(3<<3)][h+1][w], a+s+r+d);
                    }
                }
            }
        }
    }

    int ans = INFINT;
    for (int bit=0; bit<M; bit++) {
        chmin(ans, dp[bit][H][W]);
    }

    cout << ans << endl;

    
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}