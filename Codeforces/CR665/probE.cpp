#include <bits/stdc++.h>
//#include <atcoder/fenwicktree>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

typedef pair<int, int> T;

const int INFINT = 2e9;
const ll INFLL = 2e18;

const int MAX = 1000000;

namespace atcoder {
namespace internal {

#ifndef _MSC_VER
template <class T>
using is_signed_int128 =
    typename std::conditional<std::is_same<T, __int128_t>::value ||
                                  std::is_same<T, __int128>::value,
                              std::true_type,
                              std::false_type>::type;

template <class T>
using is_unsigned_int128 =
    typename std::conditional<std::is_same<T, __uint128_t>::value ||
                                  std::is_same<T, unsigned __int128>::value,
                              std::true_type,
                              std::false_type>::type;

template <class T>
using make_unsigned_int128 =
    typename std::conditional<std::is_same<T, __int128_t>::value,
                              __uint128_t,
                              unsigned __int128>;

template <class T>
using is_integral = typename std::conditional<std::is_integral<T>::value ||
                                                  is_signed_int128<T>::value ||
                                                  is_unsigned_int128<T>::value,
                                              std::true_type,
                                              std::false_type>::type;

template <class T>
using is_signed_int = typename std::conditional<(is_integral<T>::value &&
                                                 std::is_signed<T>::value) ||
                                                    is_signed_int128<T>::value,
                                                std::true_type,
                                                std::false_type>::type;

template <class T>
using is_unsigned_int =
    typename std::conditional<(is_integral<T>::value &&
                               std::is_unsigned<T>::value) ||
                                  is_unsigned_int128<T>::value,
                              std::true_type,
                              std::false_type>::type;

template <class T>
using to_unsigned = typename std::conditional<
    is_signed_int128<T>::value,
    make_unsigned_int128<T>,
    typename std::conditional<std::is_signed<T>::value,
                              std::make_unsigned<T>,
                              std::common_type<T>>::type>::type;

#else

template <class T> using is_integral = typename std::is_integral<T>;

template <class T>
using is_signed_int =
    typename std::conditional<is_integral<T>::value && std::is_signed<T>::value,
                              std::true_type,
                              std::false_type>::type;

template <class T>
using is_unsigned_int =
    typename std::conditional<is_integral<T>::value &&
                                  std::is_unsigned<T>::value,
                              std::true_type,
                              std::false_type>::type;

template <class T>
using to_unsigned = typename std::conditional<is_signed_int<T>::value,
                                              std::make_unsigned<T>,
                                              std::common_type<T>>::type;

#endif

template <class T>
using is_signed_int_t = std::enable_if_t<is_signed_int<T>::value>;

template <class T>
using is_unsigned_int_t = std::enable_if_t<is_unsigned_int<T>::value>;

template <class T> using to_unsigned_t = typename to_unsigned<T>::type;

}  // namespace internal
// Reference: https://en.wikipedia.org/wiki/Fenwick_tree
template <class T> struct fenwick_tree {
    using U = internal::to_unsigned_t<T>;

  public:
    fenwick_tree() : _n(0) {}
    fenwick_tree(int n) : _n(n), data(n) {}

    void add(int p, T x) {
        assert(0 <= p && p < _n);
        p++;
        while (p <= _n) {
            data[p - 1] += U(x);
            p += p & -p;
        }
    }

    T sum(int l, int r) {
        assert(0 <= l && l <= r && r <= _n);
        return sum(r) - sum(l);
    }

  private:
    int _n;
    std::vector<U> data;

    U sum(int r) {
        U s = 0;
        while (r > 0) {
            s += data[r - 1];
            r -= r & -r;
        }
        return s;
    }
};

}  // namespace atcoder


ll solve(vector<T> Ls, vector<T> Ds) {
    atcoder::fenwick_tree<int> St(MAX+1);
    priority_queue<T, vector<T>, greater<T>> q;
    for (auto &[y, maxx] : Ls) {
        St.add(MAX-y, 1);
        q.push({maxx, MAX-y});
    }
    ll ans = 0;
    for (auto &[x, maxy] : Ds) {
        while (!q.empty() && q.top().first < x) {
            int y = q.top().second;
            //cout << y << " ";
            St.add(y, -1);
            q.pop();
        }
        ll s = St.sum(0, maxy);
        // cout << s << " ";
        ans += s;
    }
    //cout << ans << endl;
    return ans;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M; cin >> N >> M;
    vector<T> Ls, Rs, Us, Ds;
    set<T> S1, S2;
    T p;
    ll ans = 1ll;
    for (int i=0; i<N; i++) {
        int y, lx, rx; cin >> y >> lx >> rx;
        if (lx == 0 && rx == MAX) {
            ans += 1ll;
        } 
        if (lx == 0) {
            p = {rx, y};
            Ls.push_back({MAX-y, rx});
        } else {
            Rs.push_back({y, MAX-lx});
            p = {lx, y};
        }
        if (S1.count(p)) ans++;
        S1.insert(p);
    }
    for (int i=0; i<M; i++) {
        int x, ly, ry; cin >> x >> ly >> ry;
        if (ly == 0 && ry == MAX) {
            ans += 1ll;
        } 
        if (ly == 0) {
            p = {x, ry};
            Ds.push_back({x, ry});
        } else {
            Us.push_back({MAX-x, MAX-ly});
            p = {x, ly};
        }
        if (S2.count(p)) ans++;
        S2.insert(p);
    }
    sort(Ls.begin(), Ls.end());
    sort(Rs.begin(), Rs.end());
    sort(Us.begin(), Us.end());
    sort(Ds.begin(), Ds.end());
    ans += solve(Ls, Ds);
    ans += solve(Ds, Rs);
    ans += solve(Rs, Us);
    ans += solve(Us, Ls);

    cout << ans << endl;
}