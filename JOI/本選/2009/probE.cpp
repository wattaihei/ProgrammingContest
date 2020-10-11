#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

typedef tuple<int, int, int> T;

const int INFINT = 2e9;
const ll INFLL = 2e18;

int R, W, H, X, Y;


vector<int> solve(int W, int H, int X, int Y, vector<vector<int>> state) {
    vector<int> ret = {0};
    vector<vector<bool>> checked(H, vector<bool>(W, false));
    priority_queue<T, vector<T>, greater<T>> q;
    q.push({state[Y][X], Y, X});
    int tmpmax = 0;
    while (!q.empty()) {
        T p = q.top(); q.pop();
        int s = get<0>(p);
        int h = get<1>(p);
        int w = get<2>(p);
        if (checked[h][w]) continue;
        if (s == INFINT) break;
        checked[h][w] = true;
        tmpmax = max(s, tmpmax);
        ret.push_back(tmpmax);
        q.push({state[h+1][w], h+1, w});
        q.push({state[h-1][w], h-1, w});
        q.push({state[h][w-1], h, w-1});
        q.push({state[h][w+1], h, w+1});
    }
    return ret;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> R;
    vector<int> V[2];
    for (int i=0; i<2; i++) {
        cin >> W >> H >> X >> Y;
        vector<vector<int>> state(H+2, vector<int>(W+2));
        for (int h=0; h<H+2; h++) {
            for (int w=0; w<W+2; w++) {
                if (h == 0 || h == H+1 || w == 0 || w == W+1) {
                    state[h][w] = INFINT;
                } else {
                    cin >> state[h][w];
                }
            }
        }
        V[i] = solve(W+2, H+2, X, Y, state);
    }
    int ans = INFINT;
    // for (auto v : V[0]) cout << v << " ";
    // cout << endl;
    // for (auto v : V[1]) cout << v << " ";
    // cout << endl;
    for (int i=max(0, R+1-(int)V[1].size()); i<min((int)V[0].size(), R+1); i++) {
        // 0 <= r - i - 2 <= V1.size - 1
        ans = min(ans, V[0][i] + V[1][R-i]);
    }
    cout << ans << endl;
}