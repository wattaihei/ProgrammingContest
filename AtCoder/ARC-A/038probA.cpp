#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int N; cin >> N;
    vector<int> A(N);
    for (int i=0; i<N; i++){
        cin >> A[i];
        
    }
    sort(A.begin(), A.end(), greater<int>());
    int c = 0;
    int ans = 0;
    for (int a: A){
        if (c%2==0){
            ans += a;
        }
        c += 1;
    }
    cout << ans << endl;
}