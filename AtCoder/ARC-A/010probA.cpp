#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int N, M, A, B; cin >> N >> M >> A >> B;
    int a = N;
    int ans = -1;
    for (int i=0; i<M; i++){
        int c; cin >> c;
        if (a <= A){
            a += B;
        }
        a -= c;
        if (a < 0){
            ans = i+1;
            break;
        }
    }
    if (ans == -1){
        cout << "complete" << endl;
    }
    else{
        cout << ans << endl;
    }
}