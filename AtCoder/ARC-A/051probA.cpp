#include <bits/stdc++.h>
using namespace std;

int main() {
    int x1, y1, r; cin >> x1 >> y1 >> r;
    int x2, y2, x3, y3; cin >> x2 >> y2 >> x3 >> y3;
    bool red = false, blue = false;
    for (int x=-100; x<=100; x++){
        for (int y=-100; y<=100; y++){
            bool nr = false, nb = false;
            if (pow(x-x1, 2)+pow(y-y1, 2) <= pow(r, 2)){
                nr = true;
            }
            if (x2 <= x && x <= x3 && y2 <= y && y <= y3){
                nb = true;
            }
            if (nr && nb){
                continue;
            }
            else {
                if (nr){
                    red = true;
                }
                if (nb){
                    blue = true;
                }
            } 
        }
    }
    if (red){
        cout << "YES" << endl;
    }
    else{
        cout << "NO" << endl;
    }
    if (blue){
        cout << "YES" << endl;
    }
    else{
        cout << "NO" << endl;
    }
}