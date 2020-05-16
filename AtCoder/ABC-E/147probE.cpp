#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

int L = 80*80*4;
int mid = L/2;
int l2, l3;

int main() {
    int H, W; cin >> H >> W;
    int A[H][W];
    int B[H][W];
    REP(h, H){
        REP(w, W){
            cin >> l2;
            A[h][w] = l2;
        }
    }
    REP(h, H) {
        REP(w, W){
            cin >> l3;
            B[h][w] = l3;
        }
    }
    bool dp1[H+1][W+1][L+1];
    REP(h, H+1){
        REP(w, W+1){
            REP(l, L+1) {
                dp1[h][w][l] = false;
            }
        }
    }
    REP(h, H+1){
        dp1[h][0][mid] = true;
    }
    REP(w, W+1){
        dp1[0][w][mid] = true;
    }

    REP(h, H){
        REP(w, W){
            int c1 = A[h][w]-B[h][w];
            REP(l, L+1){
                if (0 <= l-c1 <= L){
                    dp1[h+1][w+1][l] = dp1[h+1][w+1][l] || dp1[h][w+1][l-c1] || dp1[h+1][w][l-c1];
                }
                if (0 <= l+c1 <= L){
                    dp1[h+1][w+1][l] = dp1[h+1][w+1][l] || dp1[h][w+1][l+c1] || dp1[h+1][w][l+c1];
                }
            }
        }
    }

    int ans = 1000000000;
    REP(l1, L+1){
        if (dp1[H][W][l1]){
            //cout << l1-mid << endl;
            ans = min(abs(l1-mid), ans);
        }
    }
    cout << ans << endl;

}