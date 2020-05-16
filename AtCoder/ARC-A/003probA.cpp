#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int N; cin >> N;
    string S; cin >> S;
    double ans = 0;
    for (int i=0; i<N; i++){
        if (S[i] == 'A'){
            ans += 4;
        }
        else if (S[i] == 'B'){
            ans += 3;
        }
        else if (S[i] == 'C'){
            ans += 2;
        }
        else if (S[i] == 'D'){
            ans += 1;
        }
    }
    cout << fixed << setprecision(10);
    cout << ans/N << endl;
}