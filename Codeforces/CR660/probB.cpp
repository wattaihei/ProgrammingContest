#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

string solve(int N) {
    string ret = "";
    if (N%4 == 0) {
        for (int i=0; i<3*N/4; i++) {
            ret += "9";
        }
        for (int i=0; i<N/4; i++) {
            ret += "8";
        }
    } else {
        for (int i=0; i<3*N/4; i++) {
            ret += "9";
        }
        ret += "8";
        for (int i=0; i<N/4; i++) {
            ret += "8";
        }
    }
    return ret;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q; cin >> Q;
    for (int q=0; q<Q; q++) {
        int N; cin >> N;
        cout << solve(N) << endl;
    }
}