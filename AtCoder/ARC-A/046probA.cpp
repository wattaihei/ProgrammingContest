#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main() {
    int N; cin >> N;
    if (N%9 == 0){
        for (int i=0; i<(N/9); i++){
            cout << 9;
        }
    }
    else{
        for (int i=0; i<=(N/9); i++){
            cout << N%9;
        }
    }
    cout << endl;
}