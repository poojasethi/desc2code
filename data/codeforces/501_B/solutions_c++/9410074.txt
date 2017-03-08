#include<bits/stdc++.h>
using namespace std;
int main(){
	int n;
	cin>>n;
	map<string,string> mp,rmp;
	map<string,int> hs;
	while(n--){
		string x,y;
		cin>>x>>y;
		if(rmp.find(x)!=rmp.end())
			x=rmp[x];
		else{
			mp[x]=x;
			hs[x]=1;
		}
		if(!hs[y]){
			mp[x]=y;
			rmp[y]=x;
			hs[y]=1;
		}
	}
	map<string,string>::iterator it;
	cout<<mp.size()<<endl;
	for(it=mp.begin();it!=mp.end();it++)
		cout<<it->first<<' '<<it->second<<endl;
}
		

