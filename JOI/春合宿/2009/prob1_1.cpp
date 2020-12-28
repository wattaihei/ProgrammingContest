#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

int M, initbit = 0;
ll p, q, t = 0ll;

ll Count(vector<int> SeqToBit, ll s) {
    if (s < 0) return 0ll;
    int cycle = SeqToBit.size();
    if (cycle*M <= s) {
        ll p = cycle*M;
        return t*(s/p) + Count(SeqToBit, s%p);
    }

    ll oddcnt = 0ll;
    for (int i=0; i<s/M; i++) {
        oddcnt += __builtin_popcount(SeqToBit[i]);
    }
    for (int i=0; i<s%M; i++) {
        oddcnt += (SeqToBit[s/M]>>i)&1;
    }
    return oddcnt;
} 

void solve() {
    // unordered_map<int, int> bitToSeq;
    vector<int> SeqToBit = {initbit};
    // bitToSeq[initbit] = 0;
    int bit = initbit;
    t = __builtin_popcount(bit);
    while (true) {
        int nbit = 0;
        int p = (bit>>(M-1))&1;
        for (int i=0; i<M; i++) {
            p ^= ((bit>>i)&1);
            nbit |= (p<<i);
        }
        if (nbit == initbit) break;
        t += __builtin_popcount(nbit);
        // bitToSeq[nbit] = SeqToBit.size();
        SeqToBit.push_back(nbit);
        bit = nbit;
    }

    if (bit == 0) {
        cout << 0 << endl;
    } else {
        ll ans = Count(SeqToBit, q) - Count(SeqToBit, p-1);
        cout << ans << endl;
    }
    
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> M;
    cin >> p;
    cin >> q;
    for (int i=0; i<M; i++) {
        int a; cin >> a;
        initbit |= ((a&1)<<i);
    }
    solve();
    return 0;
}