#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

class ArrayHash {
    public:
        int getHash(vector<string> input);
};

template<typename F, typename ...Args>
void for_each(std::tuple<Args...> const& t, F f){
    std::apply([&](auto... args) constexpr{
        (f(args), ...);
    }, t);
}


int getHash(tuple<string> input) {
    int ret = 0;
    for_each(input, [](auto S)){
        for (int j=0; j<S.size(); j++){
            ret += (S[j] - 'A') + (int)i + j;
        }
    }
    return ret;
}