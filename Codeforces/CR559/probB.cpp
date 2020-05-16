#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

bool compare_by_b(pair<int, int> a, pair<int, int> b) {
    if(a.second != b.second){
        return a.second < b.second;
    }else{
        return a.first < b.first;
    }
}



int main() {
    int N; cin >> N;
    vector<pair<int, int>> pairs(N);
    int a;
    REP(i, N){
        cin >> a;
        pairs[i] = make_pair(i+1, a);
    }
    sort(pairs.begin(), pairs.end(), compare_by_b);

    set<int> unchecked;
    REP(i, N){
        unchecked.insert(i+1);
    }
    int K = -1;
    int min_i, max_i, f;
    REP(ind, N){
        int i = pairs[ind].first;
        int b = pairs[ind].second;
        min_i = *unchecked.upper_bound(0);
        max_i = *unchecked.lower_bound(N+1);
        unchecked.erase(i);
        f = max(abs(unchecked[min_i]-i), abs(unchecked[max_i]-i));
        if (f == 0) continue;
        if (K==-1) K = b/f;
        K = min(K, b/f);
    }
    cout << K << endl;
}