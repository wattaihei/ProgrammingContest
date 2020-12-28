#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;


struct S {
    int s, p, par;
};


class comp {
    public:
    bool operator() (S a, S b) {
        return a.s > b.s;
    }
};

const int INFINT = 2e9;
const ll INFLL = 2e18;
const int MAXN = 10000;

vector<int> Childs(MAXN, 0), Parent(MAXN), A(MAXN);

void solve() {
    int N, M;
    cin >> N >> M;
    int s, a;
    
    for (int i=0; i<N; i++) {
        cin >> s >> a;
        s--;
        if (s != -1) {
            Childs[s]++;
        }
        Parent[i] = s;
        A[i] = a;
    }

    priority_queue<S, vector<S>, comp> q;
    int ans = 0;
    for (int i=0; i<N; i++) {
        if (Childs[i] == 0) {
            int w = i, s = 0;
            while (Childs[w] < 2) {
                s += A[w];
                w = Parent[w];
            }
            q.push({s, i, w});
        }
        ans += A[i];
    }

    while (q.size() > M) {
        S s = q.top(); q.pop();
        if (Childs[s.par] > 1) {
            Childs[s.par]--;
            ans -= s.s;
        } else {
            while (Childs[s.par] < 2) {
                s.s += A[s.par];
                s.par = Parent[s.par];
            }
            q.push(s);
        }
    }

    cout << ans << endl;

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}