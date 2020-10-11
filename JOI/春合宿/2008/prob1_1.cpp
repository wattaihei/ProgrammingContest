#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

const int MAXN = 1e5, INF = 2e9;
int N, root;
int A[MAXN], Par[MAXN];

vector<int> graph[MAXN];

int solve() {
    int ans = -INF;

    int Score[N]; // max score if used n
    vector<int> stack = {root};
    while (!stack.empty()) {
        int p = stack[stack.size()-1]; stack.pop_back();
        if (p >= 0) {
            stack.push_back(~p);
            for (int np : graph[p]) {
                stack.push_back(np);
            }
        } else {
            p = ~p;
            Score[p] = A[p];
            for (int ch : graph[p]) {
                Score[p] += max(0, Score[ch]);
            }
            ans = max(ans, Score[p]);
        }
    }

    return ans;
}

int main() {
    cin >> N;
    for (int i=0; i<N; i++) {
        int s; cin >> s >> A[i];
        if (s == 0) root = i;
        else {
            graph[s-1].push_back(i);
            Par[i] = s-1;
        }
    }
    cout << solve() << endl;
}