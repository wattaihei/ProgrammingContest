#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;
const ll mod = 998244353;

const int MAX = 10000;
long long fac[MAX], finv[MAX], inv[MAX];

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

// テーブルを作る前処理
void COMinit() {
    fac[0] = fac[1] = 1;
    finv[0] = finv[1] = 1;
    inv[1] = 1;
    for (int i = 2; i < MAX; i++){
        fac[i] = fac[i - 1] * i % mod;
        inv[i] = mod - inv[mod%i] * (mod / i) % mod;
        finv[i] = finv[i - 1] * inv[i] % mod;
    }
}

// 二項係数計算
long long COM(int n, int k){
    if (n < k) return 0;
    if (n < 0 || k < 0) return 0;
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    COMinit();

    int N, K; cin >> N >> K;
    mint A[N], B[N];
    for (int i=0; i<N; i++) {
        cin >> A[i];
        B[i] = 1;
    }
    mint C[2*K+1];
    for (int k=0; k<=2*K; k++) {
        mint c = 0;
        for (int i=0; i<N; i++) {
            c += B[i];
            B[i] *= A[i];
        }
        C[k] = c;
    }
    
    vector<mint> ans(K+1, 0);
    for (int l=0; l<=K; l++) {
        for (int r=0; r<=K; r++) {
            int x = l+r;
            if (x <= K) {
                ans[x] += (mint)COM(x, l) * ((C[l] * C[r]) - C[l+r]);
            }
        }
    }
    for (int i=1; i<K+1; i++) {
        cout << (ans[i]/2) << endl;
    }
}