#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;

	while(t--)
		{
			int n, sum = 0;
			cin>>n;
			char national[50];
			cin>>national;

			for(int i = 0; i < n; i++)
				{
					char arr[50];
					cin>>arr;
					if(strcmp(arr, "CONTEST_WON") == 0)
					{
						int no;
						cin>>no;
						if(no > 20)
							sum += 300;
						else
							sum += 300 + (20 - no);
					}
					else if(strcmp(arr, "TOP_CONTRIBUTOR") == 0)
					{
						sum += 300;
					}
					else if(strcmp(arr, "BUG_FOUND") == 0)
					{
						int no;
						cin>>no;
						sum += no;
					}
					else if(strcmp(arr, "CONTEST_HOSTED") == 0)
					{
						sum += 50;
					}
				}	
			

			if(strcmp(national, "INDIAN") == 0)				
			{
				cout<<sum/ 200;
			}
			else
			{cout<<sum/ 400;}				
			cout<<endl;

		}
	return 0;		
}
