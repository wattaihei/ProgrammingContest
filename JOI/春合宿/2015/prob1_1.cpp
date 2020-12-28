#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;
const int MAXN = 200000;


int K, N;
ll M;
string S;
ll A[MAXN], B[MAXN], C[MAXN];

void solve() {
    cin >> K >> M;
    cin >> S;
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> A[i] >> B[i] >> C[i];
    }
    string ans = "";
    for (int k=0; k<K; k++) {
        ll n = k;
        for (int i=N-1; i>=0; i--) {
            ll a = A[i], b = B[i], c = C[i];
            if (c <= n && n < c + (b-a)) {
                n = a + (n-c);
            } else if (c + (b-a) <= n) {
                n -= (b-a);
            }
        }
        ans += S[n];
    }
    cout << ans << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}