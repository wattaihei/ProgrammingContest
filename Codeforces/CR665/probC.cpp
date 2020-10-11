#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q; cin >> Q;
    for (int q=0; q<Q; q++) {
        int N; cin >> N;
        vector<int> A, B;
        for (int i=0; i<N; i++) {
            int a; cin >> a;
            A.push_back(a);
        }
        B = A;
        sort(A.begin(), A.end());
        int p = A[0];
        bool ok = true;
        for (int i=0; i<N; i++) {
            if (A[i] != B[i]) {
                if (A[i]%p != 0) {
                    ok = false;
                }
            }
        }
        cout << (ok ? "YES" : "NO") << endl;
    }
}