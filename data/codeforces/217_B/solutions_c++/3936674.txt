/* bhupkas */

#include "iostream"
#include "stdio.h"
#include "set"
#include "algorithm"
#include "vector"
#include "string"
#include "string.h"

using namespace std;

#define FOR(i,a,b)	for(i=a;i<b;i++)

char S[1000050],S1[1000050];
int ans=100000000;

int n,r;

void fun(int a,int b)
	{
		int i,cur;
		for(cur=n-1;cur>=0&&a*b!=0;cur--)
			{
				if(a>=b)	{a-=b;	S[cur]='T';}
				else		{b-=a;	S[cur]='B';}	
			}
		if(cur!=-1 || !(a==0 && b==1))	return;
		int co=0;
		FOR(i,1,n)
			{
				if(S[i]==S[i-1])	co++;
			} 
		if(co<ans)
			{
				ans=co;
				FOR(i,0,n)	S1[i]=S[i];
			}
	}

int main()
	{
		
		int i,j;
		cin>>n>>r;
		FOR(i,0,r+1)
			{
				fun(i,r);
				fun(r,i);
			}
		if(ans==100000000)	
			{
				cout<<"IMPOSSIBLE"<<endl;	return 0;
			}
		else
			{
				cout<<ans<<endl;
				FOR(i,0,n)	
					cout<<S1[i];
				cout<<endl;
			}
		return 0;
	}