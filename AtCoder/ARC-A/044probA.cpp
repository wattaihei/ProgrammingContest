#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    ll N; cin >> N;
    bool prime = true;
    for (int i=2; i<=sqrt(N); i++){
        if (N%i == 0){
            prime = false;
        }
    }
    if (!prime && (N%2!=0 && N%3!=0 && N%5!=0)){
        prime = true;
    }
    if (prime && N!=1){
        cout << "Prime" << endl;
    }
    else{
        cout << "Not Prime" << endl;
    }
}