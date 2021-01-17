#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    ll N; cin >> N;
    int M; cin >> M;
    vector<int> seq(M*M, -1), A;
    ll a = 1;
    int last = 0;
    seq[1] = 0;
    A.push_back(1);
    for (int m=0; m<M*M+4; m++) {
        a = a*10ll % (M*M);
        if (seq[a] != -1) {
            last = m+1;
            break;
        }
        A.push_back(a);
        seq[a] = m+1;
    }

    ll m2 = -1;
    if (N < (ll)last) {
        m2 = A[N];
    } else {
        N -= seq[a];
        N %= (last - seq[a]);
        N += seq[a];
        m2 = A[N];
    }

    cout << (m2/M) << endl;

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}