#include <bits/stdc++.h>
#include <atcoder/modint>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;
using namespace atcoder;

const int INFINT = 2e9;
const ll INFLL = 2e18;

using mint = modint1000000007;

istream &operator >>(istream &is,mint& x){//xにconst付けない
    ll t;is >> t;
    x=t;
    return (is);
}
ostream &operator <<(ostream &os,const mint& x){
    return os<<x.val();
}

void solve() {
    int N; cin >> N;
    vector<ll> A(N);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }

    int M = 60;
    vector<ll> B(M, 0ll);
    for (int i=0; i<N; i++) {
        ll a = A[i];
        for (int j=0; j<M; j++) {
            if ((1ll<<j)&a) {
                B[j]++;
            }
        }
    }

    mint ans = 0;
    for (int i=0; i<N; i++) {
        ll a = A[i];
        mint b = 0ll, c = 0ll;
        for (int j=0; j<M; j++) {
            if ((1ll<<j)&a) {
                b += (mint)(1ll<<j)*B[j];
                c += (mint)(1ll<<j)*N;
            } else {
                c += (mint)(1ll<<j)*B[j];
            }
        }
        ans += b*c;
    }

    cout << ans << endl;


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