#include<bits/stdc++.h>

using namespace std;

int main()
{
	int n,a,b;
	char ch;
	int f[444]={0},m[444]={0};


	scanf("%d",&n);

	for(int i=0;i<n;i++){
		scanf(" %c %d %d",&ch,&a,&b);
		for(int j=a;j<=b;j++){
			if(ch=='F') f[j]++;
			else m[j]++;
		}
	}

	int ans=0;

	for(int i=1;i<367;i++){
		int temp=min(m[i],f[i]);
		ans=max(ans,temp);
	}

	cout<<ans*2<<endl;


	return 0;

}
