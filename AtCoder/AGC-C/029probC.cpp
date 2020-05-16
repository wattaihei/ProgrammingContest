#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

int main() {
    int N; cin >> N;
    int A[N];
    REP(i, N) cin >> A[i];
    int l = 0;
    int r = N;
    int m;
    while (r-l>1){
        m = (r+l)/2;
        bool ok = true;
        unordered_map<int, int> dp;
        int needreset = 1000000007, pre = -1;
        unordered_map<int, int> exception;
        REP(i, N){
            int ind = A[i];
            REP(j, 100){
                if (needreset >= ind || exception[ind]){
                    dp[ind] = ((pre < A[i]) ? 0 : 1);
                }
                else {
                    dp[ind] = ((pre < A[i]) ? 0 : 1);
                    exception[ind] = 1;
                }
                if (dp[ind] < m){
                    dp[ind] += 1;
                    break;
                }
                else if (ind == 1){
                    ok = false;
                    break;
                }
                else{
                    dp[ind] = 1;
                    ind -= 1;
                }
            }
            if (!ok) break;
            if (pre > A[i]){
                needreset = A[i];
                exception.clear();
            }      
            pre = A[i];
        }
        if (ok){
            r = m;
        } else {
            l = m;
        }
    }
    cout << r << endl;
}