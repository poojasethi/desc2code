#include<bits/stdc++.h>
using namespace std;
int main()
{
	string s1,s2,s3;
	cin>>s1>>s2>>s3;
	reverse(s3.begin(),s3.end());
	if(s1==s3&&s2[0]==s2[2])
		puts("YES");
	else
		puts("NO");
	return 0;
}
