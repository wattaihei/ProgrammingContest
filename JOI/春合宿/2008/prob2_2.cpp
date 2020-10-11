#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

const int INF = 2e9;
int N, M;
vector<int> X, Y;


bool isOK(int m) {
    int need = 0;

    int prex = -INF;
    for (int x : X) {
        if (prex + m < x) {
            need++;
            prex = x;
        }
    }
    int prey = -INF;
    for (int y : Y) {
        if (prey + m < y) {
            need++;
            prey = y;
        }
    }

    return need <= N;
}


int solve() {
    sort(X.begin(), X.end());
    sort(Y.begin(), Y.end());
    int l,r,m;
    l = -1;
    r = 1e9+8;
    while (r-l > 1) {
        m = (r+l)/2;
        if (isOK(m)) r = m;
        else l = m;
    }
    return r;
}

int main() {
    cin >> N >> M;
    for (int m=0; m<M; m++) {
        int x, y;
        cin >> x >> y;
        X.push_back(x);
        Y.push_back(y);
    }
    cout << solve() << endl;
}