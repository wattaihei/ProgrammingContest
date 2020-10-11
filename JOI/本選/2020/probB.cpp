#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

const int INF = 1e9;
int N, K;
string S;

int solve() {
    vector<int> Ji, Oi, Ii;
    for (int i=0; i<N; i++) {
        if (S[i] == 'J') {
            Ji.push_back(i);
        } else if (S[i] == 'O') {
            Oi.push_back(i);
        } else {
            Ii.push_back(i);
        }
    }
    int ans = INF;
    int oi=0, ii=0;
    int j0, j1, o0, o1, i0, i1;
    for (int ji=0; ji<Ji.size()-K+1; ji++) {
        j0 = Ji[ji];
        j1 = Ji[ji+K-1];
        while (oi < Oi.size() && Oi[oi] < j1) oi++;
        if (oi+K-1 >= Oi.size()) break;
        o1 = Oi[oi+K-1];
        while (ii < Ii.size() && Ii[ii] < o1) ii++;
        if (ii+K-1 >= Ii.size()) break;
        i1 = Ii[ii+K-1];
        ans = min(ans, i1-j0+1-3*K);
    }
    if (ans == INF) return -1;
    return ans;
}

int main() {
    cin >> N >> K;
    cin >> S;
    cout << solve() << endl;
}