#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int L, R; cin >> L >> R;
    int l, r;
    map<int, int> A, B;
    for (int i=0; i<L; i++){
        cin >> l;
        if (!A[l]){
            A[l] = 1;
        }
        else{
            A[l] += 1;
        }
    }
    for (int i=0; i<R; i++){
        cin >> r;
        if (!B[r]){
            B[r] = 1;
        }
        else{
            B[r] += 1;
        }
    }
    int ans = 0;
    for (int i=0; i<41; i++){
        if (!A[i] || !B[i]){
            continue;
        }
        else{
            ans += min(A[i], B[i]);
        }
    }
    cout << ans << endl;

}