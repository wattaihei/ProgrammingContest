#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int N; cin >> N;
    cout << (N/10)*100 + min((N%10)*15, 100) << endl;
}