#include <bits/stdc++.h>
using namespace std;

int main() {
    long long A, K; cin >> A >> K;
    long long L = 2E12;
    if (K==0){
        cout << L - A << endl;
    }
    else {
        long long C = A;
        int ans = 0;
        while (C<L){
            C = (K+1)*C + 1;
            ans += 1;
        }
        cout << ans << endl;
    }
}