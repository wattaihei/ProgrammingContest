#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    int N; cin >> N;
    ll X; cin >> X;
    vector<ll> A(N), B(N), C(N);
    set<ll> S;
    for (int i=0; i<N; i++) {
        cin >> A[i] >> B[i] >> C[i];
        S.insert(A[i]);
        S.insert(A[i]-1);
        S.insert(B[i]);
        S.insert(B[i]+1);
    }

    S.insert(0);
    S.insert(1);

    vector<ll> ind_to_co;
    unordered_map<ll, int> co_to_ind;
    for (auto a : S) {
        ind_to_co.push_back(a);
        co_to_ind[a] = ind_to_co.size()-1;
    }

    vector<ll> D(ind_to_co.size()+1, 0ll); 
    for (int i=0; i<N; i++) {
        D[co_to_ind[A[i]]] += C[i];
        D[co_to_ind[B[i]+1]] -= C[i];
    }

    ll ans = 0ll;
    for (int i=1; i<D.size()-1; i++) {
        ans += min(D[i], X)*(ind_to_co[i+1]-ind_to_co[i]);
        D[i+1] += D[i];
    }

    cout << ans << endl;

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}