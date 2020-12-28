#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q; cin >> Q;
    for (int q=0; q<Q; q++) {
        int N; cin >> N;
        string S; cin >> S;
        for (int i=0; i<N; i++) {
            cout << S[N-1];
        }
        cout << endl;
    }
}