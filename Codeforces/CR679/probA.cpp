#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    int N; cin >> N;
    int A[N];
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }
    for (int i=0; i<N/2; i++) {
        cout << A[2*i+1] << " ";
        cout << A[2*i]*(-1);
        if (i != N/2-1) {
            cout << " ";
        }
    }
    cout << endl;
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