#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

typedef pair<int, int> T;

int M,K;

// a <= m/M 
int unders(int m) {
    vector<int> count(M+1, 0);
    for (int n=2; n<=M; n++) {
        count[n] = n*m/M;
    }
    int cnt = 0;
    for (int n=2; n<=M; n++) {
        cnt += count[n];
        for (int l=2*n; l<=M; l+=n) {
            count[l] -= count[n];
        }
    }
    return cnt;
}

T subsolve(int tmpcnt, int m) {
    auto compare = [](T a, T b) {
        return a.first*b.second > b.first*a.second;
    };

    priority_queue<T, vector<T>, decltype(compare)> q {compare};

    for (int n=2; n<=M; n++) {
        int a = (m*n + M - 1)/M;
        while (__gcd(a, n) != 1) a++;
        q.push({a, n});
    }

    while (tmpcnt <= K) {
        T p = q.top(); q.pop();
        if (tmpcnt == K) return p;
        int a = p.first+1, b = p.second;
        while (__gcd(a, b) != 1) a++;
        q.push({a, b});
        tmpcnt++;
    }
    return {-1, -1};
}

T solve() {
    // m/M <= ans < (m+1)/M
    int l, r, m;
    l = 0; r = M;
    while (r-l > 1) {
        m = (r+l)/2;
        if (unders(m) >= K) {
            r = m;
        } else {
            l = m;
        }
    }
    if (l == M-1) return {-1, -1};
    if (K == 1) return {1, M};
    //cout << l << endl;
    return subsolve(unders(l), l);
}

int main() {
    cin >> M >> K;
    T ans = solve();
    if (ans.first == -1) cout << -1 << endl;
    else cout << ans.first << " " << ans.second << endl;
}