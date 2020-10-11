#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;


ll power(ll x, ll n, ll mod) {
    ll res = 1;
    while (n > 0) {
        if (n & 1) res = res * x % mod;
        x = x * x % mod;
        n >>= 1;
    }
    return res;
}

int solve(int n, int p) {
    map<int, int> S;
    for (int x=0; x<p; x++) {
        int q = power(x, n, p);
        if (S[q]) S[q]++; else S[q] = 1;
        //cout << q << " " << S[q] << endl;
    }
    //cout << endl;
    int cnt = 0;
    for (const auto& [v1, c1] : S) {
        //cout << v1 << " " << c1 << endl;
        for (const auto& [v2, c2] : S) {
            cnt += S[(v1+v2)%p] * c1 * c2;
        }
    }
    return cnt;
}

int main() {
    int n, p; cin >> p;
    cin >> n;
    cout << solve(n, p) << endl;
}