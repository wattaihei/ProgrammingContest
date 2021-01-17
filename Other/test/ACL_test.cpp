#include <bits/stdc++.h>
#include <atcoder/modint>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;
using namespace atcoder;

using mint = modint1000000007;

istream &operator >>(istream &is,mint& x){//xにconst付けない
    ll t;is >> t;
    x=t;
    return (is);
}
ostream &operator <<(ostream &os,const mint& x){
    return os<<x.val();
}

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    mint a;
    cin >> a;
    cout << a/2 << endl;
    
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}