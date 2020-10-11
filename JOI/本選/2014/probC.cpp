#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

ll solve(int N, ll *A) {
    ll S = 0; 
    vector<ll> E = {0};
    for (int i=0; i<N; i++) {
        S += A[i];
        E.push_back(S);
    }
    for (int i=0; i<N; i++) {
        E.push_back(E[E.size()-1] + A[i]);
    }
    E.push_back(E[E.size()-1] + A[0]);
    int ind1 = 0, ind2 = 0;
    ll ans = 0;
    for (int ind0=0; ind0<N; ind0++) {
        while ((E[ind1+1] - E[ind0])*3 < S) {
            ind1++;
        }
        while ((E[ind2+1] - E[ind0])*3 < S*2) {
            ind2++;
        }
        ll s1 = E[ind1] - E[ind0], s2 = E[ind2] - E[ind1];
        ll d1 = E[ind1+1] - E[ind1], d2 = E[ind2+1] - E[ind2];
        vector<vector<ll>> R = {
            {s1, s2, S-s1-s2},
            {s1+d1, s2-d1, S-s1-s2},
            {s1, s2+d2, S-s1-s2-d2},
            {s1+d1, s2+d2-d1, S-s1-s2-d2}
        };
        for (auto r : R) {
            ll s = *min_element(r.begin(), r.end());
            if (s > ans) {
                ans = s;
            }
        }
    }
    return ans;
}

int main() {
    int N; cin >> N;
    ll A[N];
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }
    cout << solve(N, A) << endl;
}