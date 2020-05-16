#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

struct point{
    ll x;
    ll y;
};

ll A[1010101];


vector<point> ConvexHull(vector<point> Points){
    vector<point> Qs;
    for (int i=0; i<Points.size(); i++){
        point p = Points[i];
        while (Qs.size() > 1){
            int s = Qs.size();
            point p1 = Qs[s-1];
            point p2 = Qs[s-2];
            if ((p1.y-p.y)*(p.x-p2.x) > (p.y-p2.y)*(p1.x-p.x)){
                Qs.pop_back();
            } else {
                break;
            }
        }
        Qs.push_back(p);
    }
    return Qs;
}



int main() {
    ll N; cin >> N;
    for (ll i=0; i<N; i++){
        cin >> A[i];
    }
    vector<point> Points;
    point p = {0LL, 0LL};
    Points.push_back(p);
    ll tmp = 0LL;
    for (ll i=0LL; i<N; i++){
        tmp += A[i];
        p = {i+1, tmp};
        Points.push_back(p);
    }
    vector<point> C = ConvexHull(Points);
    vector<double> ans;
    for (int i=0; i<C.size()-1; i++){
        ll count = C[i+1].x - C[i].x;
        ll value = C[i+1].y - C[i].y;
        for (ll j=0; j<count; j++){
            ans.push_back((double)value/(double)count);
        }
    }

    cout << fixed << setprecision(10);
    for (int i=0; i<ans.size(); i++){
        cout << ans[i] << " ";
    }
    cout << "\n";

}