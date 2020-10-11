#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

int N;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> N;
    map<int, int> A;
    for (int i=0; i<N; i++) {
        int a; cin >> a;
        A[a] += 1;
    }
    vector<int> B(9, 0);
    for (auto &[a, b] : A) {
        B[min(8,b)] += 1;
    }
    int Q; cin >> Q;
    for (int q=0; q<Q; q++) {
        char s;
        int n;
        cin >> s >> n;
        int k = A[n];
        B[min(k,8)] -= 1;
        if (s == '+') {
            A[n] += 1;
            k += 1;
        } else {
            A[n] -= 1;
            k -= 1;
        }
        B[min(k,8)] += 1;
        int cnt2 = 2*B[8];
        for (int i=4; i<8; i++) {
            cnt2 += B[i];
        }
        bool ok;
        if (cnt2 >= 2) {
            ok = true;
        } else if (cnt2 == 0) {
            ok = false;
        } else {
            int cnt1 = B[2] + B[3] + B[6] + B[7];
            if (cnt1 > 1) {
                ok = true;
            } else {
                ok = false;
            }
        }
        cout << (ok ? "YES" : "NO") << endl;
    }
}