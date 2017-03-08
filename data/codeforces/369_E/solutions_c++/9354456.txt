#include <bits/stdc++.h>
using namespace std;

#define lli long long int
#define ii pair<int,int>
#define mod 1000000007
#define inf 999999999
#define lim 300010

using namespace std;

int n,m;
ii A[lim];
vector<int> v[lim];
int ans[lim];

int in[1000001]={0},tree[1000001]={0};
vector<int> out[1000001];

vector<ii> query[1000001];

void upd(int idx,int val) {
	while(idx<1000001) {
		tree[idx]+=val;
		idx+=idx&-idx;
	}
}

int read(int idx) {
	int sum=0;
	while(idx>0) {
		sum+=tree[idx];
		idx-=idx&-idx;
	}
	return sum;
}

int main(){ 
	// cin.sync_with_stdio(false);
	cin>>n>>m;

	for(int i=0;i<n;i++) {
		cin>>A[i].first>>A[i].second;
		in[A[i].first]++;
		out[A[i].second].push_back(A[i].first);
	}

	for(int i=0;i<m;i++) {
		int num;
		cin>>num;
		v[i].resize(num);
		for(int j=0;j<num;j++) {
			cin>>v[i][j];
			query[v[i][j]].push_back(ii(i,j));
		}
		ans[i]=0;
	}


	for(int t=1;t<=1000000;t++) {
		upd(t,in[t]);

		// cout<<t<<" "<<in[t]<<endl;

		for(int i=0;i<query[t].size();i++) {
			ii p=query[t][i];

			if(p.second==0) {
				ans[p.first]+=read(t);
			}
			else {
				ans[p.first]+=read(t)-read(v[p.first][p.second-1]);
			}
		}


		for(int i=0;i<out[t].size();i++)
			upd(out[t][i],-1);
	}


	for(int i=0;i<m;i++)
		cout<<ans[i]<<endl;
	return 0;
}