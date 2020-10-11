#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

int H, W;
vector<string> state;

int solve() {
    vector<vector<int>> dp1(H, vector<int>(W, 1));
    for (int h=1; h<H; h++) {
        for (int w=0; w<W; w++) {
            if (state[h][w] == state[h-1][w]) {
                dp1[h][w] = dp1[h-1][w] + 1;
            }
        }
        char tmps = '1';
        int r = 0;
        for (int w=0; w<W; w++) {
            if (tmps != state[h][w]) {
                r = 0;
            } else {
                r++;
            }
            tmps = state[h][w];
            dp1[h][w] = min(r+1, dp1[h][w]);
        }
        tmps = '1';
        int l = 0;
        for (int w=W-1; w>=0; w--) {
            if (tmps != state[h][w]) {
                l = 0;
            } else {
                l++;
            }
            tmps = state[h][w];
            dp1[h][w] = min(l+1, dp1[h][w]);
        }
    }

    vector<vector<int>> dp2(H, vector<int>(W, 1));
    for (int h=H-2; h>=0; h--) {
        for (int w=0; w<W; w++) {
            if (state[h][w] == state[h+1][w]) {
                dp2[h][w] = dp2[h+1][w] + 1;
            }
        }
        char tmps = '1';
        int r = 0;
        for (int w=0; w<W; w++) {
            if (tmps != state[h][w]) {
                r = 0;
            } else {
                r++;
            }
            tmps = state[h][w];
            dp2[h][w] = min(r+1, dp2[h][w]);
        }
        tmps = '1';
        r = 0;
        for (int w=W-1; w>=0; w--) {
            if (tmps != state[h][w]) {
                r = 0;
            } else {
                r++;
            }
            tmps = state[h][w];
            dp2[h][w] = min(r+1, dp2[h][w]);
        }
    }

    int ans = 0;
    for (int h=0; h<H; h++) {
        for (int w=0; w<W; w++) {
            ans += min(dp1[h][w], dp2[h][w]);
        }
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> H >> W;
    for (int i=0; i<H; i++) {
        string S; cin >> S;
        state.push_back(S);
    }
    cout << solve() << endl;
}