#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<set>
#include<utility>
#include<stack>
#include<queue>
#include<map>
using namespace std;



#define min(a,b) a<b?a:b
#define max(a,b) a>b?a:b

#define f(i,start,end) for(i=start;i<end;i++)
#define rep(i,n) for(i=0;i<n;i++)
#define INF INT_MAX
#define ALL(x) x.begine(),x.end()
#define pb push_back
#define  sz(x) int(x.size())
#define fill(x,v) memset(x,v,sizeof(x))


#define SI(a) scanf("%d",&a)
#define SC(a) scanf("%c",&a)
#define SL(a) scanf("%lld",&a)
#define SS(a) scanf("%s",a)
#define SF(a) scanf("%f",&a)
#define PI(a) printf("%d",a)
#define PL(a) printf("%lld",a)
#define LL long long

typedef pair<int,int> PI;
typedef vector<int> vec;
typedef vector<vec> matrix;

//int arr[100000];
int main()
{
	int n,k;
	SI(n);
	SI(k);
	int i,j,m;
	/*rep(i,n)
	{
		SI(arr[i]);
	}*/
	PI st[100000];
	
	rep(i,n){
		SI(m);
		st[i]=make_pair(m,i);
	}
	sort(st,st+n);
/*	rep(i,n){
		cout<<st[i].first <<" => " <<st[i].second<<endl;
	}
*/	int count=0;
	i=0;
	while(i<n)
	{
		count++;
		j=i+1;
	while(j<n)
	{
		if(st[i].first ==st[j].first && st[j].second - st[i].second < k)
		{
			j++;
		}
		else break;
	}
		//else 
	//	{
		//	count++;
			i=j;
		//	break;
		//}
//	cout << "i beacomes " << i<<endl;
	}

	

	cout<<count<<endl;

	return 0;
}

