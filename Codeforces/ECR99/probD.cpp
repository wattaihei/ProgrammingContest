#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    int N, X; cin >> N >> X;
    vector<int> A(N);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }
    bool increase = true;
    for (int i=0; i<N-1; i++) {
        if (A[i] > A[i+1]) {
            increase = false;
            break;
        }
    }
    int ans = INFINT;
    if (increase) {
        cout << 0 << endl;
        return;
    }
    for (int i=0; i<N; i++) {
        vector<int> B;
        for (int j=0; j<N; j++) {
            if (i != j) {
                B.push_back(A[j]);
            }
        }
        B.push_back(X);
        sort(B.begin(), B.end());
        vector<int> C = {X}, D;
        for (int j=0; j<N; j++) {
            if (A[j] != B[j]) {
                C.push_back(A[j]);
                D.push_back(B[j]);
            }
        }
        bool ok = true;
        for (int j=0; j<D.size(); j++) {
            if (C[j] != D[j]) {
                ok = false;
                break;
            }
        }
        if (!D.empty() && C[C.size()-1] < D[D.size()-1]) {
            ok = false;
        }
        if (ok) {
            ans = min(ans, (int)(D.size()));
        }
    }
    cout << (ans == INFINT ? -1 : ans) << endl;

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