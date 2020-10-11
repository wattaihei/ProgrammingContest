#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M; cin >> N >> M;
    int A[N], B[M];
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }
    for (int i=0; i<M; i++) {
        cin >> B[i];
    }

    int ans = (1<<9);
    for (int bit=0; bit<(1<<9); bit++) {
        bool good = true;
        for (int i=0; i<N; i++) {
            int a = A[i];
            bool ok = false;
            for (int j=0; j<M; j++) {
                int b = (a & B[j]);
                if (((bit|b) == bit) && ((bit&b) == b)) {
                    ok = true;
                    //cout << bit << " " << b << endl;
                    break;
                }
            }
            if (!ok) {
                good = false;
                break;
            }
        }
        if (good) {
            ans = min(ans, bit);
        }
    }
    cout << ans << endl;
}