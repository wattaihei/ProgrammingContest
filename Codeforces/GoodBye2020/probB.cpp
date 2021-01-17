#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    int N; cin >> N;
    vector<int> A(N);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }

    sort(A.begin(), A.end());

    unordered_set<int> B;
    for (int i=0; i<N; i++) {
        int a = A[i];
        if (B.count(a)) {
            B.insert(a+1);
        } else {
            B.insert(a);
        }
    }

    cout << B.size() << endl;

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