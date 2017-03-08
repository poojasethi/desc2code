#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
char ch;
bool flag=0;
int zero=0,ans=0;
ch=getchar();
while(ch!='~')
{
	if(ch=='0')
	{
		zero++;
	}
         else if(ch=='#')
         {
		cout<<ans<<endl;
		zero=0;
		ans=0;
         }
         else if(ch==' '||ch=='\n')
	 {
	 	if(zero==1)
		{
			flag=1;
		}
		else if(zero==2)
		{
			flag=0;
		}
	        else if(zero>2)
		{
			while(zero>2)
			{
				if(flag)
				{
					ans=2*ans+1;
				}
				else
				{
					ans=ans*2;
				}
				zero--;
			}

		}
		zero=0;
	 }
	// cout<<endl<<zero<<endl;
	 ch=getchar();
}
return 0;
}
/*
0 0000
00 000 0 0000
#
0 000
#
~
*/
