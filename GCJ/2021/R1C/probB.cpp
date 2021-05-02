#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 4e18;

void print(int query, string ans) {
    cout << "Case #" << query+1 << ": ";
    cout << ans << endl;
}

bool is_roaming(ll l) {
    string s = to_string(l);
    int r = s.size();
    string f = "";
    for (int i=0; i<r-1; i++) {
        f += s[i];
        ll p = atoll(f.c_str());
        int ind = i+1, num = p+1;
        bool ok = true;
        while (ind < r) {
            string g = to_string(num);
            if (ind + g.size() > r) { 
                ok = false;
                break;
            }
            for (int j=0; j<g.size(); j++) {
                if (g[j] != s[ind]) {
                    ok = false;
                    break;
                }
                ind++;
            }
            if (!ok) break;
            num++;
        }
        if (ok) return true;
    }
    return false;
}

bool bigger(string a, string b) {
    ll la = a.size(), lb = b.size();
    if (la > lb) {
        return true;
    }
    if (la < lb) {
        return false;
    }
    for (int i=0; i<la; i++) {
        if (a[i] > b[i]) return true;
        if (a[i] < b[i]) return false;
    }
    return true;
}

string subsolve(ll N, ll rep) {
    string Ns = to_string(N);
    ll ng = 0, ok = INFLL, m;
    while (abs(ok-ng) > 1) {
        m = (ok+ng)/2;
        string f = "";
        for (ll num=m; num<m+rep; num++) {
            f += to_string(num);
        }
        if (bigger(f, Ns)) {
            ok = m;
        } else {
            ng = m;
        }
    }
    ll num = ok;
    string f = "";
    for (ll t=num; t<num+rep; t++) {
        f += to_string(t);
    }
    return f;
}

void solve(int query) {
    ll N; cin >> N;
    ll s = to_string(N).size();

    string ans = "";
    for (int i=0; i<70; i++) {
        ans += "1";
    }
    for (int rep=2; rep<s+2; rep++) {
        string rt = subsolve(N+1, rep);
        // cout << rep << " " << rt << endl;
        if (bigger(ans, rt)) {
            ans = rt;
        }
    }
    print(query, ans);

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