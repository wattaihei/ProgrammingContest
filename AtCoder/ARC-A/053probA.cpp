#include <bits/stdc++.h>
using namespace std;

int main() {
    int H, W; cin >> H >> W;
    if (H == 1){
        cout << W-1 << endl;
    }
    else if (W == 1){
        cout << H-1 << endl;
    }
    else{
        cout << (H-1)*W + H*(W-1) << endl;
    }
}