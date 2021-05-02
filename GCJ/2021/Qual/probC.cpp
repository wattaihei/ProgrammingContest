#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void print(int query, vector<int> ans) {
    cout << "Case #" << query+1 << ":";
    for (int  a : ans) {
        cout <<  " " << a;
    }
    cout << endl;
}

void print_imp(int query) {
    cout << "Case #" << query+1 << ": IMPOSSIBLE" << endl;
}

void solve(int query) {
    int N, C; cin >> N >> C;
    if (C < N-1 || N*(N+1)/2-1 < C) {
        print_imp(query);
        return;
    }
    int remain = C - (N-1);
    vector<int> A = {N};
    for (int i=0; i<N-1; i++) {
        int n = N-i-1;
        int ind = 0;
        if (remain == 0) {
            ind = 0;
        } else if (remain > i+1) {
            ind = i+1;
        } else {
            ind = remain;
        }

        vector<int> B;
        for (int j=ind-1; j>=0; j--) {
            B.push_back(A[j]);
        }
        B.push_back(n);
        for (int j=ind; j<i+1; j++) {
            B.push_back(A[j]);
        }
        A = B;
        remain -= ind;
    }
    
    print(query, A);

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