#include<bits/stdc++.h>

using namespace std;

int main(){
	int n,ub=2e9,lb=-2e9;
	scanf("%d",&n);
	while(n--){
		string s,ans;
		int num;
		cin>>s>>num>>ans;
		if(s==">"){
			if(ans=="Y")lb=max(lb,num+1);
			else ub=min(num,ub);
		}
		if(s=="<"){
			if(ans=="N")lb=max(lb,num);
			else ub=min(num-1,ub);
		}
		if(s==">="){
			if(ans=="Y")lb=max(lb,num);
			else ub=min(num-1,ub);
		}
		
		if(s=="<="){
			if(ans=="Y")ub=min(num,ub);
			else lb=max(lb,num+1);
		}
	}
	if(ub<lb)cout<<"Impossible"<<endl;
	else cout<<lb<<endl;
}
