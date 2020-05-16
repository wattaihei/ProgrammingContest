#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int X, Y, K; cin >> X >> Y >> K;
    if (K >= Y){
        cout << Y + X - (K-Y) << endl;
    }
    else{
        cout << X + K << endl;
    }
}