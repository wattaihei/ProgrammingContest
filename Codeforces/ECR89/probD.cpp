#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

int A[1000007];

int main() {
    int m = 10000007;
    vector<int> Mo(m+1, -1);
    for (int i=2; i<=m; i++){
        if (Mo[i] == -1){
            Mo[i] = 1;
            int l = 2;
            while (i*l <= m){
                Mo[i*l] = i;
                l += 1;
            }
        }  
    }

    int N, a; cin >> N;
    int ans1[N];
    int ans2[N];
    pair<int, int> ret;
    for (int i=0; i<N; i++){
        cin >> A[i];
    }
    for (int i=0; i<N; i++){
        a = A[i];
        if (Mo[a] == 1){
            ans1[i] = -1;
            ans2[i] = -1;
        } else {
            int p = Mo[a];
            int a2 = 1;
            while (a % p == 0){
                a2 *= p;
                a /= p;
            }
            if (a != 1) {
                ans1[i] = a;
                ans2[i] = a2;
            } else {
                ans1[i] = -1;
                ans2[i] = -1;
            }  
 
        }
    }
    for (int i=0; i<N; i++){
        cout << ans1[i] << " ";
    }
    cout << endl;
    for (int i=0; i<N; i++){
        cout << ans2[i] << " ";
    }
    cout << endl;
}