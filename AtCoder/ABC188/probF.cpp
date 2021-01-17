#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

template <typename T>
bool chmax(T &a, const T& b) {
  if (a < b) {
    a = b;
    return true;
  }
  return false;
}

template <typename T>
bool chmin(T &a, const T& b) {
  if (a > b) {
    a = b;
    return true;
  }
  return false;
}


const int INFINT = 2e9;
const ll INFLL = 2e18;




ll solve(ll x, ll y) {
    ll ans = INFLL;
    unordered_map<ll, ll> mp;
    unordered_set<ll> q = {y}, qq;
    mp[y] = -INFLL;
    while (!q.empty()) {
        qq.clear();
        for (ll p : q) {
            chmin(ans, INFLL+mp[p]+abs(p-x));
            if (p > x) {
                if (p%2 == 0) {
                    chmin(mp[p/2], mp[p]+1);
                    qq.insert(p/2);
                } else {
                    chmin(mp[p/2+1], mp[p]+2);
                    chmin(mp[p/2], mp[p]+2);
                    qq.insert(p/2+1);
                    qq.insert(p/2);
                }
            }
        }
        q = qq;
    }

    return ans;
}

ll solve2(ll x, ll y) {
    vector<ll> dp(y*2+1, INFLL), q = {x}, qq;
    dp[x] = 0ll;
    while (!q.empty()) {
        qq.clear();
        for (ll p : q) {
            if (p+1 <= 2*y && dp[p+1] > dp[p] + 1) {
                dp[p+1] = dp[p] + 1;
                qq.push_back(p+1);
            }
            if (p-1 >= 1 && dp[p-1] > dp[p] + 1) {
                dp[p-1] = dp[p] + 1;
                qq.push_back(p-1);
            }
            if (p*2 <= 2*y && dp[p*2] > dp[p] + 1) {
                dp[p*2] = dp[p] + 1;
                qq.push_back(p*2);
            }
        }
        q = qq;
    }
    return dp[y];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll x, y; cin >> x >> y;
    cout << solve(x, y) << endl; 
    // for (int x=1; x<100; x++) {
    //     for (int y=1; y<100; y++) {
    //         ll ans1 = solve(x, y);
    //         ll ans2 = solve2(x, y);
    //         if (ans1 != ans2) {
    //             cout << x << " " << y << endl;
    //         }
    //     }
    // }
}