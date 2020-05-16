#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int N, M; cin >> N >> M;
    int a[M];
    for (int i=0; i<M; i++){
        cin >> a[i];
    }
    bool checked[N+1];
    for (int i=0; i<N+1; i++){
        checked[i] = false;
    }
    vector<int> ans;
    for (int i=M-1; i>=0; i--){
        //cout << a[i] << checked[a[i]] << endl;
        if (!checked[a[i]]){
            ans.push_back(a[i]);
            checked[a[i]] = true;
        }
    }
    for (int i=1; i<=N; i++){
        if (!checked[i]){
            ans.push_back(i);
        }
    }
    for (int a : ans){
        cout << a << endl;
    }
}