#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

int M, initbit = 0;
ll p, q;

ll Count(vector<int> SeqToBit, unordered_map<int, int> bitToSeq, int sbit, ll s) {
    if (bitToSeq[sbit]*M >= s) {
        
    }
    int cycle = SeqToBit.size() + 1 - bitToSeq[sbit];
    int oddcnt = 0;
    for (int i=0; i<bitToSeq[sbit]; i++) {
        int c = __builtin_popcount(SeqToBit[i]);
        oddcnt += c;
    }
} 

int solve() {
    unordered_map<int, int> bitToSeq;
    vector<int> SeqToBit = {initbit};
    bitToSeq[initbit] = 0;
    int bit = initbit;
    while (true) {
        int nbit = 0;
        int p = (bit>>(M-1))&1;
        for (int i=0; i<M; i++) {
            p ^= ((bit>>i)&1);
            nbit |= (p<<i);
        }
        if (bitToSeq.count(nbit)) break;
        bitToSeq[nbit] = SeqToBit.size();
        SeqToBit.push_back(nbit);
        bit = nbit;
    }

    
    
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
}