#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int N; cin >> N;
    string S; cin >> S;
    vector<int> a(4);
    for (int i=0; i<4; i++){
        a[i] = 0;
    }
    for (int i=0; i<N; i++){
        a[(int)(S[i]-'0')-1] += 1;
    }
    cout << *max_element(a.begin(), a.end()) << ' ' << *min_element(a.begin(), a.end()) << endl;
}