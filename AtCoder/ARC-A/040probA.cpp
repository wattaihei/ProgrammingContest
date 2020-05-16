#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int N; cin >> N;
    string S[N];
    int red = 0, blue = 0;
    for (int i=0; i<N; i++){
        cin >> S[i];
        for (int j=0; j<N; j++){
            if (S[i][j] == 'R'){
                red += 1;
            }
            else if (S[i][j] == 'B'){
                blue += 1;
            }
        }
    }
    if (red > blue){
        cout << "TAKAHASHI" << endl;
    }
    else if (red < blue){
        cout << "AOKI" << endl;
    }
    else{
        cout << "DRAW" << endl;
    }
}