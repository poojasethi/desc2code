/*
    Nimesh Ghelani (nims11)
*/
#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<map>
#include<string>
#include<vector>
#include<queue>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<cmath>
#include<stack>
#include<set>
#include<utility>
#define in_T int t;for(scanf("%d",&t);t--;)
#define in_I(a) scanf("%d",&a)
#define in_F(a) scanf("%lf",&a)
#define in_L(a) scanf("%lld",&a)
#define in_S(a) scanf("%s",a)
#define newline printf("\n")
#define MAX(a,b) a>b?a:b
#define MIN(a,b) a<b?a:b
#define SWAP(a,b) {int tmp=a;a=b;b=tmp;}
#define P_I(a) printf("%d",a)

using namespace std;
set<int> foo;
map<int, int> bar;
vector<int> foobar;
int main()
{
    foo.insert(1);

        foobar.push_back(0);
    bar[1] = -1;
        for(set<int>::iterator it = foo.begin(); it != foo.end(); it++){
            int cur = *it;
            int prev = 0;
            while(cur <= 1e8){
                if(foo.find(cur) == foo.end()){
                    foo.insert(cur);
                    bar[cur] = *it;
                }

                int tmp = cur;
                cur += prev;
                prev = tmp;
            }
            foobar.push_back(*it);
        }
        in_T{
            int L, R, N;
            in_I(L);
            in_I(R);
            in_I(N);
            int st = lower_bound(foobar.begin(), foobar.end(), L)-foobar.begin();
            int end = upper_bound(foobar.begin(), foobar.end(), R)-foobar.begin();
            if(end-st < N){
                printf("%d\n", -1);
            }else{
                int idx = foobar[st+N-1];
                if(idx == 0){
                    printf("0 .##.\n");
                    continue;
                }
                vector<int> res;
                res.push_back(idx);
                printf("%d .", idx);
                while(bar[idx] != -1){
                    idx = bar[idx];
                    if(idx != 1)
                    res.push_back(idx);
                }
                int cur = 1, prev = 1;
                for(int i = res.size()-1;i>=0;){
                    if(cur == 0)
                        printf("#");
                    else
                        printf(".");
                    if(cur == foobar[st+N-1])break;
                    if(cur == res[i]){
                        i--;
                        prev = cur;
                        cur = 0;
                    }else{
                        int tmp = cur;
                        cur += prev;
                        prev = tmp;
                    }
                }
                newline;
            }
        }
}
