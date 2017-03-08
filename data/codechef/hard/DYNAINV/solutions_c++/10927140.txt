#include <bits/stdc++.h>

using namespace std;


vector<int> mysort(vector<int> vec,int &inver)
{
	if(vec.size()<=1)
	{
		inver=0;
		return vec;
	}
	int mid=vec.size()/2;
	vector<int> left,right;
	for(int i=0;i<mid;i++)
	{
		left.push_back(vec[i]);
	}
	for(int i=mid;i<vec.size();i++)
	{
		right.push_back(vec[i]);
	}
	int left_inver=0,right_inver=0;
	left=mysort(left,left_inver);
	right=mysort(right,right_inver);
	int x=0,y=0,ans=0;
	for(int i=0;i<vec.size();i++)
	{
		if(x<left.size()&&y<right.size())
		{
			if(left[x]<=right[y])
			{
				vec[i]=left[x];
				x++;
			}
			else
			{
				vec[i]=right[y];
				ans+=(left.size()-x);
				y++;
			}
		}
		else if(x<left.size())
		{
			vec[i]=left[x];
			x++;
		}
		else
		{
			vec[i]=right[y];
			ans+=(left.size()-x);
			y++;
		}
	}
	inver=ans;
	inver+=left_inver;
	inver+=right_inver;
	return vec;
}

int main()
{
	int n,m,x,y;
	cin>>n>>m;
	vector<int> vec;
	vec.resize(n);
	for(int i=0;i<n;i++)
	{
		cin>>vec[i];
	}
	int inversions=0;
	vector<int> ans;
	ans=mysort(vec,inversions);
	inversions%=2;
	for(int i=0;i<m;i++)
	{
		cin>>x>>y;
		if(x!=y){inversions=(inversions+1)%2;}
		cout<<inversions<<endl;
	}
}