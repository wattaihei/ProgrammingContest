#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;
const ll mod = 998244353;


int main() {
    int l;
    vector<int> A;
    A.push_back(4);
    A.push_back(3);
    int B[3];
    map<int, int> M;
    M[2] = 9;
    vector<vector<int>> P(10, vector<int>(10, 0));
    for (int i=0; i<5; i++) {
        B[i] = 0;
    }
    P[3][3] = 4;
    cin >> l;
    A.push_back(l);
    cout << l*2 << endl;;
}
