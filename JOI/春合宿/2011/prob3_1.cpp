#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int mod = 10000000;

template<ll mod> class modint{
public:
    ll val=0;
    //コンストラクタ
    modint(ll x=0){while(x<0)x+=mod;val=x%mod;}
    //コピーコンストラクタ
    modint(const modint &r){val=r.val;}
    //算術演算子
    modint operator -(){return modint(-val);} //単項
    modint operator +(const modint &r){return modint(*this)+=r;}
    modint operator -(const modint &r){return modint(*this)-=r;}
    modint operator *(const modint &r){return modint(*this)*=r;}
    modint operator /(const modint &r){return modint(*this)/=r;}
    //代入演算子
    modint &operator +=(const modint &r){
        val+=r.val;
        if(val>=mod)val-=mod;
        return *this;
    }
    modint &operator -=(const modint &r){
        if(val<r.val)val+=mod;
        val-=r.val;
        return *this;
    }
    modint &operator *=(const modint &r){
        val=val*r.val%mod;
        return *this;
    }
    modint &operator /=(const modint &r){
        ll a=r.val,b=mod,u=1,v=0;
        while(b){
            ll t=a/b;
            a-=t*b;swap(a,b);
            u-=t*v;swap(u,v);
        }
        val=val*u%mod;
        if(val<0)val+=mod;
        return *this;
    }
    //等価比較演算子
    bool operator ==(const modint& r){return this->val==r.val;}
    bool operator <(const modint& r){return this->val<r.val;}
    bool operator !=(const modint& r){return this->val!=r.val;}
};

using mint = modint<mod>;

//入出力ストリーム
istream &operator >>(istream &is,mint& x){//xにconst付けない
    ll t;is >> t;
    x=t;
    return (is);
}
ostream &operator <<(ostream &os,const mint& x){
    return os<<x.val;
}

//累乗
mint modpow(const mint &a,ll n){
    if(n==0)return 1;
    mint t=modpow(a,n/2);
    t=t*t;
    if(n&1)t=t*a;
    return t;
}

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    int L; cin >> L;
    string S; cin >> S;
    int N; cin >> N;
    vector<vector<int>> canmove(26, vector<int>(26, 1));
    for (int i=0; i<N; i++) {
        char s, t; cin >> s >> t;
        int p = s - 'A', q = t - 'A';
        canmove[p][q] = 0;
        // canmove[q][p] = 0;
    }
    vector<vector<int>> T(26);
    for (int i=0; i<L; i++) {
        int s = S[i] - 'A';
        T[s].push_back(i);
    }
    vector<int> Inds(26, 0);

    vector<mint> dp(L+1, 0);
    for (int s=0; s<26; s++) {
        if (!T[s].empty()) {
            dp[T[s][0]] = 1;
        }
    }

    mint ans = 0;
    for (int i=0; i<L; i++) {
        ans += dp[i];
        int p = S[i] - 'A';
        Inds[p]++;
        for (int s=0; s<26; s++) {
            if (canmove[p][s] && Inds[s] < T[s].size()) {
                dp[T[s][Inds[s]]] += dp[i];
            }
        }
    }
    cout << ans << endl;

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}