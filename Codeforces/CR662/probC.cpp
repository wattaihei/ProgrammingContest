#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

bool isOK(int interval, vector<int> C) {
    priority_queue<int> q;
    for (int c : C) {
        q.push(c);
    }
    while (!q.empty()) {
        vector<int> P;
        for (int i=0; i<interval; i++) {
            if (q.empty()) {
                return P.empty();
            }
            int k = q.top(); q.pop();
            if (k > 1) {
                P.push_back(k-1);
            }
        }
        for (int p : P) {
            q.push(p);
        }
    }
    return true;
}

int solve(int N, vector<int> A) {
    map<int, int> B;
    for (auto a : A) {
        B[a] += 1;
    }
    vector<int> C;
    for (auto &[a, b] : B) {
        C.push_back(b);
    }
    sort(C.begin(), C.end());
    reverse(C.begin(), C.end());
    int ok = 1, ng = N, m;
    while (ng - ok > 1) {
        m = (ok+ng)/2;
        if (isOK(m, C)) {
            ok = m;
        } else {
            ng = m;
        }
    }
    return ok - 1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q; cin >> Q;
    for (int q=0; q<Q; q++) {
        int N; cin >> N;
        vector<int> A;
        for (int i=0; i<N; i++) {
            int a; cin >> a;
            A.push_back(a);
        }
        cout << solve(N, A) << endl;
    }
}