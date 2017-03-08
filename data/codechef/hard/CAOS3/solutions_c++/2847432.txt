#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#define x getchar_unlocked()
#define lli long long int
#define mod 1000000007
#define inf 999999999
#define ii pair<int,int>
using namespace std;

inline void inp(int &n ) {//fast input function
	n=0;
	int ch=x,sign=1;
	while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=x;}
	while( ch >= '0' && ch <= '9' )
		n=(n<<3)+(n<<1)+ ch-'0', ch=x;
	n=n*sign;
}
int game[20][20][20][20],A[20][20],n,m;

int find(int i1,int i2,int j1,int j2) {

	// cout<<"yo\n";
	if(i1>i2 || j1>j2)
		return 0;
	// cout<<"yo\n";
	if(game[i1][i2][j1][j2]!=-1)
		return game[i1][i2][j1][j2];
// cout<<"yo\n";
	int ans=0,num,val=0;

	set<int> s;
	for(int i=i1;i<=i2;i++) {
		for(int j=j1;j<=j2;j++) {
			if(A[i][j]) {
				num=0;

				num^=find(i1,i-1,j1,j-1);
				num^=find(i1,i-1,j+1,j2);
				num^=find(i+1,i2,j1,j-1);
				num^=find(i+1,i2,j+1,j2);

				s.insert(num);
			}
		}
	}

	while(s.find(ans)!=s.end())
		ans++;
	game[i1][i2][j1][j2]=ans;
	return ans;
}
int main() {
	int t,ans,a,num;
	char s[20][21];
	inp(t);
	while(t--) {
		inp(n);
		inp(m);

		for(int i=0;i<n;i++)
			scanf("%s",s[i]);
		
		memset(A,0,sizeof A);
		memset(game,-1,sizeof game);

		for(int i=2;i<n-2;i++) {
			for(int j=2;j<m-2;j++) {
				if(s[i][j]=='^') {
					num=inf;
					a=0;

					int k=j+1;
					while(k<m && s[i][k]=='^') {
						a++;
						k++;
					}
					num=min(num,a);

					k=j-1;
					a=0;
					while(k>=0 && s[i][k]=='^')
						a++,k--;

					k=i+1;
					num=min(num,a);
					a=0;

					while(k<n && s[k][j]=='^')
						a++,k++;
					num=min(num,a);

					k=i-1;
					a=0;
					while(k>=0 && s[k][j]=='^')
						a++,k--;

					num=min(num,a);
					if(num>1)
						A[i][j]=1;
				}
			}
		}

		// for(int i=0;i<n;i++) {
		// 	for(int j=0;j<m;j++)
		// 		cout<<A[i][j]<<" ";
		// 	cout<<endl;
		// }

		ans=find(0,n-1,0,m-1);

		if(ans)
			printf("Asuna\n");
		else
			printf("Kirito\n");
	}
	return 0;
}