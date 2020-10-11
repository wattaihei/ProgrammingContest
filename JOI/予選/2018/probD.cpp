#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

int N;
int A[50];

// int makeDelta(int l, int r, int minimum, int limit) {
//     int ok, ng, m;
//     ng = 0;
//     ok = limit;
//     while (ok - ng > 1) {
//         m = (ok + ng) / 2;
//         int s = 0;
//         bool canMake = true;
//         for (int i=0; i<l; i++) {
//             if (s < minimum || s + A[i] <= m + minimum) {
//                 s += A[i];
//             } else {
//                 if (A[i] > m + minimum) canMake = false;
//                 s = A[i];
//             }
//         }
//         if ((0 < s && s < minimum) || minimum + m < s) canMake = false;
//         s = 0;
//         for (int i=r; i<N; i++) {
//             if (s < minimum || s + A[i] <= m + minimum) {
//                 s += A[i];
//             } else {
//                 if (A[i] > m + minimum) canMake = false;
//                 s = A[i];
//             }
//         }
//         if ((0 < s && s < minimum) || minimum + m < s) canMake = false;

//         if (canMake) {
//             ok = m;
//         } else {
//             ng = m;
//         }
//     }
//     return ok;
// }

int solve() {
    int B[N+1];
    B[0] = 0;
    for (int i=0; i<N; i++) {
        B[i+1] = B[i] + A[i];
    }
    set<int> S;
    for (int l=0; l<N; l++) {
        for (int r=l+1; r<N+1; r++) {
            S.insert(B[r] - B[l]);
        }
    }
    unordered_map<int, int> co_to_ind;
    vector<int> ind_to_co;
    int k = 0;
    for (int s : S) {
        co_to_ind[s] = k++;
        ind_to_co.push_back(s);
    }

    int K = ind_to_co.size();
    vector<vector<int>> dp(N+1, vector<int>(K, K));

    for (int i=0; i<N; i++) {
        dp[i+1][co_to_ind[B[i+1]]] = co_to_ind[B[i+1]];
        for (int l=0; l<i; l++) {
            int k0 = co_to_ind[B[i+1]-B[l+1]];
            for (int k=0; k<K; k++) {
                dp[i+1][min(k,k0)] = min(dp[i+1][min(k,k0)], max(dp[l+1][k], k0));
            }
        }
    }

    // for (int i=0; i<N+1; i++) {
    //     for (int k=0; k<K; k++) {
    //         cout << dp[i][k] << " ";
    //     }
    //     cout << endl;
    // }
    
    int ans = B[N];
    for (int k=0; k<K-1; k++) {
        if (dp[N][k] == K) continue;
        ans = min(ans, ind_to_co[dp[N][k]] - ind_to_co[k]);
    }

    return ans;
}

int main() {
    cin >> N;
    for (int i=0; i<N; i++) cin >> A[i];
    cout << solve() << endl;
}