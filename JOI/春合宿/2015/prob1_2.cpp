#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

int K;
string S;

int solve() {
    string joi = "JOI";
    unordered_map<int, char> shouldBeBefore, shouldBeAfter;
    int ind = -1;
    int score = 0, bd = 0;
    for (int k=K-1; k>=0; k--) {
        for (int i=0; i<3; i++) {
            for (int j=0; j<(1<<(2*k)); j++) {
                int l = j+ind+1;
                if (S[l] != joi[i]) score++;
            }
            if (S[ind+1] != joi[i]) bd++;
            shouldBeBefore[ind+1] = joi[i];
            ind += 1<<(2*k);
            shouldBeAfter[ind] = joi[i];
        }
    }

    int ans = score;
    for (int start=1; start<(1<<(2*K)); start++) {
        for (auto& [i, s] : shouldBeBefore) {
            if (S[(start+i-1)%(1<<(2*K))] != s) score--;
        }
        for (auto& [i, s] : shouldBeAfter) {
            if (S[(start+i)%(1<<(2*K))] != s) score++;
        }
        ans = min(ans, score);
    }

    return ans;
}

int main() {
    cin.tie(nullptr);
    cin >> K;
    cin >> S;
    cout << solve() << endl;
}