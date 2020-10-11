#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

int N;
vector<pair<ll, ll>> AB;


ll solve() {
    sort(AB.begin(), AB.end());
    ll ans = AB[N-1].second;
    ll s = 0;
    ll kmin = 0;
    for (int i=0; i<N; i++) {
        ll a = AB[i].first, b = AB[i].second;
        //cout << a << " " << b << endl;
        kmin = min(kmin, s-a);
        s += b;
        ans = max(ans, s-a-kmin);
    }
    return ans;
}

int main() {
    cin >> N;
    for (int i=0; i<N; i++){
        ll a, b; cin >> a >> b;
        AB.push_back({a, b});
    }
    cout << solve() << endl;
}