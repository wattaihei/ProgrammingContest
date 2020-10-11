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
        int x1, y1, z1, x2, y2, z2;
        cin >> x1 >> y1 >> z1 >> x2 >> y2 >> z2;
        int ans = 0;
        if (z1 > y2) {
            ans += 2*y2;
            z1 -= y2;
        } else {
            ans += 2*z1;
            z1 = 0;
        }
        ans -= 2*max(z2-(z1+x1), 0);


        cout << ans << endl;
    }
}