
/*
2015-02-04 01:37
practice
FEB 15
*/
#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;

typedef long long int ll;

#define FOR(i,n) for(int i = 0; i < n; i++)
#define FORS(i,a,n) for(int i = a; i < n; i++)
#define RDARR(a,n) FOR(i,n) cin>>a[i];
#define SOLVE() int t;cin>>t;FOR(tc,t) solve();
#define PB push_back
#define MAX 4001


int ans[10][MAX]={0};

void precompute(){

	int temp,x,m;


	FOR(i,MAX){
		ans[0][i]=0;
		ans[1][i]=1;
	}
	FORS(i,2,10){
		int a[MAX];
		a[0]=i,m=1;
		ans[i][0]=1;
		ans[i][1]=i;
		FORS(j,2,MAX){
			temp=0;
			FOR(k,m){
				x=a[k]*i+temp;
				a[k]=x%10;
				temp=x/10;
			}
			while(temp){
				a[m++]=temp%10;
				temp/=10;
			}
			int sum=0;
			FOR(k,m)
				sum+=a[k];
			ans[i][j]=sum;


		}
	}
	//cout<<ans[2][32];

}


void solve(){
	int t,a,b;
	cin>>t;
	FOR(i,t){
		cin>>a>>b;
		cout<<"Case "<<i+1<<": "<<ans[a][b]<<endl;
	}
}

int main(){ _

	precompute();
	solve();
	//SOLVE()

	return 0;
}
