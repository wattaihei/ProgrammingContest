#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

const int MAXN = 100;

vector<vector<int>> state(MAXN);

void change(vector<int> r) {
    state[r[0]][r[1]] ^= 1;
    state[r[2]][r[3]] ^= 1;
    state[r[4]][r[5]] ^= 1;
}

vector<int> check(int h, int w) {
    vector<int> ret;
    if (state[h][w]) {
        if (state[h+1][w]) {
            ret = {h, w, h+1, w, h, w+1};
            change(ret);
            return ret;
        } else {
            ret = {h, w, h, w+1, h+1, w+1};
            change(ret);
            return ret;
        }
    } else {
        if (state[h+1][w]) {
            ret = {h+1, w, h, w+1, h+1, w+1};
            change(ret);
            return ret;
        } else {
            return ret;
        }
    }
}

vector<int> check2(int h, int w) {
    vector<int> ret;
    if (state[h][w]) {
        if (state[h][w+1]) {
            ret = {h, w, h+1, w, h, w+1};
            change(ret);
            return ret;
        } else {
            ret = {h, w, h+1, w, h+1, w+1};
            change(ret);
            return ret;
        }
    } else {
        if (state[h][w+1]) {
            ret = {h, w+1, h+1, w, h+1, w+1};
            change(ret);
            return ret;
        } else {
            return ret;
        }
    }
}

vector<int> dig(int h, int w) {
    vector<int> ret;
    vector<int> points = {h, w, h+1, w, h, w+1, h+1, w+1};
    int a00 = state[h][w], a10 = state[h+1][w], a01 = state[h][w+1], a11 = state[h+1][w+1];
    int s = a00 + a10 + a01 + a11;
    if (s == 4) {
        ret = {h, w, h+1, w, h, w+1};
        change(ret);
        return ret;
    } else if (s == 3) {
        for (int i=0; i<4; i++) {
            int nh = points[2*i], nw = points[2*i+1];
            if (!state[nh][nw]) {
                for (int j=0; j<4; j++) {
                    if (i!=j) {
                        ret.push_back(points[2*j]);
                        ret.push_back(points[2*j+1]);
                    }
                }
                change(ret);
                return ret;
            } 
        }
    } else if (s == 2) {
        for (int i=0; i<4; i++) {
            int nh = points[2*i], nw = points[2*i+1];
            if (state[nh][nw]) {
                for (int j=0; j<4; j++) {
                    if (i!=j) {
                        ret.push_back(points[2*j]);
                        ret.push_back(points[2*j+1]);
                    }
                }
                change(ret);
                return ret;
            } 
        }
    } else if (s == 1) {
        for (int i=0; i<4; i++) {
            int nh = points[2*i], nw = points[2*i+1];
            if (!state[nh][nw]) {
                for (int j=0; j<4; j++) {
                    if (i!=j) {
                        ret.push_back(points[2*j]);
                        ret.push_back(points[2*j+1]);
                    }
                }
                change(ret);
                return ret;
            } 
        }
    } else {
        return ret;
    }
}

void solve() {
    int N, M; cin >> N >> M;

    for (int i=0; i<N; i++) {
        string S;
        cin >> S;
        vector<int> T;
        for (int j=0; j<M; j++) {
            T.push_back(S[j]-'0');
        }
        state[i] = T;
    }

    vector<vector<int>> ans;
    for (int i=0; i<N-1; i+=2) {
        for (int j=0; j<M-2; j++) {
            vector<int> ret = check(i, j);
            if (!ret.empty()) {
                ans.push_back(ret);
            }
        }
    }
    if (N%2 != 0) {
        int i = N-2;
        for (int j=0; j<M-2; j++) {
            vector<int> ret = check(i, j);
            if (!ret.empty()) {
                ans.push_back(ret);
            }
        }
    }

    for (int j=0; j<N-2; j++) {
        vector<int> ret = check2(j, M-2);
        if (!ret.empty()) {
            ans.push_back(ret);
        }
    }

    vector<int> ret;
    while (true) {
        ret = dig(N-2, M-2);
        if (ret.empty()) {
            break;
        }
        ans.push_back(ret);
    }

    cout << ans.size() << endl;
    for (int i=0; i<ans.size(); i++) {
        for (int j=0; j<6; j++) {
            cout << ans[i][j]+1 << " ";
        }
        cout << endl;
    }

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q; cin >> Q;
    for (int q=0; q<Q; q++) {
        solve();
    }
}