#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int A, B; cin >> A >>B;
    cout << max({A%100+900-B, A-(B%100+100), A-B +90-(A%100)/10*10, A-(B-(B%100)/10*10), A-B-A%10+9, A-(B-B%10)}) << endl;

}