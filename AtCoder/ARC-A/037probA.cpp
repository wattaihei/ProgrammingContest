#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int N; cin >> N;
    int ans = 0;
    for (int i=0; i<N; i++){
        int a; cin >> a;
        if (a < 80){
            ans += (80 - a);
        }
    }
    cout << ans << endl;
}