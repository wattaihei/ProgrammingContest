#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

int main() {
    int N; cin >> N;
    ull A[N];
    for (int i=0; i<N; i++){
        cin >> A[i];
    }

    ull B[N+1];
    B[0] = 0;
    ull tmp = 0;
    for (int i=0; i<N; i++){
        tmp += A[i];
        B[i+1] = B[i] + tmp;
        tmp += 1;
    }
    ull C[N+1];
    C[N] = 0;
    tmp = 0;
    for (int i=N-1; i>=0; i--){
        tmp += A[i];
        C[i] = C[i+1] + tmp;
        tmp += 1;
    }

    ull ans = ULLONG_MAX;
    for (int i=0; i<N; i++){
        if (i % 2 != 0) continue;
        ans = min(ans, B[i]+C[i+1]);
    }
    cout << ans << endl;
}