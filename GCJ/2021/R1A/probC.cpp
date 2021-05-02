#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void print(int query, string S, ll f, ll g) {
    cout << "Case #" << query+1 << ": " << S << " " << f << "/" << g << endl;
}


char inv(char s) {
    return s == 'F' ? 'T' : 'F';
}

void solve(int q) {
    int N, Q; cin >> N >> Q;
    vector<string> Ss;
    vector<int> A;
    for (int i=0; i<N; i++) {
        string S; cin >> S;
        int a; cin >> a;
        Ss.push_back(S);
        A.push_back(a);
    }

    if (N == 1) {
        int a = A[0];
        string S;
        for (int i=0; i<Q; i++) {
            if (Q-a > a) {
                S += inv(Ss[0][i]);
            } else {
                S += Ss[0][i];
            }
        }
        int ans = max(Q-a, a);
        print(q, S, ans, 1);
    } else if (N == 2) {
        int a = 0;
        unordered_set<int> us;
        for (int i=0; i<Q; i++) {
            if (Ss[0][i] == Ss[1][i]) { 
                a++;
                us.insert(i);
            }
        }
        int b = Q-a;
        int n = A[0];
        int m = A[1];
        int i = (n+m-b)/2;
        int j = (n-m+b)/2;
        int ans = max(i, a-i) + max(j, b-j);
        string S;
        int x = 0, y = 0;
        for (int h=0; h<Q; h++) {
            if (us.count(h)) {
                if (i >= a-i) {
                    if (x < i) {
                        S += Ss[0][h];
                        x++;
                    } else {
                        S += inv(Ss[0][h]);
                    }
                } else {
                    if (x < a-i) {
                        S += inv(Ss[0][h]);
                        x++;
                    } else {
                        S += Ss[0][h];
                    }
                }
            } else {
                if (j >= b-j) {
                    S += Ss[0][h];
                } else {
                    S += inv(Ss[0][h]);
                }
            }
            // cout << y << " " << j << endl;
        }
        print(q, S, ans, 1);
    }

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