#include<bits/stdc++.h>
using namespace std;
int main()
{
int a; cin>>a;
vector<int>v1(a),v2(a);
for(int i=0;i<a;i++)
{
	cin>>v1[i];
	v2[i]=v1[i];
}
sort(v2.begin(),v2.end());
if(v1==v2)
	return cout<<"yes\n"<<1<<" "<<1<<endl,0;
int x=-1,y=0;
for(int i=0;i<a;i++)
{
	if(v1[i]!=v2[i])
	{
		if(x==-1)
		x=i;
		else
		y=i;
	}

}
reverse(v1.begin()+x,v1.begin()+y+1);
if(v1!=v2)
	cout<<"no\n";
else
	cout<<"yes\n"<<x+1<<" "<<y+1<<endl;
	return 0;
}
