#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

int T;
int m = 20;

int solve(int N, string A, string B) {
    vector<vector<int>> exists(m, vector<int>(m, 0));
    for (int i=0; i<N; i++) {
        if (A[i] > B[i]) return -1;
        if (A[i] == B[i]) continue;
        exists[A[i]-'a'][B[i]-'a'] = 1;
    }
}

int main() {
    cin >> T;
    int N;
    string A, B;
    for (int t=0; t<T; t++) {
        cin >> N;
        cin >> A >> B;
        cout << solve(N, A, B) << "\n";
    }
}