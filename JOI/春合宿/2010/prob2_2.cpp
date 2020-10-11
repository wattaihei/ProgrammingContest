#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

int solve(string S, unordered_set<string> Ss) {
    int M = S.size();
    vector<int> dp(M, INFINT);
    dp[0] = 0;
    for (int i=0; i<M; i++) {
        string t = "";
        int maxind = 0;
        for (int k=0; k<min(20, M-i); k++) {
            t += S[i+k];
            if (Ss.count(t)) {
                maxind = k;
            }
        }
        for (int k=1; k<=maxind; k++) {
            dp[i+k] = min(dp[i+k], dp[i]+1);
        }
    }
    return dp[M-1];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N; cin >> N;
    string S; cin >> S;
    unordered_set<string> Ss;
    for (int i=0; i<N; i++) {
        string s; cin >> s;
        Ss.insert(s);
    }
    cout << solve(S, Ss) << endl;
}