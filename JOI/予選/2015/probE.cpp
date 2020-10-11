#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

struct point {
    int h;
    int w;
};

const int MAX = 1000;
int H, W;
int state[MAX][MAX];

int solve() {
    vector<point> stack;
    for (int h=0; h<H; h++) {
        for (int w=0; w<W; w++) {
            if (state[h][w] == 0) continue;
            int cnt = 0;
            for (int nh=h-1; nh<=h+1; nh++){
                for (int nw=w-1; nw<=w+1; nw++) {
                    if (state[nh][nw] == 0) cnt++;
                }
            }
            if (cnt >= state[h][w]) {
                stack.push_back({h, w});
            }
        }
    }

    int ans = 0;
    while (!stack.empty()) {
        ans++;
        set<int> nset;
        for (point p : stack) {
            state[p.h][p.w] = 0;
            for (int h=p.h-1; h<=p.h+1; h++) {
                for (int w=p.w-1; w<=p.w+1; w++) {
                    nset.insert(h*W+w);
                }
            }
        }
        stack = {};
        for (int r : nset) {
            point p;
            p.h = r/W; p.w = r%W;
            if (state[p.h][p.w] == 0) continue;
            int cnt = 0;
            for (int nh=p.h-1; nh<=p.h+1; nh++){
                for (int nw=p.w-1; nw<=p.w+1; nw++) {
                    if (state[nh][nw] == 0) cnt++;
                }
            }
            if (cnt >= state[p.h][p.w]) {
                stack.push_back({p.h, p.w});
            }
        }
    }
    return ans;
}

int main() {
    cin.tie(nullptr);
    cin >> H >> W;
    for (int h=0; h<H; h++) {
        string S; cin >> S;
        for (int w=0; w<W; w++) {
            if (S[w] == '.') state[h][w] = 0;
            else state[h][w] = (int)(S[w]-'0');
        }
    }
    cout << solve() << endl;
}