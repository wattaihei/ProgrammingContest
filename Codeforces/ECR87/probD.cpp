#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

int N, Q;
int A[1010101];
int Query[1010101];

bool check(int x){
    int small = 0, large = 0; // xより小さいもの、x以上のもの
    for (int i=0; i<N; i++){
        if (A[i] < x) {
            small++;
        } else {
            large++;
        }
    }
    for (int i=0; i<Q; i++){
        int k = Query[i];
        if (k > 0) {
            if (k < x) {
                small++;
            } else {
                large++;
            }
        } else {
            k = -k;
            if (k > small) {
                large--;
            } else {
                small--;
            }
        }
    }
    return small > 0;
}

int main() {
    cin >> N >> Q;
    for (int i=0; i<N; i++){
        scanf("%d", &A[i]);
        //cin >> A[i];
    }
    for (int i=0; i<Q; i++){
        scanf("%d", &Query[i]);
        //cin >> Query[i];
    }

    int l = 0;
    int r = N+2;
    int m;
    while (r-l > 1){
        m = (r+l)/2;
        if (check(m)) {
            r = m;
        } else {
            l = m;
        }
    }
    if (l == N+1){
        cout << 0 << endl;
    } else {
        cout << l << endl;
    }
}