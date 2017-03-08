#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
using namespace std;

int N;
int mark[100003];
int vis[100003];
vector<pair<int,int> > ans;
int main(){
	for(int i=2;i*i<=100000;++i){
		if(mark[i])continue;
		for(int j=i;j*i<=100000;++j){
			mark[i*j]=1;
		}
	}
	scanf("%d",&N);
	for(int i=N/2;i>=2;--i){
		if(mark[i])continue;
		int cnt = 0;
		vector<int> st;
		for(int j=1;i*j<=N;++j){
			if(!vis[i*j]){
				++cnt;
				st.push_back(i*j);
			}
		}
		if(cnt%2){
			st.erase(st.begin()+1);
		}
		for(int j=0;j<st.size();j+=2){
			ans.push_back(make_pair(st[j],st[j+1]));
			vis[st[j]] = 1;
			vis[st[j+1]] = 1;
		}
	}
	printf("%d\n",(int)ans.size());
	for(int i=0;i<ans.size();++i){
		printf("%d %d\n",ans[i].first,ans[i].second);
	}
	return 0;
}