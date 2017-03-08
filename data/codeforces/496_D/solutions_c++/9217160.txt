#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

const int N=100100;
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)>(b)?(b):(a))
int arr[N];
int s0[N+1],s1[N+1],p0[N],p1[N];
int cnt0,cnt1;
int main(){
	std::ios::sync_with_stdio(0);

	int n;
	cin>>n;
	int i;
	for(i=0;i<n;i++){
		cin>>arr[i];
		if(arr[i]==1)
			p0[cnt0++]=i;
		else
			p1[cnt1++]=i;
		s0[i+1]=s0[i]+(arr[i]==1);
		s1[i+1]=s1[i]+(arr[i]==2);
	}
    
	vector<pair<int,int> > ans;
	for(int k=1;k<=n;k++){
		int t0=0,t1=0;
		int flag=0;
		int ok=1;
		i=0;
		while(i<n){
			int j0=s0[i]+k>cnt0?n+1:(p0[s0[i]+k-1]+1);
			int j1=s1[i]+k>cnt1?n+1:(p1[s1[i]+k-1]+1);
			if(min(j0,j1)>n){
				ok=0;
				break;
			}
			if(j0<j1){
				i=j0;
				t0++;
				flag=0;
			}
			else{
				i=j1;
				t1++;
				flag=1;
			}
		}
		if(t0==t1 || (t0<t1)^flag){
			ok=0;
		}
		if(ok){
			ans.push_back(make_pair(max(t0,t1),k));
		}
	}
    sort(ans.begin(),ans.end());

cout<<ans.size()<<endl;
	for(i=0;i<ans.size();i++)
		cout<<ans[i].first<<" "<<ans[i].second<<endl;

	return 0;
}