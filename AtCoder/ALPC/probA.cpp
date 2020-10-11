#include <bits/stdc++.h>
#include <atcoder/dsu>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;
using namespace atcoder;

int main() {
    int N, Q; cin >> N >> Q;
    dsu uni(N);
    int t,a,b;
    for (int i=0; i<Q; i++) {
        cin >> t >> a >> b;
        if (t == 0) {
            uni.merge(a, b);
        } else {
            cout << (uni.same(a, b) ? 1 : 0) << endl;
        }
    }    
}