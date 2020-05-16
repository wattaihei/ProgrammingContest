#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

int main() {
    int N; cin >> N;
    string S; cin>>S;
    vector<int> L, R;
    REP(i, N){
        if (S[i] == '('){
            L.push_back(i);
        }
        else{
            R.push_back(i);
        }
    }
    if (L.size() !=R.size()){
        cout << 0 << endl;
        cout << 1 << " " << 1 << endl;
    }
    else{
        R.push_back(L[0]);
        int ans = -1;
        int al, ar;
        for (int i=0; i<L.size(); i++) for (int j=0;j<R.size();j++){
            int l = L[i], r = R[j];
            string P = S;
            P[l] = S[r];
            P[r] = S[l];
            int a = 0;
            vector<int> A;
            REP(k, N){
                if (P[k] == '('){
                    a += 1;
                }
                else{
                    a -= 1;
                }
                A.push_back(a);
            }
            int b = *min_element(A.begin(), A.end());
            int s = 0;
            for (int p=0; p<A.size(); p++){
                if (b-A[p] >= 0){
                    s += 1;
                }
            }
            if (ans < s){
                ans = s;
                al = l+1;
                ar = r+1;
            }
        }
        cout << ans <<endl;
        cout << al << " " << ar << endl;
    }

}