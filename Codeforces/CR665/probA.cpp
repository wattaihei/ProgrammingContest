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
        int a, k; cin >> a >> k;
        int ans = abs(k-a);
        if (k < a) {
            ans = min(ans, (a-k)%2);
        }
        cout << ans << endl;
    }
}