#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#define ll long long
using namespace std;
const ll maxn= 6e5,mo= 1e9+7;
char s[maxn];
ll sta[maxn];
ll X[maxn],Y[maxn];
ll ans,cnt;
ll n,h,w,i,j,la;
ll xi,yi,xa,ya,Xi,Yi,Xa,Ya,xx,yy,flag;
void update(ll &ans,ll x){
	ans= (ans+cnt*x)%mo;
}
bool move(char c){
	bool bl= 0;
	if (c=='L'){
		yy--;
		if (yy<Yi){
			Yi--;
			update(ans,xa-xi+1);
			yi++;
			bl= 1;
		}
	}
	if (c=='R'){
		yy++;
		if (yy>Ya){
			Ya++;
			update(ans,xa-xi+1);
			ya--;
			bl= 1;
		}		
	}
	if (c=='U'){
		xx--;
		if (xx<Xi){
			Xi--;
			update(ans,ya-yi+1);
			xi++;
			bl= 1;
		}				
	}
	if (c=='D'){
		xx++;
		if (xx>Xa){
			Xa++;
			update(ans,ya-yi+1);
			xa--;
			bl= 1;
		}						
	}
	return bl;
}
void Move(ll x,ll y){
	xx+= x;
	yy+= y;
}
int main()
{
	//freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
	scanf("%I64d%I64d%I64d%s",&n, &h, &w, s+1);
	xi= yi= 1;
	xa= h;
	ya= w;
	flag= 1;
	for (i= 1;i<=n;i++){
		if (s[i]=='L') Y[i]= -1;
		if (s[i]=='R') Y[i]= 1;
		if (s[i]=='U') X[i]= -1;
		if (s[i]=='D') X[i]= 1;
		X[i]+= X[i-1];
		Y[i]+= Y[i-1];
	}
	for (i= 1;i<=n;i++){
		cnt++;
		move(s[i]);
		if (xi>xa||yi>ya){
			flag= 0;
			break;
		}
	}
	if (!flag){
		printf("%I64d\n",ans);
		return 0;
	}
	for (i= 1;i<=n;i++){
		cnt++;
		if (move(s[i]))
			sta[++la]= i;		
		if (xi>xa||yi>ya){
			flag= 0;
			break;
		}
	}
	if (!flag){
		printf("%I64d\n",ans);
		return 0;
	}
	if (!la){
		printf("-1");
		return 0;
	}
	while (xi<=xa&&yi<=ya){
		for (i= 1;i<=la;i++){
			cnt= (cnt+sta[i]-sta[i-1])%mo;
			ll vx= X[sta[i]-1]-X[sta[i-1]];
			ll vy= Y[sta[i]-1]-Y[sta[i-1]];
			Move(vx,vy);			
			move(s[sta[i]]);
			if (xi>xa||yi>ya)
				break;
		}
		ll vx= X[n]-X[sta[la]];
		ll vy= Y[n]-Y[sta[la]];
		Move(vx,vy);
		cnt= (cnt+n-sta[la])%mo;
	}
	printf("%I64d\n",ans);
	return 0;
}
