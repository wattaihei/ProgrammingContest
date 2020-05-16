#include <bits/stdc++.h>

using namespace std;

int main(){
    int N; cin >> N;
    double a, b, c, d, e;
    vector<double> V(N);
    for (int i=0; i<N; i++){
        cin >> a >> b >> c >> d >> e;
        V[i] = a+b+c+d+e*11/90;
    }
    cout << fixed << setprecision(10);
    cout << *max_element(V.begin(), V.end()) << endl;
}