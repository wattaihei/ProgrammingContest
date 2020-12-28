#include <bits/stdc++.h>
using namespace std;

// 比較関数
class comp {
    public:
    bool operator()(edge a, edge b) {
        return a.t > b.t;
    }
};

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

