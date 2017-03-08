#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

typedef long long ll;	
const int M=100010;
const int mod=1000000007;
int n,m,join[2*M],cnt=0,ans[M],tot=0;
vector<int> v[M];
queue<int> q;

struct node{
	int val,no;
}rec[M];

bool cmp(node a,node b){
	return a.val<b.val;
}

void add(int x,int y){
	join[y]++;
	v[x].push_back(y);
}

int main(){
    ios::sync_with_stdio(0);
    cin>>n>>m;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cin>>rec[j].val;
			rec[j].no=j;
		}
		sort(rec,rec+m,cmp);
		for(int j=0;j<m;j++){
			if(rec[j].val<0) continue;
			if(!j||rec[j].val!=rec[j-1].val) cnt++;
			add(rec[j].no,m+cnt+1);
			add(m+cnt,rec[j].no);
		}
		cnt++;
	}
	for(int i=0;i<m+cnt;i++)
		if(!join[i]) q.push(i);
	while(!q.empty()){
		int t=q.front();
		q.pop();
		if(t<m) ans[tot++]=t;
		for(int i=0;i<v[t].size();i++){
			int tmp=v[t][i];
			join[tmp]--;
			if(!join[tmp]) q.push(tmp);
		}
	}
	if(tot<m) cout<<-1;
	else 
		for(int i=0;i<m;i++)
			cout<<ans[i]+1<<' ';
    return 0;
}