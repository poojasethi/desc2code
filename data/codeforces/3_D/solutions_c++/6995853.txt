#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <string>
using namespace std;
typedef pair<int,int> pii;
typedef long long LL;
const int maxn=50010;
int main()
{
	string str;
	cin>>str;
	int flag=0;
	LL val=0;
	priority_queue<pii> q;
	for(int i=0;i<str.size();i++)
	{
		if(str[i]=='(') flag++;
		else if(str[i]==')') flag--;
		else
		{
			flag--;
			int a,b;
			cin>>a>>b;
			val+=b;
			str[i]=')';
			q.push(make_pair(b-a,i));
		}
		if(flag<0)
		{
			if(q.empty()) break;
			flag+=2;
			pii tmp=q.top();q.pop();
			val-=tmp.first;
			str[tmp.second]='(';
		}
	}
	if(flag!=0) puts("-1");
	else
	{
		cout<<val<<"\n"<<str<<"\n";
	}
	return 0;
}
