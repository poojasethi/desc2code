#include<iostream>
#include<cstring>

using namespace std;
 
int flips(char s[],int n)
{
	int a=0,b=0;
	for(int i=0;i<n;i++)
	{
		if(s[i]=='a'||s[i]=='A')
			a++;
		else if(s[i]=='b'||s[i]=='B')
			b++;
	}
	if(a<b)
		return a;
	else
		return b;
} 
 
int main()
{
	int t;
	cin>>t;
	char s[100];
	int l;
	for(int i=0;i<t;i++)
	{
		cin>>s;
		l=strlen(s);
		cout<<flips(s,l)<<endl;
	}
	return 0;
}  