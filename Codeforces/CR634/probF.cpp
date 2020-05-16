#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

int Q,N,M;


int main() {
    cin >> Q;
    for (int q=0; q<Q; q++){
        cin >> N >> M;
        char Color[N][M];
        char Field[N][M];
        for (int i=0; i<N; i++){
            for (int j=0; j<M; j++){
                cin >> Color[i][j];
            }
        }
        for (int i=0; i<N; i++){
            for (int j=0; j<M; j++){
                cin >> Field[i][j];
            }
        }
    }

}