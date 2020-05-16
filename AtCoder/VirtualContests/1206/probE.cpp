#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

string Alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
string s, s1, s2;



int main() {
    int N; cin >> N;
    vector<string> Ss;
    string S;
    REP(i, N){
        cin >> S;
        Ss.push_back(S);
    }
    unordered_map<string, int> dic;

    for (string S : Ss){
        if (S.length() >= 52){
            
        }
        else{
            unordered_map<string, int> dic1, dic2, dic3;
            REP(i, S.length()){
                s = {S[i]};
                REP(j, 52) REP(k, 52){
                    s2 = {Alp[j], Alp[k]};
                    if (dic2[s2] == 1 && dic3[s2+s] != 1){
                        dic3[s2+s] = 1;
                        dic[s2+s] += 1;
                    }
                }
                REP(j, 52){
                    s1 = {Alp[j]};
                    if (dic1[s1] == 1){
                        dic2[s1+s] = 1;
                    }
                }
                dic1[s] = 1;
            }
        }
    }
    string ans;
    int num = 0;
    REP(i, Alp.length()) REP(j, Alp.length()) REP(k, Alp.length()){
        s = {Alp[i], Alp[j], Alp[k]};
        if (dic[s] > num){
            ans = s;
            num = dic[s];
        }
    }
    cout << ans << "\n";

}