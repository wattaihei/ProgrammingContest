#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

struct s1 {int l; char s;};
struct s2 {int l; int r;};

int main() {
    string S; cin >> S;
    int Q; cin >> Q;
    int check[Q];
    s1 S1[Q];
    s2 S2[Q];
    REP(i, Q){
        cin >> check[i];
        if (check[i] == 1){
            cin >> S1[i].l >> S1[i].s;
        }
        else{
            cin >> S2[i].l >> S2[i].r;
        }
    }

    map<char, set<int>> dic;
    REP(i, S.length()){
        bool update = false; 
        for (auto a=dic.begin(); a!=dic.end(); a++){
            if ((a->first) == S[i]){
                dic[a->first].insert(i);
                update = true;
            }
        }
        if (!update){
            set<int> Tmp;
            Tmp.insert(i);
            dic[S[i]] = Tmp;
        }
    }

    int l,r;
    char s;
    REP(i, Q){
        if (check[i] == 1){
            l = S1[i].l-1, s = S1[i].s;
            for (auto a=dic.begin(); a!=dic.end(); a++){
                if ((a->second).find(l) != (a->second).end()){
                    dic[a->first].erase(l);
                }
            }
            bool update = false;
            for (auto a=dic.begin(); a!=dic.end(); a++){
                if ((a->first) == s){
                    dic[s].insert(l);
                    update = true;
                }
            }
            if (!update){
                set<int> Tmp;
                Tmp.insert(l);
                dic[s] = Tmp;
            }
        }
        else{
            l = S2[i].l-1, r = S2[i].r-1;
            int count = 0;
            for (auto a=dic.begin(); a!=dic.end(); a++){
                set<int> root = (a->second);
                if (root.find(l) != root.end() || root.find(r) != root.end()){
                    count += 1;
                }
                else if (lower_bound(root.begin(), root.end(), l) != lower_bound(root.begin(), root.end(), l)){
                    count += 1;
                }
            }
            cout << count << endl;
        }
    }

}