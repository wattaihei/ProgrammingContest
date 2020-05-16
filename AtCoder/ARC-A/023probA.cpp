#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int day(int y, int m, int d){
    if (m == 1 || m == 2){
        m += 12;
        y -= 1;
    }
    return 365*y + y/4 - y/100 + y/400 + 306*(m+1)/10 + d - 429;
}

int main() {
    int y, m, d; cin >> y >> m >> d;
    int d1 = day(y, m, d);
    int d2 = day(2014, 5, 17);
    cout << d2 - d1 << endl;
}