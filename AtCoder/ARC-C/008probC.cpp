#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;


const double INF = 1e18;

int main() {
    int N; cin >> N;
    double X[N],Y[N], T[N], R[N];
    for (int i=0; i<N; i++){
        cin >> X[i];
        cin >> Y[i];
        cin >> T[i];
        cin >> R[i];  
    }
    vector< pair<double, int> > graph[N];
    double x1, y1, t1, r1, x2, y2, t2, r2, d;
    for (int i=0; i<N; i++){
        x1 = X[i]; y1 = Y[i]; t1 = T[i]; r1 = R[i];
        for (int j=i+1; j<N; j++){
            x2 = X[j]; y2 = Y[j]; t2 = T[j]; r2 = R[j];
            d = sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
            graph[i].push_back({d/min(t1, r2), j});
            graph[j].push_back({d/min(t2, r1), i});
        }
    }

    priority_queue< pair<double, int>, vector<pair<double, int> >, greater<pair<double, int> > > que;
    vector<double> D(N, INF);
    que.push({0, 0});
    D[0] = 0;
    pair<double, int> now, next;
    while (!que.empty()) {
        now = que.top();
        que.pop();
        if (D[now.second] < now.first) continue;
        for (pair<double, int> next : graph[now.second]){
            if (D[now.second] + next.first < D[next.second]) {
                D[next.second] = D[now.second] + next.first;
                que.push(next);
            }
        }
    }
    sort(D.begin(), D.end(), greater<double>());
    double ans = 0;
    for (int i=0; i<N-1; i++){
        //cout << D[i] << endl;
        ans = max(ans, D[i]+(double)i);
    }
    cout << fixed << setprecision(10);
    cout << ans << endl;
}