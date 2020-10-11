#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, D, M; cin >> N >> D >> M;
    vector<int> A,B;
    for (int i=0; i<N; i++) {
        int a; cin >> a;
        if (a > M) {
            A.push_back(a);
        } else {
            B.push_back(a);
        }
    }
    sort(A.begin(), A.end(), greater<int>());
    sort(B.begin(), B.end(), greater<int>());
    vector<ll> BB = {0};
    ll b = 0;
    for (int i=0; i<B.size(); i++) {
        b += (ll)B[i];
        BB.push_back(b);
    }
    ll ans = b;
    ll p = 0;
    for (int i=0; i<A.size(); i++) {
        int reml = min(N - ((D+1)*i + 1), (int)BB.size()-1);
        if (reml < 0) break;
        p += (ll)A[i];
        ans = max(ans, p + BB[reml]);
        //cout << ans << endl;
    }
    cout << ans << endl;
}