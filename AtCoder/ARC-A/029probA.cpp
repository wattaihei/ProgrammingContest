#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int N;
int T[10];
int sum = 0;
int ans = 1E9;

int dfs(int a, int S) {
    //cout << ans << endl;
    if (a == N){
        S = max(S, sum-S);
        return min(ans, S);
    }
    ans = dfs(a+1, S+T[a]);
    ans = dfs(a+1, S);
    return ans;
}

int main() {
    cin >> N;
    for (int i=0; i<N; i++){
        cin >> T[i];
        sum += T[i];
    }
    //cout << ans << endl;
    int& rans = ans;
    rans = sum;
    //cout << ans << endl;
    ans = dfs(0, 0);
    cout << ans << endl;
}