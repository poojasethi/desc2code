#include<bits/stdc++.h>

using namespace std;

int a[105],b[105];
int main(){
	int m,n;
	cin >> m;
	for(int i=0;i<m;i++)
		cin >> a[i];
	cin >> n;
	for(int i=0;i<n;i++)
		cin >> b[i];
	sort(a,a+m);
	sort(b,b+n);
	int i=0,j=0,cnt=0;
	while(i<m&&j<n){
		if(abs(a[i]-b[j])<2){cnt++;i++;j++;}
		else if(a[i]>b[j]+1)j++;
		else if(b[j]>a[i]+1)i++;
	}
	cout << cnt << endl;
	return 0;
}
	

