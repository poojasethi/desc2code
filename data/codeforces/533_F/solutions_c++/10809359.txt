#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#define rep(i,a,b) for (int i=a;i<=b;i++)
#define drep(i,a,b) for (int i=a;i>=b;i--)
#define INF int(1e8)
#define LL long long
#define LD long double
#define pb push_back
#define mp make_pair
#define Pi M_PI
#define clr(a) memset(a,0,sizeof(a));
using namespace std;
template<class T> inline T min(T &a,T &b) {return a<b?a:b;}
template<class T> inline T max(T &a,T &b) {return a>b?a:b;}
const int N=320000;
const int Mod=1000000007;
vector<int> ans;
char s[N],t[N];
int vis[1000],ss[100],tt[100],ttt[100],tmp[100],n,m;
void check(int w)
{
	rep(i,0,25) vis[i]=0;
	rep(i,0,25)
		rep(j,0,25)
		if (!vis[j] && ss[i]==tt[j] && ss[j]==tt[i])
		{
			vis[j]=1;
			break;
		}
	rep(i,0,25)
		if (!vis[i]) return;
	ans.pb(w);
}
int main()
{
	scanf("%d%d",&n,&m);
	scanf("%s%s",s+1,t+1);
	rep(i,1,m)
		rep(j,0,25)
		{
			if (t[i]-'a'==j) tt[j]=(tt[j]*2+1)%Mod;
			else tt[j]=(tt[j]*2)%Mod;
		}
	int cc=1;
	rep(i,1,m-1) cc=cc*2%Mod;
	rep(i,1,m)
	{
		rep(j,0,25)
		{
			if (s[i]-'a'==j) ss[j]=(ss[j]*2+1)%Mod;
			else ss[j]=(ss[j]*2)%Mod;
		}
	}
	check(1);
	rep(i,m+1,n)
	{
		ss[s[i-m]-'a']=(ss[s[i-m]-'a']-cc)%Mod;
		if (ss[s[i-m]-'a']<0) ss[s[i-m]-'a']+=Mod;
		rep(j,0,25) ss[j]=(ss[j]*2)%Mod;
		ss[s[i]-'a']++;
		ss[s[i]-'a']%=Mod;
		check(i-m+1);
	}
	cout<<ans.size()<<endl;
	for (int i=0;i<ans.size();i++) printf("%d ",ans[i]);puts("");
}
