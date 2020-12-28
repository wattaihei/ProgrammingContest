#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    int N; cin >> N;
    vector<int> A;
    for (int n=0; n<2*N; n++) {
        string a; cin >> a;
        if (a == "+") {
            A.push_back(0);
        } else {
            int p; cin >> p;
            A.push_back(p);
        }
    }
    reverse(A.begin(), A.end());
    vector<int> stack, ans;
    for (int a : A){
        if (a > 0) {
            if (stack.empty() || stack[stack.size()-1] > a) {
                stack.push_back(a);
            } else {
                cout << "NO" << endl;
                return;
            }
        } else {
            if (stack.empty()) {
                cout << "NO" << endl;
                return;
            } else {
                ans.push_back(stack[stack.size()-1]);
                stack.pop_back();
            }
        }
    }
    cout << "YES" << endl;
    reverse(ans.begin(), ans.end());
    for (auto a : ans) {
        cout << a << " "; 
    }
    cout << endl;
    
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}