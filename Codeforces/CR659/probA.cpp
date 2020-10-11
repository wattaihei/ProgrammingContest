#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

int N, T;
// vector<int> A;


int solve() {
    cin >> N;
    string S = "";
    for (int i=0; i<60; i++) {
        S += "a";
    }
    cout << S << endl;
    for (int i=0; i<N; i++) {
        int a; cin >> a;
        char s = S[a];
        if (s == 'a') {
            S[a] = 'b';
        } else {
            S[a] = 'a';
        }
        cout << S << endl;
    }

}


int main() {
    cin >> T;
    for (int t=0; t<T; t++){
        solve();
    }
}