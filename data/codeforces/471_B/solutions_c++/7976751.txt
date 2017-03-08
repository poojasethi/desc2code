#include <cstdio>
#include<algorithm>
#include <vector>

using namespace std;
struct tuple
{
	int first,second;
};

int main()
{
	int n,i,tmp;
	scanf("%d",&n);
	pair<int,int> arr[n];
	for(i=0;i<n;i++)
	{
		scanf("%d",&tmp);
		arr[i].first=tmp;
		arr[i].second=i+1;
	}

	sort(arr,arr+n);
	vector<int> mm;
	for(i=0;i<n-1 && mm.size()<2;i++)
	{
		if(arr[i].first==arr[i+1].first)
			mm.push_back(i);
	}

	if(mm.size()<2)
		printf("NO\n");
	else
	{
		printf("YES\n");
		for(i=0;i<n;i++)
			printf("%d ",arr[i].second);
		printf("\n");
		swap(arr[mm[0]],arr[mm[0]+1]);

		for(i=0;i<n;i++)
			printf("%d ",arr[i].second);
		printf("\n");

		swap(arr[mm[1]],arr[mm[1]+1]);
		for(i=0;i<n;i++)
			printf("%d ",arr[i].second);
		printf("\n");
	}
	return 0;
}
