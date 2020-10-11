#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;


const int MAXN = 4e5;
int T, N, K, L;
ll D[MAXN];



bool solve() {
    cin >> N >> K >> L;
    for (int i=0; i<N; i++) {
        cin >> D[i];
    }
    ll l = K - D[0];
    bool up = false;
    for (int i=0; i<N; i++) {
        if (D[i] > L) return false;
        if (!up) {
            if (l + D[i] > L) {
                return false;
            }
        } else {
            if (l + D[i] > L) {
                return false;
            } else {
                if (K + D[i] <= L) {
                    l = L - D[i];
                    up = false;
                }
            }
        }
        if (l == K) up = false;
        if (l == 0) up = true;
        if (up) l++; else l--;
        if (l == K) up = false;
        if (l == 0) up = true;
    }
    return true;
}

int main() {
    cin >> T;
    for (int t=0; t<T; t++) {
        cout << (solve() ? "Yes" : "No") << "\n";
    }
}