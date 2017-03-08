#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int n,op[100100];
vector <int> v;

inline void Solve(int last,int now)
{
	if(v.size()==0)
	{
		cout<<"0\n";
		return;
	}
	if(v.size()==1)
	{
		cout<<"pushStack\n";
		cout<<"1 popStack\n";
		return;
	}
	if(v.size()==2)
	{
		cout<<"pushStack\n";
		cout<<"pushQueue\n";
		cout<<"2 popStack popQueue\n";
		return;
	}
	sort(v.begin(),v.end());
	for(int i=last;i<=now;i++)
	{
		if(op[i]==-v[0])
		{
			cout<<"pushStack\n";
			v[0]=1;
			continue;
		}
		if(op[i]==-v[1])
		{
			cout<<"pushQueue\n";
			v[1]=1;
			continue;
		}
		if(op[i]==-v[2])
		{
			cout<<"pushFront\n";
			v[2]=1;
			continue;
		}
		cout<<"pushBack\n";
	}
	cout<<"3 popStack popQueue popFront\n";
}

int main()
{
	int i,last=1;
	cin>>n;
	for(i=1;i<=n;i++)
	{
		cin>>op[i];
		if(op[i]!=0)
			v.push_back(-op[i]);
		else
		{
			Solve(last,i-1);
			v.clear();
			last=i+1;
		}
	}
	n=v.size();
	while(n--)
		cout<<"pushStack\n";
	return 0;
}
