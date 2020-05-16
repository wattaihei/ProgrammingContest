#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int A[4][4];
    for (int i=0; i<4; i++){
        for (int j=0; j<4; j++){
            cin >> A[i][j];
        }
    }
    string ans = "GAMEOVER";
    for (int i=0; i<4; i++){
        for (int j=0; j<3; j++){
            if (A[i][j] == A[i][j+1] || A[j][i] == A[j+1][i]){
                ans = "CONTINUE";
            }

        }
    }
    cout << ans << endl;
}