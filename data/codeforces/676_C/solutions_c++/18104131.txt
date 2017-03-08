#include <iostream>
#include <algorithm>
using namespace std;
string arr;
int n,k;
int run(char c)
{
	int ans = 0,l = 0,r = -1,cnt = 0;
	while(l < n)
	{
		while(r < n && cnt <= k)
		{
			if(arr[r+1] == c)
				r++;
			else
			{
				cnt++;
				r++;
			}
		}
		ans = max(ans,r-l);
		if(arr[l] != c)
			cnt--;
		l++;
	}
	return ans;
}
int main()
{
	cin>>n>>k>>arr;
	cout<<max(run('a'),run('b'));
	return 0;
} 

