#include <bits/stdc++.h>
#define fi first
#define se second
using namespace std;

typedef pair < int , int > ii;

const int maxn = 2020;

int p[maxn],pos[maxn],n;
vector < ii > ans;

int main(){
	
	scanf("%d",&n);
	
	for( int i=1 ; i <= n ; i++ )
		scanf("%d",&p[i]);
	
	for( int i=1,x ; i <= n ; i++ ){
		scanf("%d",&x);
		pos[x] = i;
	}
	
	int res = 0;
	
	for( int i=n ; i ; i-- ){
		
		if( pos[p[i]] <= i )
			continue;
		
		int cur = i;
		
		for( int j=i+1 ; j <= pos[p[cur]] ; j++ )
			if( pos[p[j]] <= cur ){
				ans.push_back(ii(cur,j));
				res += abs( cur-j );
				swap( p[cur] , p[j] );
				cur = j;
			}
	}
	
	printf("%d\n%u\n",res,ans.size());
	
	for( int i=0 ; i < (int)ans.size() ; i++ )
		printf("%d %d\n",ans[i].fi,ans[i].se);
	
	return 0;
}
