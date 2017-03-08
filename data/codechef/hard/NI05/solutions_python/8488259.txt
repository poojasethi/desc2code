#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sz size()
#define all(a)  a.begin(), a.end()
#define allr(a) a.rbegin(), a.rend()
#define SL(n) scanf("%lld", &n)
#define fill(a, x) memset(a, x, sizeof(a));
#define mod 1000000007
#define eps 0.000000001

using namespace std;
typedef long long LL;
typedef vector <LL> VL;
typedef map <LL, LL> ML;
typedef pair<LL, LL> PL;
typedef vector <PL> VPL;

int dp[1029][1029];
int a[11];
int Usable[11];

bool isSet(int x, int mask){
    return (mask & (1 << x));
}

int Set(int x, int mask){
    //x = 10 - x - 1;
    return (mask | (1 << x));
}

int inp[11][11] = {{55,60,4,25,18,10,12,8,11,50}, {60,45,75,23,27,20,24,7,33,12}, {4,75,78,32,36,30,36,6,12,65}, 
{25,23,32,15,45,40,48,5,14,23}, {18,27,36,45,54,50,60,4,15,12}, {10,20,30,40,50,60,72,3,32,34},
{12,24,36,48,60,72,84,2,23,34}, {8,7,6,5,4,3,2,1,34,123}, {11,33,12,14,15,32,23,34,65,48}, 
{50,12,65,23,12,34,34,123,48,71}};

int Solve(int mask1, int mask2){
    //cout << mask1 << " " << mask2 << endl;
    if(dp[mask1][mask2] != -1){
        return dp[mask1][mask2];
    }
    int Ans = 0;
    for(int n=0;n<10;++n){
        for(int m=0;m<10;++m){
            if(Usable[n] == 1 && Usable[m] == 1){
                if(n == m){
                    if(isSet(n, mask1) == 0){
                        int tmask1 = mask1;
                        int tmask2 = mask2;
                        tmask1 = Set(n, tmask1);
                        tmask2 = Set(n, tmask2);
                        Ans = max(Ans, inp[n][m] + Solve(tmask1, tmask2));
                    }
                }
                else{
                    int tmask1 = mask1;
                    int tmask2 = mask2;
                    if((isSet(n, mask1) == 0 || isSet(n, mask2) == 0) && (isSet(m, mask1) == 0 || isSet(m, mask2) == 0)){
                        if(isSet(n, mask1) == 0){
                            tmask1 = Set(n, tmask1);
                        }
                        else{
                            tmask2 = Set(n, tmask2);
                        }
                        if(isSet(m, tmask1) == 0){
                            tmask1 = Set(m, tmask1);
                        }
                        else{
                            tmask2 = Set(m, tmask2);
                        }
                        Ans = max(Ans, inp[n][m] + Solve(tmask1, tmask2));
                    }
                }
            }
        }
    }
    return (dp[mask1][mask2] = Ans);
}
int main() {
    int T , lll ;
    cin >> T;
    while(T--){
        for(int n=0;n<10;++n){
            scanf("%d", &a[n]);
            if(a[n] >= 2){
                a[n] = 2;
            }
        }
        
        fill(dp, (int)-1);
        fill(Usable, (int)0);
        for(int n=0;n<(int)10;++n){
            scanf("%d", &Usable[n]);
        }
        int Ans = 0;
        Ans = max(Ans, Solve(0, 0));
        /*
        for(int n=0;n<10;++n){
            cout << dp[lll][lll][n] << endl;
        }
        */
        printf("%d\n", Ans);
    }
    return 0;
}