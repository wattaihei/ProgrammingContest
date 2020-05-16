#include <bits/stdc++.h>
using namespace std;

int main() {
    double L, X, Y, S, D; cin >> L >> X >> Y >> S >> D;
    double left, right;
    if (S <= D){
        right = (D-S)/(X+Y);
        if (Y > X){
            left = (S+L-D)/(Y-X);
        }
        else{
            left = right;
        }
    }
    else {
        right = (D+L-S)/(Y+X);
        if (Y > X){
            left = (S-D)/(Y-X);
        }
        else{
            left = right;
        }
    }
    cout << fixed << setprecision(10);
    cout << min(left, right) << endl;
}