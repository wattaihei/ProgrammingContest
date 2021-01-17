#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    int N; cin >> N;
    int M = (1<<N);
    vector<ll> A(M);
    vector<int> S;
    for (int i=0; i<M; i++) {
        cin >> A[i];
        S.push_back(i);
    }

    while (S.size() > 2) {
        vector<int> T;
        for (int i=0; i<S.size()/2; i++) {
            int i1 = S[2*i], i2 = S[2*i+1];
            if (A[i1] > A[i2]) {
                T.push_back(i1);
            } else {
                T.push_back(i2);
            }
        }
        S = T;
    }

    cout << (A[S[0]] < A[S[1]] ? S[0]+1 : S[1]+1) << endl;

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}