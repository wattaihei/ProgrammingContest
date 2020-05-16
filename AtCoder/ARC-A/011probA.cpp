#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int m, n, N; cin >> m >> n >> N;
    int ans = N, a = N, b = 0;
    while (a > 0){
        b += a%m;
        a = a/m * n;
        if (b >= m){
            a += b/m * n;
            b = b%m;
        }
        ans += a;
    }
    cout << ans << endl;
}