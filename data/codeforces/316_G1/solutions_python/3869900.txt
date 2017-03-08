/* bhupkas */

#include "iostream"
#include "stdio.h"
#include "string.h"
#include "string"
#include "set"
#include "algorithm"
#include "map"

using namespace std;

#define FOR(i,a,b)	for(i=a;i<b;i++)

bool fun(string p,string t,int a,int b)
	{
		int i,j,s1=p.size(),s2=t.size(),cnt=0;
		i=0;
		while(i<s1-s2+1)
			{
				if(p[i]==t[0])
					{
						for(j=0;j<s2;j++)
							if(p[i+j]!=t[j])	break;
						if(j==s2)	cnt++;
					}
				i++;
			}
		if(cnt<=b && cnt>=a)	return true;
		return false;
	}

int main()
	{
		string t,s,p[11],temp;
		int n,i,j,k,a[11],b[11],ans=0;
		set<string> myset;
		set<string>::iterator it;
		cin>>s;
		getchar();
		cin>>n;
		FOR(i,0,n)
			{
				cin>>p[i];
				getchar();
				cin>>a[i]>>b[i];
				getchar();
			}
		FOR(i,0,s.size())
			{
				FOR(j,i,s.size())
					{
						temp=s.substr(i,j-i+1);
						it=myset.find(temp);
						if(it!=myset.end())	continue;
						myset.insert(temp);
						FOR(k,0,n)	
							{
								if(!fun(p[k],temp,a[k],b[k]))	break;
							}
						if(k==n)	ans++;
					}
			}
		cout<<ans<<endl;
		return 0;
	}