#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

int H, W, N;
int state[1001][1001];

pair<int, int> solve() {
    int count[H+1][W+1];
    for (int h=0; h<H+1; h++) {
        for (int w=0; w<W+1; w++) {
            count[h][w] = 0;
        }
    }
    count[0][0] = N-1;
    for (int h=0; h<H; h++) {
        for (int w=0; w<W; w++) {
            int c = count[h][w];
            if (c % 2 == 0) {
                count[h+1][w] += c/2;
                count[h][w+1] += c/2;
            } else {
                if (state[h][w] == 1) {
                    count[h+1][w] += c/2;
                    count[h][w+1] += (c+1)/2;
                    state[h][w] = 0;
                } else {
                    count[h+1][w] += (c+1)/2;
                    count[h][w+1] += c/2;
                    state[h][w] = 1;
                }
            }
        }
    }

    int h = 0, w = 0;
    while (h < H && w < W) {
        if (state[h][w] == 1) {
            w++;
        } else {
            h++;
        }
    }
    return {h+1, w+1};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> H >> W >> N;
    for (int h=0; h<H; h++) {
        for (int w=0; w<W; w++) {
            cin >> state[h][w];
        }
    }
    pair<int, int> p = solve();
    cout << p.first << " " << p.second << endl;
}