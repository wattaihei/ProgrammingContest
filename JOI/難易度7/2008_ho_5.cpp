#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

int W, H;


int main() {
    cin >> W >> H;
    int N; cin >> N;
    int x1, y1, x2, y2;
    vector< vector<int> > board;
    set<int> Xs = {0, W}, Ys = {0, H};
    for (int i=0; i<N; i++) {
        cin >> x1 >> y1 >> x2 >> y2;
        board.push_back({x1, y1, x2, y2});
        Xs.insert(x1); Xs.insert(x2);
        Ys.insert(y1); Ys.insert(y2);
    }

    // 座標圧縮
    vector<int> ind_to_co_X, ind_to_co_Y;
    for (int x : Xs) {
        ind_to_co_X.push_back(x);
    }
    for (int y : Ys) {
        ind_to_co_Y.push_back(y);
    }
    sort(ind_to_co_X.begin(), ind_to_co_X.end());
    sort(ind_to_co_Y.begin(), ind_to_co_Y.end());

    unordered_map<int, int> co_to_ind_X, co_to_ind_Y;
    for (int i=0; i<ind_to_co_X.size(); i++) {
        co_to_ind_X[ind_to_co_X[i]] = i;
    }
    for (int i=0; i<ind_to_co_Y.size(); i++) {
        co_to_ind_Y[ind_to_co_Y[i]] = i;
    }

    int mX = ind_to_co_X.size(), mY = ind_to_co_Y.size();
    int grid[mX][mY];
    for (int i=0; i<mX; i++) {
        for (int j=0; j<mY; j++) {
            grid[i][j] = 0;
        }
    }
    grid[mX-1][0] = 1; grid[0][mY-1] = 1;

    for (auto tp : board) {
        x1 = co_to_ind_X[tp[0]];
        y1 = co_to_ind_Y[tp[1]];
        x2 = co_to_ind_X[tp[2]];
        y2 = co_to_ind_Y[tp[3]];
        grid[x1][y1]++;
        grid[x1][y2]--;
        grid[x2][y1]--;
        grid[x2][y2]++;
    }

    // imos
    for (int x=0; x<mX; x++) {
        //cout << endl;
        for (int y=0; y<mY; y++) {
            //cout << grid[x][y] << " ";
            if (x > 0) {
                grid[x][y] += grid[x-1][y];
            }
            if (y > 0) {
                grid[x][y] += grid[x][y-1];
            }
            if ( x > 0 && y > 0) {
                grid[x][y] -= grid[x-1][y-1];
            }
        }
    }

    //for (int x=0; x<mX; x++) grid[x][0]++;
    //for (int y=0; y<mY; y++) grid[0][y]++;

    // bfs
    int color = 0;
    int checked[mX][mY];
    for (int x=0; x<mX; x++) for (int y=0; y<mY; y++) checked[x][y] = 0;
    for (int x=0; x<mX; x++) {
        //cout << endl;
        for (int y=0; y<mY; y++) {
            //cout << grid[x][y] << " ";
            if (grid[x][y] > 0 || checked[x][y]) continue;
            color++;
            queue<pair<int, int>> q;
            vector<pair<int, int>> nexts;
            q.push({x, y});
            checked[x][y] = 1;
            while (q.size() != 0) {
                pair<int, int> p = q.front();
                x1 = p.first; y1 = p.second;
                q.pop();

                nexts = {};
                if (x1 > 0) nexts.push_back({x1-1, y1});
                if (x1 < mX-1) nexts.push_back({x1+1, y1});
                if (y1 > 0) nexts.push_back({x1, y1-1});
                if (y1 < mY-1) nexts.push_back({x1, y1+1});
                for (auto pa : nexts) {
                    x2 = pa.first, y2 = pa.second;
                    if (grid[x2][y2] == 0 && !checked[x2][y2]) {
                        checked[x2][y2] = 1;
                        q.push({x2, y2});
                    }
                }
            }
        }
    }

    cout << color << endl;


}