#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>
#include <math.h>
using namespace std;

const long long V=1LL<<48;

bool myfunction (int i, int j) {
  return (i==j);
}

void removeDuplicates(vector<int> &a);
long long getValue(vector<int> a);

int main()
{
	int t,k,ni,i,j;
	long long gameV;
	cin>>t;
	while(t--)
	{
		gameV=0;
		scanf("%d",&k);//cin>>k;
		for(i=0;i<k;i++)
		{
			scanf("%d",&ni);//cin>>ni;
			vector <int> a;
			int temp;
			for(j=0;j<ni;j++)
			{
				scanf("%d",&temp);//cin>>temp;
				a.push_back(temp);
			}
			sort(a.begin(),a.end());
			unique(a.begin(), a.end(), myfunction);
			gameV+=getValue(a);
			//a.erase(a.begin(),a.end());
		}
		if(gameV > 0)
		{
			printf("%s\n","EVEN");//cout<<"EVEN"<<endl;
		}
		else if(gameV < 0)
		{
			printf("%s\n","ODD");//cout<<"ODD"<<endl;
		}
		else if(gameV==0)
		{
			printf("%s\n","DON'T PLAY");//cout<<"DON'T PLAY"<<endl;
		}
	}
return 0;
}

long long getValue(vector<int> a)
{
	bool flipped=false;
	long long ret=0,tempV=0,add=V;
	int siz=a.size(),i,power=1;
	if(a[0]%2==0)
	{
		tempV+=add;
	}
	else if(a[0]%2==1)
	{
		tempV-=add;
	}
	for(i=1;i<siz;i++)
	{
		if(flipped==false)
		{
			if(((a[i]%2==0)&&(a[i-1]%2==1))||((a[i]%2==1)&&(a[i-1]%2==0)))
			{
				flipped=true;
				if(a[i]%2==0)
				{
					add=V>>power;
					tempV+=add;
					power++;
				}
				else if(a[i]%2==1)
				{
					add=V>>power;
					tempV-=add;
					power++;
				}
				continue;
			}
			if(a[i]%2==0)
			{
				tempV+=add;
			}
			else if(a[i]%2==1)
			{
				tempV-=add;
			}
		}
		else if(flipped==true)
		{
			if(a[i]%2==0)
			{
				add=V>>power;
				tempV+=add;
				power++;
			}
			else if(a[i]%2==1)
			{
				add=V>>power;
				tempV-=add;
				power++;
			}
		}
	}
	ret=tempV;
	return ret;
}
