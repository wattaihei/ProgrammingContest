#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int N; cin >> N;
    string ans = "YES";
    for (int i=2; i<sqrt(N)+1; i++){
        if (N%i == 0){
            ans = "NO";
        }
    }
    cout << ans << endl;
}