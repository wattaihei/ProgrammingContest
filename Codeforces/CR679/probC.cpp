#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    ll A[6];
    for (int i=0; i<6; i++) cin >> A[i];
    int N; cin >> N;
    ll B[N];
    vector<pair<ll, int>> C;
    for (int i=0; i<N; i++) {
        cin >> B[i];
        for (int k=0; k<6; k++) {
            C.push_back({B[i]-A[k], i});
        }
    }
    sort(C.begin(), C.end());
    int csize = C.size();

    // for (auto c : C) {
    //     cout << c.first << " ";
    // }
    // cout << endl;
    // for (auto c : C) {
    //     cout << c.second << " ";
    // }
    // cout << endl;
    
    ll ans = 1e18;
    map<int, queue<ll>> P;
    int r = 0;
    for (auto l=0; l<csize; l++) {
        while (P.size() < N && r < csize) {
            pair<ll, int> p = C[r];
            P[p.second].push(p.first);
            r++;
        }
        // cout << l << " " << r << endl;
        if (r == csize && P.size() < N) break;
        pair<ll, int> np = C[l];
        ans = min(ans, C[r-1].first-np.first);
        P[np.second].pop();
        if (P[np.second].empty()) {
            P.erase(P.find(np.second));
        }
    }
    cout << ans << endl;


    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}