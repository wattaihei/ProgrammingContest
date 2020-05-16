#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int D[7], J[7];
    int ans = 0;
    for (int i=0; i<7; i++){
        cin >> D[i];
    }
    for (int i=0; i<7; i++){
        cin >> J[i];
    }
    for (int i=0; i<7; i++){
        ans += max(D[i], J[i]);
    }
    cout << ans << endl;
}