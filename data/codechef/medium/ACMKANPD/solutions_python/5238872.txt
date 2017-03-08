/*
*
*	FileName:
*	Created By: r3gz3n
*	Description:
*
*/

#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <istream>
#include <ostream>
#include <fstream>
#include <set>
#include <list>
#include <map>
#include <utility>
#include <stack>
#include <queue>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <cctype>
#include <climits>


#define ll long long
#define ull unsigned long long
#define ins(x) scanf("%s", x)
#define inc(x) scanf("%c", &x)
#define ini(x) scanf("%d", &x)
#define inl(x) scanf("%ld", &x)
#define inll(x) scanf("%lld", &x)
#define in2i(x, y) scanf("%d %d", &x, &y)
#define in2l(x, y) scanf("%ld %ld", &x, &y)
#define in2ll(x, y) scanf("%lld %lld", &x, &y)

using namespace std;

template<class T> inline void read(T&x){bool fu=0;char c;for(c=getchar();c<=32;c=getchar());if(c=='-')fu=1,c=getchar();for(x=0;c>32;c=getchar())x=x*10+c-'0';if(fu)x=-x;};
template<class T> inline void read(T&x,T&y){read(x);read(y);}
template<class T> inline void read(T&x,T&y,T&z){read(x);read(y);read(z);}
const long MOD = 1000000007;

int main()
{
    //freopen("input.txt", "r", stdin);
    string s;
    int flag, a[35], l, x;
    ll ans, A;
    while(cin >> s)
    {
        if(s == "~") break;
        l = s.size();
        if(l == 1) flag = 1;
        else flag = 0;
        x = 0;
        while(cin >> s)
        {
            if(s == "#") break;
            l = s.size();
            if(l == 1) flag = 1;
            else if(l == 2) flag = 0;
            else
            {
                l -= 2;
                for(int i = 0;i < l;++i)
                    a[x++] = flag;
            }
        }
        A = 1;
        ans = 0;
        for(int i = x-1;i >= 0;--i)
        {
            ans += (A*a[i]);
            A <<= 1;
        }
        cout << ans << endl;
    }
    return 0;
}
