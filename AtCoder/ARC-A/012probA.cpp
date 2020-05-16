#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    string S; cin >> S;
    string A[7] = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
    if (S == A[5] || S == A[6]){
        cout << 0 << endl;
    }
    for (int i=0; i<5; i++){
        if (S == A[i]){
            cout << 5 - i << endl;
        }
    }
}