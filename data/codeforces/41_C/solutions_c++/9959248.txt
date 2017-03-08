#include <iostream>
#include <string>
using namespace std;
int main()
{
	string s;
	int i;
	cin>>s;
	for (i=2;i<s.size();i++)
		if (s[i]=='t'&&s[i-1]=='a')
		{
			s.replace(i-1,2,"@");
			break;
		}
	for (i=3;i<s.size()-1;i++)
		if (s[i]=='t'&&s[i-1]=='o'&&s[i-2]=='d')
			s.replace(i-2,3,".");
	cout<<s;
	return 0;
}
