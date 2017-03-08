#include<bits/stdc++.h>

using namespace std;

int main(){
	int n,left=0,right=0,sum=0;
	cin >> n;
	vector< pair<int,int> > v(n);
	for(int i=0;i<n;i++){
		scanf("%d%d",&v[i].first,&v[i].second);
		(v[i].first>0) ? (right++) : (left++);
	}
	sort(v.begin(),v.end());
	if(left==right)
		for(int i=0;i<n;i++)
			sum+=v[i].second;
	else if(left>right)
		for(int i=left-right-1;i<n;i++)
			sum+=v[i].second;
	else
		for(int i=0;i<n-(right-left-1);i++)
			sum+=v[i].second;
	cout << sum << endl;
}
