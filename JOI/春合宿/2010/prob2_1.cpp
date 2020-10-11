#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

vector<pair<int, ll>> solve(int M1, vector<pair<int, ll>> P1, int M2, vector<pair<int, ll>> P2) {
    vector<pair<int, ll>> ret, ret2;
    reverse(P1.begin(), P1.end());
    reverse(P2.begin(), P2.end());

    vector<pair<int, ll>> R;
    ll indsum1 = 0, indsum2 = 0;
    int ind1 = 0;
    for (auto &[a2, b2] : P2) {
        indsum2 += b2;
        while (ind1 < P1.size() && indsum1 + P1[ind1].second <= indsum2) {
            R.push_back({P1[ind1].first + a2, P1[ind1].second});
            indsum1 += P1[ind1].second;
            ind1++;
        }
        if (indsum1 < indsum2) {
            if (ind1 < P1.size()) {
                R.push_back({P1[ind1].first + a2, indsum2 - indsum1});
                P1[ind1].second -= (indsum2 - indsum1);
                indsum1 = indsum2;
            } else {
                R.push_back({a2, min(indsum2 - indsum1, b2)});
            }
        }
    }

    while (ind1 < P1.size()) {
        R.push_back(P1[ind1]);
        ind1++;
    }


    int upnum = 0;
    for (auto &[a, b] : R) {
        if (a < 10) {
            if (a == 9 && upnum >= 1) {
                ret.push_back({0, b});
                upnum = 1;
            } else if (upnum) {
                ret.push_back({a+1, 1ll});
                if (b > 1) {
                    ret.push_back({a, b-1});
                }
                upnum = 0;
            } else {
                ret.push_back({a, b});
                upnum = 0;
            }
        } else {
            int c = a%10;
            if (upnum) {
                ret.push_back({c+1, b});
            } else {
                ret.push_back({c, 1ll});
                if (b > 1) {
                    ret.push_back({c+1, b-1});
                }
            }
            upnum = 1;
        }
    }

    if (upnum) {
        ret.push_back({1, 1ll});
    }

    int k = 0;
    while (k < ret.size()) {
        int a = ret[k].first;
        ll b = 0;
        while (k < ret.size() && ret[k].first == a) {
            b += ret[k].second;
            k++;
        }
        ret2.push_back({a, b});
    }

    reverse(ret2.begin(), ret2.end());
    
    return ret2;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int M1; cin >> M1;
    vector<pair<int, ll>> P1;
    for (int i=0; i<M1; i++) {
        int a; ll b;
        cin >> a >> b;
        P1.push_back({a, b});
    }

    int M2; cin >> M2;
    vector<pair<int, ll>> P2;
    for (int i=0; i<M2; i++) {
        int a; ll b; cin >> a >> b;
        P2.push_back({a, b});
    }

    vector<pair<int, ll>> ans = solve(M1, P1, M2, P2);
    cout << ans.size() << endl;
    for (auto &[a, b] : ans) {
        cout << a << " " << b << "\n";
    }
}