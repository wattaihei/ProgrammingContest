#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;


void print(int query, int ans) {
    cout << "Case #" << query+1 << ": " << ans << endl;
}

void solve(int c) {
    int N; cin >> N;
    vector<int> A(N);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }

    int ans = 0;
    for (int i=0; i<N-1; i++) {
        int j = i, m = INFINT;
        for (int k=i; k<N; k++) {
            int a = A[k];
            if (a < m) {
                m = a;
                j = k;
            }
        }

        ans += j-i+1;
        // reverse
        vector<int> B = A;
        for (int k=i; k<=j; k++) {
            B[k] = A[j+i-k];
        }
        A = B;
        // cout << ans << endl;
    }

    print(c, ans);

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q; cin >> Q;
    for (int q=0; q<Q; q++) {
        solve(q);
    }
}