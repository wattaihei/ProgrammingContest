#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int N, K; cin >> N >> K;
    int T[N];
    for (int i=0; i<N; i++){
        cin >> T[i];
    }
    int ans = -1;
    for (int i=2; i<N; i++){
        if (T[i]+T[i-1]+T[i-2] < K){
            ans = i+1;
            break;
        }
    }
    cout << ans << endl;
}