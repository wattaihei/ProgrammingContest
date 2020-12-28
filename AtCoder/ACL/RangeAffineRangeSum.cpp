#include <bits/stdc++.h>
#include <atcoder/lazysegtree>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;
using namespace atcoder;

const int mod = 998244353;

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

struct S {
    mint a;
    int size;
};

S op(S a, S b) {
    return {a.a + b.a, a.size+b.size};
}

S e() {
    return {0, 0};
}

struct F {
    mint b, c;
};

S mapping(F f, S a) {
    return {f.b * a.a + (mint)a.size * f.c, a.size};
}

F composition(F f1, F f2) {
    return {f1.b*f2.b, f2.c*f1.b + f1.c};
}

F id() {
    return (F){1, 0};
}

void solve() {
    int N, Q; cin >> N >> Q;
    vector<S> A(N);
    mint a;
    for (int i=0; i<N; i++) {
        cin >> a;
        A[i] = {a, 1};
    }
    lazy_segtree<S, op, e, F, mapping, composition, id> lst(A);

    int l, r;
    mint b, c;
    vector<mint> ans;
    for (int i=0; i<Q; i++) {
        int q; cin >> q;
        if (q == 0) {
            cin >> l >> r >> b >> c;
            lst.apply(l, r, {b, c});
        } else {
            cin >> l >> r;
            ans.push_back(lst.prod(l, r).a);
        }
    }
    for (auto a : ans) {
        cout << a << endl;
    }

    
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}