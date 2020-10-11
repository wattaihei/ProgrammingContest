#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

struct point {
    int h;
    int w;
};

int H, W;
point A[1000001];

int check(vector<vector<int>> &state, point p, int cango) {
    if (p.h == -1 || p.w == -1 || p.h == H || p.w == W || cango == -2 || state[p.h][p.w] == -1) return cango;
    if (state[p.h][p.w] == -2) return -2;
    if (cango == -1) return state[p.h][p.w];
    if (cango == state[p.h][p.w]) return cango;
    return -2;
}


int solve() {
    // -1 : not checked
    // -2 : have point more than 1
    // else : (only) number to go
    int ans = 0;
    vector<vector<int>> state(H, vector<int>(W, -1));
    for (int s=0; s<H*W; s++) {
        int cango = -1;
        point p = A[s];
        cango = check(state, {p.h, p.w+1}, cango);
        cango = check(state, {p.h, p.w-1}, cango);
        cango = check(state, {p.h+1, p.w}, cango);
        cango = check(state, {p.h-1, p.w}, cango);
        if (cango == -1) {
            state[p.h][p.w] = s;
        } else if (cango == -2) {
            //cout << p.h << " " << p.w << endl;
            state[p.h][p.w] = -2;
            ans++;
        } else {
            state[p.h][p.w] = cango;
        }
    }
    return ans;
}

int main() {
    cin >> H >> W;
    for (int h=0; h<H; h++) {
        for (int w=0; w<W; w++) {
            int a; cin >> a;
            A[a-1] = {h, w};
        }
    }
    cout << solve() << endl;
}