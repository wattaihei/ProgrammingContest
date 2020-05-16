#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int N; cin >> N;
    int a, b;
    int ans = 0;
    for (int i=0; i<N; i++){
        cin >> a >> b;
        ans += a*b;
    }
    cout << (int)(ans*1.05) << endl;
}