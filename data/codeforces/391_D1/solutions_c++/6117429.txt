/****
	*@PoloShen
	*Title:D1
	*/
//#pragma comment(linker, "/STACK:1024000000,1024000000")
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <complex>
using namespace std;

#include <vector>
#include <list>
#include <stack>
#include <deque>
#include <queue>

typedef complex<int> point;

#define x real()
#define y imag()

struct Shu{
    int xbg, ybg;
    int length;
    point getmidViaShu(){
        return (xbg, double(length / 2.0) + ybg);
    }
};

struct Hen{
    int xbg, ybg;
    int length;
    point getmidViaShu(){
        return (double(length / 2.0) + xbg, ybg);
    }
};

inline point getCross(Shu s, Hen h){ point p(s.xbg, h.ybg); return p; }

Shu data1[1005];
Hen data2[1005];

int n, m;

void solve(){
    for (int i = 0; i < n; i++){
        scanf("%d%d%d", &data1[i].xbg, &data1[i].ybg, &data1[i].length);
    }
    for (int i = 0; i < m; i++){
        scanf("%d%d%d", &data2[i].xbg, &data2[i].ybg, &data2[i].length);
    }
    int ans = 0;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            point st = getCross(data1[i], data2[j]);
            int temp = data1[i].length;
            int stshuup = data1[i].ybg + data1[i].length - st.y;
            if (stshuup < 0) continue;
            else {
                int stshudown = st.y - data1[i].ybg;
                if (stshudown < 0) continue;
                else {
                    temp = min(stshudown, stshuup);
                    int sthenleft = st.x - data2[j].xbg;
                    if (sthenleft < 0) continue;
                    else {
                        temp = min(temp, sthenleft);
                        int sthenright = data2[j].xbg + data2[j].length - st.x;
                        if (sthenright < 0) continue;
                        else {
                            temp = min(temp, sthenright);
                            ans = max(ans, temp);
                        }
                    }
                }
            }
        }
    }
    cout << ans << endl;
}

int main(){
    while (cin >> n >> m) solve();
    return 0;
}