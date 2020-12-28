#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;
const ll mod = 1000000007;

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

const int AMAX = 10000;
long long fac[AMAX], finv[AMAX], inv[AMAX];

// テーブルを作る前処理
void COMinit() {
    fac[0] = fac[1] = 1;
    finv[0] = finv[1] = 1;
    inv[1] = 1;
    for (int i = 2; i < AMAX; i++){
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

void solve() {
    COMinit();
    int R, C, N; cin >> R >> C;
    cin >> N;
    int maxr = 0, minr = R, maxc = 0, minc = C;
    for (int i=0; i<N; i++) {
        int r, c; cin >> r >> c;
        maxr = max(maxr, r);
        minr = min(minr, r);
        maxc = max(maxc, c);
        minc = min(minc, c);
    } 
    int rsize = maxr - minr + 1;
    int csize = maxc - minc + 1;
    vector<vector<mint>> dp(R+1, vector<mint>(C+1, 0));
    dp[rsize][csize] = (mint)1;
    for (int i=1; i<=rsize*csize - N; i++) {
        dp[rsize][csize] *= i;
    }
    for (int r=rsize; r<=R; r++) {
        for (int c=csize; c<=C; c++) {
            if (r < R) {
                dp[r+1][c] += (dp[r][c] * fac[c]);
            }
            if (c < C) {
                dp[r][c+1] += (dp[r][c] * fac[r]);
            }
        }
    }

    cout << (dp[R][C] * COM(R-rsize, minr-1) * COM(C-csize, minc-1)) << endl;
    
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}