#include <bits/stdc++.h>
using namespace std ;
int main()
{
	string s,temp ;
	cin >> s ;
	int n,count1=0,count2=0,ans=0 ;
	cin >> n ;
	for(int i=0;i<n;i++)
	{
		cin >> temp ;
		for(long long int j=0;s[j];j++)
		{
			if(s[j]==temp[0])
			{
				count1++ ;
			}
			else if(s[j]==temp[1])
			{
				count2++ ;
			}
			else
			{
				ans = ans+min(count1,count2) ;
				count2 =0 ;
				count1 =0 ;
			}
		}
	}
	ans+=min(count2,count1) ;
	cout << ans << "\n" ;
	return 0 ;
}