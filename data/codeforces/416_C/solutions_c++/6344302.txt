#include<bits/stdc++.h>

using namespace std;

struct req{
	int first;
	int second;
	int id;	
}r;

bool comp(req a,req b){
	return a.first<b.first;
}

int acr=0,money=0;
int n;
int k;
vector<req> lis,av;

int main(){
	cin>>n;
	int x,y;
	for(int i=0;i<n;i++){
		cin>>x>>y;
		r.first=y;
		r.second=x;
		r.id=i;
		lis.push_back(r);
	}
	sort(lis.begin(),lis.end(),comp);
	
	cin>>k;
	for(int i=0;i<k;i++){
		cin>>x;
		r.first=x;
		r.second=-1;
		r.id=i;
		av.push_back(r);
	}
	sort(av.begin(),av.end(),comp);
	
	for(int i=n-1;i>=0;i--)
		for(int j=0;j<k;j++)
			if(av[j].second< 0 && lis[i].second<=av[j].first){
				av[j].second = lis[i].id;
				money+=lis[i].first;
				acr++;
				break;
			}
	
	cout<<acr<<" "<<money<<endl;
	for(int i=0;i<k;i++)
		if(av[i].second>=0)
			cout<<av[i].second+1<<" "<<av[i].id+1<<endl;
}
