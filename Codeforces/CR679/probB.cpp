#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    int N, M; cin >> N >> M;
    int A[N][M];
    int B[M][N];
    for (int n=0; n<N; n++) {
        for (int m=0; m<M; m++) {
            cin >> A[n][m];
        }
    }
    for (int m=0; m<M; m++) {
        for (int n=0; n<N; n++) {
            cin >> B[m][n];
        }
    }
    map<int, int> C;
    for (int n=0; n<N; n++){
        C[B[0][n]] = n;
    }

    int Seq[N];
    for (int n=0; n<N; n++) {
        for (int m=0; m<M; m++) {
            if (C.count(A[n][m])) {
                Seq[C[A[n][m]]] = n;
            }
        }
    }

    for (int n=0; n<N; n++) {
        for (int m=0; m<M; m++) {
            cout << A[Seq[n]][m];
            if (m < M-1) {
                cout << " ";
            }
        }
        cout << endl;
    }

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q; cin >> Q;
    for (int q=0; q<Q; q++) {
        solve();
    }
}