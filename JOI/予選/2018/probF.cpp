#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    int N, K; ll L; cin >> N >> K >> L;
    vector<int> A(N);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }
    int ng = 0, ok = (*max_element(A.begin(), A.end())) + 1;
    while (abs(ok-ng) > 1) {
        int m = (ok+ng)/2;
        int seq = 0;
        vector<int> B = {0};
        for (int i=0; i<N; i++) {
            if (A[i] <= m) {
                seq++;
            }
            B.push_back(seq);
        }
        ll c = 0ll; 
        int ind = 0;
        for (int i=0; i<N+1; i++) {
            while (B[i]-B[ind] >= K) ind++;
            c += (ll)(ind);
        }
        if (c >= L) {
            ok = m;
        } else {
            ng = m;
        }
    }

    cout << ok << endl;

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}