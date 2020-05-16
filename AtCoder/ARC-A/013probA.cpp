#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int a[3]; cin >> a[0] >> a[1] >> a[2];
    int b[3]; cin >> b[0] >> b[1] >> b[2];
    sort(a, a+3);
    sort(b, b+3);
    int ans = 0;
    for (int i=0; i<3; i++){
        for (int j=0; j<3; j++){
            if (i==j){
                continue;
            }
            for (int k=0; k<3; k++){
                if (k==i || k==j) {
                    continue;
                }
                ans = max(ans, (a[0]/b[i])*(a[1]/b[j])*(a[2]/b[k]));
            }
        }
    }
    cout << ans << endl;
}