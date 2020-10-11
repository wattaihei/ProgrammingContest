#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

int W, H, N;
int state[3001][3001];

ll solve() {
    for (int h=0; h<H; h++) {
        for (int w=0; w<W; w++) {
            if (h != H-1) state[h+1][w] = max(state[h+1][w], state[h][w]-1);
            if (w != W-1) state[h][w+1] = max(state[h][w+1], state[h][w]-1);
            if (w != W-1 && h != H-1) state[h+1][w+1] = max(state[h+1][w+1], state[h][w]-1);
        }
    }

    for (int h=0; h<H; h++) {
        for (int w=W-1; w>=0; w--) {
            if (h != H-1) state[h+1][w] = max(state[h+1][w], state[h][w]-1);
            if (w != 0) state[h][w-1] = max(state[h][w-1], state[h][w]-1);
            if (h != H-1 && w != 0) state[h+1][w-1] = max(state[h+1][w-1], state[h][w]-1);
        }
    }

    for (int h=H-1; h>=0; h--) {
        for (int w=0; w<W; w++) {
            if (h != 0) state[h-1][w] = max(state[h-1][w], state[h][w]-1);
            if (w != W-1) state[h][w+1] = max(state[h][w+1], state[h][w]-1);
            if (h != 0 & w != W-1) state[h-1][w+1] = max(state[h-1][w+1], state[h][w]-1);
        }
    }

    for (int h=H-1; h>=0; h--) {
        for (int w=H-1; w>=0; w--) {
            if (h != 0) state[h-1][w] = max(state[h-1][w], state[h][w] - 1);
            if (w != 0) state[h][w-1] = max(state[h][w-1], state[h][w] - 1);
            if (h != 0 && w != 0) state[h-1][w-1] = max(state[h-1][w-1], state[h][w] - 1);
        }
    }

    ll ans = 0;
    for (int h=0; h<H; h++) {
        for (int w=0; w<W; w++) {
            ans += (ll)state[h][w];
        }
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> W >> H >> N;
    for (int h=0; h<H; h++) {
        for (int w=0; w<W; w++) {
            state[h][w] = 0;
        }
    }
    for (int i=0; i<N; i++) {
        int w, h, x; cin >> w >> h >> x;
        state[h][w] = max(state[h][w], x);
    }
    cout << solve() << endl;
}