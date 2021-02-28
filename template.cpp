#include <bits/stdc++.h>
using namespace std;

// 比較関数
class comp {
    public:
    bool operator()(edge a, edge b) {
        return a.t > b.t;
    }
};

vector<ll> pickup_prime(ll M) {
    vector<int> is_prime(M+1, -1);
    for (ll m=2; m<M+1; m++) {
        if (is_prime[m] == -1) {
            is_prime[m] = 1;
            ll l = 2;
            while (m*l <= M) {
                is_prime[m*l] = 0;
                l++;
            }
        }
    }
    vector<ll> primes;
    for (int m=2; m<M+1; m++) {
        if (is_prime[m] == 1) {
            primes.push_back(m);
        }
    }
    return primes;
}

set<ll> prime(ll n) {
    n = max(n, -n);
    set<ll> ret;
    for (ll num=2; num*num<=n; num++) {
        while (n%num == 0) {
            n /= num;
            ret.insert(num);
        }
        if (num > n) break;
    }
    if (n != 1) ret.insert(n);
    return ret;
}

ll gcd(ll a, ll b) {
    if (b > a) swap(a, b);
    if (b == 0) return a;
    return gcd(b, a%b);
}

int main() {
    // 固有小数点に合わせる
    cout << fixed << setprecision(10);

    //大文字小文字変換
    S = toupper(s)
    s = tolower(S)

    //char to int
    num = (int)(str-'0')
    //string to int
    num = stoi(str)
    //int to string
    str = to_string(num)

    //vector
    vector<ll> vec;
    ll S_max = *max_element(vec.begin(), vec.end());
    ll S_min = *min_element(vec.begin(), vec.end());
    ll S_sum = accumulate(vec.begin(), vec.end(), 0);
    int length = vec.size();
    sort(vec.begin(), vec.end());
    //初期値に注意！
    for (int a : vec){
        cout << a << endl;
    }
    for (int i=0; i<vec.size(); i++){
        cout<< vec[i] << endl;
    }


    //グローバル変数の書き換え(参照)
    int& rx = x;
    rx = 6;
}

