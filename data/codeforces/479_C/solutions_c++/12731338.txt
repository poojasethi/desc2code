#include<bits/stdc++.h>

using namespace std;

pair<int,int> a[5005];
int main(){
	int n;
	cin >> n;
	for(int i=0;i<n;i++)
		scanf("%d %d",&a[i].first,&a[i].second);
	sort(a,a+n);
	int cd=1;
	for(int i=0;i<n;i++){
		if(a[i].second>=cd)
			cd=a[i].second;
		else
			cd=a[i].first;
	}
	cout << cd << endl;
	return 0;
}

