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
    int m1 = 0;
    for (int i=0; i<N-1; i++) {
        if (A[i] >= A[i+1]) {
            m1 = i+1;
        } else {
            break;
        }
    }
    int m2 = N-1;
    for (int i=N-1; i>0; i--) {
        if (A[i] >= A[i-1]) {
            m2 = i-1;
        } else {
            break;
        }
    }
    cout << ((m2 <= m1) ? "YES" : "NO") << endl; 
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