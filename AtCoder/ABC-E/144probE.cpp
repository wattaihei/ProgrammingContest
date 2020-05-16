#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

const ll zero = 0;

int main() {
    ll N, K; cin >> N >> K;
    ll A[N];
    ll F[N];
    REP(i, N) cin >> A[i];
    REP(i, N) cin >> F[i];
    sort(A, A+N);
    ll l=-1, r=0, m;
    REP(i, N){
        if (A[i]*F[i] > r){
            r = A[i]*F[i];
        }
    }
    r += 1;
    priority_queue<ll> q;
    ll cost;
    while (r-l>1){
        m = (l+r)/2;
        REP(i, N){
            q.push(-(m/F[i]));
        }
        cost = 0;
        REP(i, N){
            if (A[i] > -q.top()){
                cost += A[i] + q.top();
            }
            q.pop();
        }
        if (cost <= K){
            r = m;
        }
        else{
            l = m;
        }
    }

    cout << r << endl;

}