#include <bits/stdc++.h>

#define sf(a) scanf("%d" , &a)

using namespace std;

int main(int argc , char ** argv)
{
	set <int> sums;
	set<int>::iterator it;
	int num;
	cin>>num;
	int *arr = new int[num+1];
	for(int i=0;i<num;i++)
	{
		sf(arr[i]);
	}
	sort(arr , arr + num);
	for (int i = 0; i < num-1; ++i)
	{
		for (int j = i+1; j < num; ++j)
		{
			sums.insert(arr[i]+arr[j]);
		}
	}
	int maxi = 0;

	for (it = sums.begin() ; it != sums.end() ; it++)
	{
		int count = 0;
		int trynum = *it;
		int i = 0;
		int j = num -1;
		while(i < j)
		{
			int presum = arr[i] + arr[j];
			if(presum == trynum)
			{
				//cout <<arr[i]<<" "<<arr[j]<<" "<<trynum<<endl;
				count += 1;
				i++;
				j--;
			}
			else if(presum > trynum)
			{
				j--;
			}
			else
			{
				i++;
			}
		}
		maxi = max(maxi,count);
	}
	cout<<2*maxi<<endl;

	return 0;
}