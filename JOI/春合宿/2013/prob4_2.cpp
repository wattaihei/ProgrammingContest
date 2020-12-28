#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;
const int MAXN = 100000;

int N; 
int A[MAXN];
ll B[MAXN], C[MAXN], D[MAXN];

void solve() {
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> A[i] >> B[i] >> C[i] >> D[i];
    }

    vector<int> checked(N, 0);
    ll ans = 0ll;
    for (int i=0; i<N; i++) {
        int n = i;
        vector<int> stack;
        while (!checked[n]) {
            stack.push_back(n);
            checked[n] = 1;
            n = A[n]-1;
        }
        for (int i=0; i<stack.size(); i++) {
            int p = stack[i];
            if (p == n) {
                vector<ll> ds;
                ll score = 0ll;
                for (int j=i; j<stack.size(); j++) {
                    int q = stack[j];
                    int nq = A[q]-1;
                    score += B[q]*C[nq];
                    ds.push_back(B[q]*D[nq] - B[q]*C[nq]);
                }
                sort(ds.begin(), ds.end(), greater<ll>());
                for (int j=0; j<ds.size()/2; j++) {
                    ll s = ds[2*j] + ds[2*j+1];
                    if (s > 0) {
                        score += s;
                    }
                }
                ans += score;
                break;
            } else {
                int np = A[p]-1;
                ans += max(B[p]*C[np], B[p]*D[np]);
            }
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