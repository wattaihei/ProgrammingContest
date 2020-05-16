#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    ll N, A, B; cin >> N >> A >> B;
    vector<ll> S(N);
    for (int i=0; i<N; i++){
        cin >> S[i];
    }
    ll S1 = *max_element(S.begin(), S.end());
    ll S2 = *min_element(S.begin(), S.end());

    if (S1 == S2){
        cout << -1 << endl;
    }
    else{
        double dS = S1 - S2;
        double P = B/(dS);
        double Q = A - P*accumulate(S.begin(), S.end(), 0.0)/(double)N;
        cout << fixed << setprecision(11);
        cout << P << ' ' << Q << endl;
    }
}