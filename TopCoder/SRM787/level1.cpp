#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

class AqaAsadiNames {
    public:
        string getName(string Dad, string Mom, string FirstChild, string Gender);
};


pair<string, string> split(string S){
    pair<string, string> ret;
    string tmp = "";
    for (int i=0; i<S.size(); i++){
        if (S[i] == ' '){
            ret.first = tmp;
            tmp = "";
        } else {
            tmp.push_back(S[i]);
        }
    }
    ret.second = tmp;
    return ret;
}

string AqaAsadiNames::getName(string Dad, string Mom, string FirstChild, string Gender){
    pair<string, string> Dp, Mp, Fp;
    Dp = split(Dad); Mp = split(Mom); Fp = split(FirstChild);
    string female = "AEIOUY";
    string firstboy = "Boy";
    for (auto s: female){
        if (s == Fp.first[0]){
            firstboy = "Girl";
        }
    }
    string ret = "";
    if (firstboy != Gender){
        if (Gender == "Boy"){
            ret = Dp.second + " " + Dp.first;
        } else {
            ret = Mp.second + " " + Mp.first;
        }
    } else {
        if (Gender == "Boy"){
            ret = Dp.first + " " + Fp.second;
        } else {
            ret = Mp.first + " " + Fp.second;
        }
    }
    return ret;
}