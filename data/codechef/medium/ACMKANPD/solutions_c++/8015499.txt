#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	while(1)
	{
		char ch[10000];
		char te[10000];
		char ch2[10000];
		char ch3[10000];
		int k=0;
		int j=0,i,flag;
		int ans=0;
		int count=0;
		ch[0]='\0';
		while(1)
		{
			cin>>te;
			strcat(ch,te);
	     	int	l=strlen(te);
			if(te[l-1]=='#'||te[l-1]=='~')
			break;
			strcat(ch," ");
		}
		if(ch[0]=='~')
		break;
		//
		for(i=0;ch[i]!='#';i++)
		{
			if(ch[i]=='"')
			{
				while(ch[i++]!='>');
				ch2[k++]=' ';
				i--;
			}
			else
			ch2[k++]=ch[i];
		}
		ch2[k]='\0';
		//cout<<ch2<<endl;
		for(i=0;i<k-2;i++)
		{
			if(ch2[i]==' ')
			continue;
			else if(ch2[i]=='0'&&ch2[i+1]==' ')
			{
				flag=1;
			}
			else if(ch2[i]=='0'&&ch2[i+1]=='0'&&ch2[i+2]==' ')
			{
				flag=0;
				i++;
			}
			else
			{
				count=0;
				while(ch2[i]=='0'&&i<k)
				{
					i++;
					count++;
				}
				count-=2;
				while(count>0)
				{
					ch3[j++]=flag+'0';
					count--;
				}
			}
		}
		count=1;
		for(i=j-1;i>=0;i--)
		{
			ans+=count*(ch3[i]-'0');
			count*=2;
		}
		cout<<ans<<endl;
	}
	return 0;
}