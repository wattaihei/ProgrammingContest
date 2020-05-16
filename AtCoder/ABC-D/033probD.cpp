#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

int main() {
    int N; cin >> N;
    int XY[N][2];
    REP(i, N){
        cin >> XY[i][0] >> XY[i][1];
    }
    int d1, d2, d3;
    int a1=0, a2=0, a3=0;
    REP(i, N-2) FOR(j, i+1, N-1) FOR(k, j+1, N){
        d1 = pow(XY[i][0]-XY[j][0], 2) + pow(XY[i][1]-XY[j][1], 2);
        d2 = pow(XY[j][0]-XY[k][0], 2) + pow(XY[j][1]-XY[k][1], 2);
        d3 = pow(XY[k][0]-XY[i][0], 2) + pow(XY[k][1]-XY[i][1], 2);
        if (d1+d2<d3 || d2+d3<d1 || d3+d1<d2){
            a3 += 1;
        }
        else if (d1+d2==d3 || d2+d3==d1 || d3+d1==d2){
            a2 += 1;
        }
        else{
            a1 += 1;
        }
    }
    cout << a1 << ' '<< a2 << ' ' << a3 << endl;

}