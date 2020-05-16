#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

int main() {
    int N, K; cin >> N >> K;
    vector< vector<int> > Query = {};
    vector<int> T;
    string S; cin >> S;
    int NUM = 0;
    //cout << (S[0]=='L') << endl;
    while (true){
        T = {};
        for (int i=0; i<N-1; i++){
            if (S[i]=='R' && S[i+1]=='L'){
                T.push_back(i+1);
            }
        }
        if (T.size() == 0){
            break;
        }
        for (int t : T){
            //cout << t << endl;
            S[t-1] = 'L';
            S[t] = 'R';
            NUM++;
        }
        Query.push_back(T);
    }

    if (Query.size() <= K && K <= NUM){
        int delta = K - Query.size();
        vector<int> ans[K];
        int ind = 0;
        for (auto T : Query){
            if (T.size()-1 <= delta){
                for (int t : T){
                    ans[ind] = {t};
                    ind++;
                }
                delta -= T.size()-1;
            } else if (delta > 0){
                vector<int> C={};
                for (int t : T){
                    if (delta>0){
                        ans[ind] = {t};
                        ind++;
                        delta--;
                    } else {
                        C.push_back(t);
                    }
                }
                ans[ind] = C;
                ind++;
            } else {
                ans[ind] = T;
                ind++;
            }
        }
        for (int i=0; i<K; i++){
            T = ans[i];
            cout << T.size() << " ";
            for (int t : T){
                cout << t << " ";
            }
            cout << "\n";
        }
    } else {
        cout << -1 << endl;
    }
}