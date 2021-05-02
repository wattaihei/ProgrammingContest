#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;


void print(int query, int ans) {
    cout << "Case #" << query+1 << ": " << ans << endl;
}

int toint(char s) {
    return (int)(s-'0');
}

char tochar(int t) {
    return (char)(t + '0');
}


void solve(int q) {
    int N; cin >> N;
    string T = "";
    int ans = 0;
    for (int i=0; i<N; i++) {
        string S; cin >> S;
        int n = S.size();
        int m = T.size();
        if (n <= m) {
            int state = 0;
            for (int i=0; i<n; i++) {
                if (toint(S[i]) > toint(T[i])) {
                    state = 1;
                    break;
                } else if (toint(S[i]) < toint(T[i])) {
                    state = -1;
                    break;
                }
            }
            // cout << state << endl;
            if (state == 1 || state == -1) {
                while (S.size() < m) {
                    S += '0';
                    ans++;
                }
                if (state == -1) {
                    S += '0';
                    ans++;
                }
            } else if (state == 0) {
                int l = m-1;
                while (l >= n && toint(T[l]) == 9) {
                    l--;
                }
                if (l == n-1) {
                    while (S.size() < m+1) {
                        S += '0';
                        ans++;
                    }
                } else {
                    while (S.size() < l) {
                        S += T[S.size()];
                        ans++;
                    }
                    S += tochar(toint(T[l])+1);
                    ans++;
                    while (S.size() < m) {
                        S += '0';
                        ans++;
                    }
                }
            }
        }
        // cout << S << endl;
        T = S;
    }

    print(q, ans);

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q; cin >> Q;
    for (int q=0; q<Q; q++) {
        solve(q);
    }
}