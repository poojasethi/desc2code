#include <bits/stdc++.h>

using namespace std;

vector<int> vec;



int get_res(vector<int> vec, int n)
{
	if(n<0)return vec[vec.size()-1]&vec[vec.size()-2];
	vector<int> next;
	int temp;
	for(int i=0;i<vec.size();i++)
	{
		temp=vec[i]>>n;
		if(temp&0x1==1)next.push_back(vec[i]);
	}
	if(next.size()>1)return get_res(next,n-1);
	else return get_res(vec,n-1);
}

int main()
{
	int n;
	cin>>n;
	vec.resize(n);
	for(int i=0;i<n;i++)
	{
		cin>>vec[i];
	}
	sort(vec.begin(),vec.end());
	cout<<get_res(vec,31)<<endl;

}