#include <bits/stdc++.h>
#include "grader.h"
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;



void Rescue(int R, int C, int MR, int MC, int X) {

    int rd = MR, ru = MR, ret;
    for (int c=1; c<=MC; c++) {
        while (rd != 0) {
            ret = Measure(rd, c);
            if (ret == X) {
                Pinpoint(rd, c);
                return;
            } else if (ret > X) {
                rd--;
            } else {
                break;
            }
        }
        while (ru != R+1) {
            ret = Measure(ru, c);
            if (ret == X) {
                Pinpoint(ru, c);
                return;
            } else if (ret > X) {
                ru++;
            } else {
                break;
            }
        }
    }

    rd = MR, ru = MR;
    for (int c=C; c>MC; c--) {
        while (rd != 0) {
            ret = Measure(rd, c);
            if (ret == X) {
                Pinpoint(rd, c);
                return;
            } else if (ret > X) {
                rd--;
            } else {
                break;
            }
        }
        while (ru != R+1) {
            ret = Measure(ru, c);
            if (ret == X) {
                Pinpoint(ru, c);
                return;
            } else if (ret > X) {
                ru++;
            } else {
                break;
            }
        }
    }
}