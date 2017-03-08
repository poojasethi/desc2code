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
#include<cmath>
#include<stack>
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
long long Dnums[10000000];
int masks[10000000];
int bar[2000];
int Dnums_size = 0, curr = 0, foo, baz;
long long L,R;

int main()
{
    for(int i=0;i<=10;i++)
    bar[1<<i] = i;
    for(int i=1;i<=9;i++)
    {
        Dnums[Dnums_size] = i;
        masks[Dnums_size] = ((1<<10)-1)^(1<<i);
        Dnums_size++;
    }
    while(curr<Dnums_size)
    {
//        cout<<Dnums_size<<endl;
        foo = masks[curr];
        while(foo)
        {
            baz = foo & (-foo);
            Dnums[Dnums_size] = 10*Dnums[curr] + bar[baz];
            masks[Dnums_size] = masks[curr]^(1<<bar[baz]);
            Dnums_size++;
            foo ^= baz;
        }
        curr++;
    }
    in_T
    {
        scanf("%lld%lld", &L, &R);
        printf("%d\n", upper_bound(Dnums, Dnums + Dnums_size, R) - lower_bound(Dnums, Dnums + Dnums_size, L));
    }
}
