#include<iostream>
using namespace std;
#define MAX 101

struct inter {
		int x;
		int y;
	}a[MAX];
int used[1000];
int it=1;
int p=0,t1,t2;

bool check ( inter in1,inter in2) {
		if((in2.x<in1.x && in1.x<in2.y) || (in2.x<in1.y && in1.y <in2.y))
		return true;
	return false;
	}

void way(int q1)
{
used[q1]=1;
if(q1==t2) p=1;
for(int i=1;i<=it;i++)
	if(!used[i] && check(a[q1],a[i]))
		way(i);
	}

int  main()
{
int n,i,cmd,x,y;
int j;
	cin>>n;
	for(i=0;i<n;i++) {
	for(j=0;j<=1000;j++) 
		used[j]=0;
	p=0;
	cin>>cmd;
	if(cmd==1) { cin>>a[it].x>>a[it].y;it++; }
	if(cmd==2) {
		cin>>t1>>t2;
	way(t1);
	if(p)
		cout<<"YES\n"; else cout<<"NO\n";
	}
}
return 0;
}

