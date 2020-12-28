#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 1e18;

void solve() {
    int H, W; cin >> H >> W;
    vector<vector<ll>> state(H, vector<ll>(W));
    vector<vector<ll>> L0(H, vector<ll>(W+1, INFLL));
    vector<vector<ll>> L1(H, vector<ll>(W+1, -INFLL));
    vector<vector<ll>> R0(H, vector<ll>(W+1, INFLL));
    vector<vector<ll>> R1(H, vector<ll>(W+1, -INFLL));

    ll smallest = INFLL, biggest = -INFLL;
    for (int h=0; h<H; h++) {
        for (int w=0; w<W; w++) {
            cin >> state[h][w];
            biggest = max(biggest, state[h][w]);
            smallest = min(smallest, state[h][w]);
            L0[h][w+1] = min(L0[h][w], state[h][w]);
            L1[h][w+1] = max(L1[h][w], state[h][w]);
        }
        for (int w=W-1; w>=0; w--) {
            R0[h][w] = min(R0[h][w+1], state[h][w]);
            R1[h][w] = max(R1[h][w+1], state[h][w]);
        }
    }

    ll ng = -1, ok = biggest - smallest;
    while (abs(ok-ng) > 1) {
        ll d = (ok+ng)/2;
        bool con = false;
        ll t0 = INFLL, t1 = -INFLL;
        int l0 = W;
        for (int h=0; h<H; h++) {
            for (int w=0; w<l0; w++) {
                if (state[h][w] > d+smallest) {
                    l0 = w;
                    break;
                }
            }
            t0 = min(t0, R0[h][l0]);
            t1 = max(t1, R1[h][l0]);
            if (t1-t0 > d) {
                l0 = -1;
                break;
            }
            if (L0[h][l0] <= smallest) {
                con = true;
            }
        }
        if (l0 != -1 && con) {
            ok = d;
            continue;
        }
        int l1 = W;
        con = false;
        t0 = INFLL, t1 = -INFLL;
        for (int h=H-1; h>=0; h--) {
            for (int w=0; w<l1; w++) {
                if (state[h][w] > d+smallest) {
                    l1 = w;
                    break;
                }
            }
            t0 = min(t0, R0[h][l1]);
            t1 = max(t1, R1[h][l1]);
            if (t1-t0 > d) {
                l1 = -1;
                break;
            }
            if (L0[h][l1] <= smallest) {
                con = true;
            }
        }
        if (l1 != -1 && con) {
            ok = d;
            continue;
        }
        int r0 = 0;
        con = false;
        t0 = INFLL, t1 = -INFLL;
        for (int h=0; h<H; h++) {
            for (int w=W-1; w>=max(0, r0); w--) {
                if (state[h][w] > d+smallest) {
                    r0 = w+1;
                    break;
                }
            }
            t0 = min(t0, L0[h][r0]);
            t1 = max(t1, L1[h][r0]);
            if (t1-t0 > d) {
                r0 = -1;
                break;
            }
            if (R0[h][r0] <= smallest) {
                con = true;
            }
        }
        if (r0 != -1 && con) {
            ok = d;
            continue;
        }
        int r1 = 0;
        con = false;
        t0 = INFLL, t1 = -INFLL;
        for (int h=H-1; h>=0; h--) {
            for (int w=W-1; w>=max(0, r1); w--) {
                if (state[h][w] > d+smallest) {
                    r1 = w+1;
                    break;
                }
            }
            t0 = min(t0, L0[h][r1]);
            t1 = max(t1, L1[h][r1]);
            if (t1-t0 > d) {
                r1 = -1;
                break;
            }
            if (R0[h][r1] <= smallest) {
                con = true;
            }
        }
        if (r1 != -1 && con) {
            ok = d;
            continue;
        }

        ng = d;
    }
    
    cout << ok << endl;

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}