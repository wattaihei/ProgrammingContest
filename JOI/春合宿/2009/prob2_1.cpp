#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

const ll mod = 1e7;
int W, H, N;
string S;


ll subsolve(int size, vector<int> L) {
    vector<ll> dp(size+1, 0ll);
    dp[0] = 1ll;
    for (auto l : L) {
        //cout << l << " ";
        if (l == 1){
            ll c = dp[0];
            dp[0] = 0ll;
            for (int i=0; i<size; i++) {
                ll d = dp[i+1];
                dp[i+1] = c;
                c = (c + d) % mod;
            }
        } else {
            ll c = dp[size];
            dp[size] = 0;
            for (int i=size; i>0; i--) {
                ll d = dp[i-1];
                dp[i-1] = c;
                c = (c + d) % mod;
            }
        }
    }
    //cout << endl;
    return dp[size];
}

ll solve() {
    vector<int> A,B;
    int seq = S[0] == 'R' ? 0 : 1;
    if (seq == 0) {
        A.push_back(1);
    } else {
        B.push_back(1);
    }

    for (auto s : S) {
        if (s == 'L') {
            seq = (seq == 0 ? 3 : (seq - 1));
        } else {
            seq = (seq + 1) % 4;
        }
        if (seq == 0) {
            A.push_back(1);
        } else if (seq == 1) {
            B.push_back(1);
        } else if (seq == 2) {
            A.push_back(-1);
        } else {
            B.push_back(-1);
        }
    }

    ll a = subsolve(H, A);
    ll b = subsolve(W, B);
    return (a*b) % mod;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> W >> H;
    cin >> N;
    cin >> S;
    cout << solve() << endl;
}