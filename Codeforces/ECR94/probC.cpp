#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

int solve(string S, int x) {
    int L = S.size();
    vector<int> W(L, 1);
    for (int i=0; i<L; i++) {
        if (S[i] == '0') {
            if (i-x >= 0) {
                W[i-x] = 0;
            } 
            if (i+x < L) {
                W[i+x] = 0;
            }
        }
    }
    for (int i=L-x; i<x; i++) {
        W[i] = 0;
    }
    for (int i=0; i<L; i++) {
        if (S[i] == '1') {
            if (!(((i-x >= 0) && (W[i-x] == 1)) || ((i+x < L) && (W[i+x] == 1)))) {
                cout << -1 << endl;
                return 0;
            }
        }
    }
    for (int i=0; i<L; i++) {
        cout << W[i];
    }
    cout << endl;
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q; cin >> Q;
    for (int q=0; q<Q; q++) {
        string S; cin >> S;
        int x; cin >> x;
        solve(S, x);
    }
}