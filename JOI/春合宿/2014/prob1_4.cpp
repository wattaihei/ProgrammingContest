#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;
#include "ramen.h"


vector<vector<int>> battle(vector<int> A, bool needWinner) {
    int K = A.size();
    vector<vector<int>> Result(2);
    for (int k=0; k<K/2; k++) {
        int a = A[2*k], b = A[2*k+1];
        int res = Compare(a, b);
        if (res == 1) {
            Result[1].push_back(a);
            Result[0].push_back(b);
        } else {
            Result[1].push_back(b);
            Result[0].push_back(a);
        }
    }
    if (K%2 == 1) {
        int mem = A[K-1];
        // battle with winner
        if (needWinner) {
            Result[1].push_back(mem);
        } else {
            Result[0].push_back(mem);
        }
    }
    return Result;
}

void Ramen(int N) {
    vector<int> Members;
    for (int i=0; i<N/2*2; i++) Members.push_back(i);

    vector<int> Winner, Loser;
    vector<vector<int>> FirstResult = battle(Members, true);
    if (N%2 == 1) {
        FirstResult[1].push_back(N-1);
        FirstResult[0].push_back(N-1);
    }
    Winner = FirstResult[1];
    Loser = FirstResult[0];
    while (Winner.size() > 1) {
        Winner = battle(Winner, true)[1];
    }
    while (Loser.size() > 1) {
        Loser = battle(Loser, false)[0];
    }
    int win = Winner[0], lose = Loser[0];
    Answer(lose, win);
}