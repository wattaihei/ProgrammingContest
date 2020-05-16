#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

double dis(int x1, int x2, int y1, int y2){
    return pow(pow(x1-x2, 2) + pow(y1-y2, 2), 0.5);
}

int main() {
    int N; cin >> N;
    int X[N], Y[N];
    for (int i=0; i<N; i++){
        cin >> X[i] >> Y[i];
    }
    double ans = 0;
    for (int i=0; i<N-1; i++){
        for (int j=i+1; j<N; j++){
            ans = max(ans, dis(X[i], X[j], Y[i], Y[j]));
        }
    }
    cout << fixed << setprecision(8);
    cout << ans << endl;
}