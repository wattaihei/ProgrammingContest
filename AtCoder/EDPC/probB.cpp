#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
int INF = 1E9;

int main() {
    int N, K; cin >> N >> K;
    int H[N];
    for (int i=0; i<N; i++){
        cin >> H[i];
    }
    int dp[N];
    for (int i=0; i<N; i++){
        dp[i] = INF;
    }
    dp[0] = 0;
    for (int i=0; i<N; i++){
        for (int k=1; k<K+1; k++){
            if (i+k > N-1){
                dp[N-1] = min(dp[N-1], dp[i] + abs(H[N-1]-H[i]));
            }
            else{
                dp[i+k] = min(dp[i+k], dp[i] + abs(H[i+k]-H[i]));
            }
        }
    }
    cout << dp[N-1] << endl;
}