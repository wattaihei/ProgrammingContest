#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

int main() {
    int A, B, C, K, S, T;
    cin >> A >> B >> C >> K >> S >> T;
    int ans = A*S + B*T;
    if (S+T >= K){
        ans -= C*(S+T);
    }
    cout << ans << endl;
}