#include <stdio.h>
#include <set>
using namespace std;
int main()
{
	int n,l,x,y,i,d,idx=0;
	set<int> s;
	set<int>::iterator it;
	bool bx=false,by=false;
	scanf("%d%d%d%d",&n,&l,&x,&y);
	for (i=1;i<=n;i++)
	{
		scanf("%d",&d);
		s.insert(d);
	}
	for (it=s.begin(),i=1;it!=s.end();it++,i++)
	{
		if (s.count(*it-x))
			bx=true;
		if (s.count(*it-y))
			by=true;
		if (s.count(*it-x-y))
			idx=*it-x;
		if (*it+x<=l&&s.count(*it+x-y))
			idx=*it+x;
		if (*it+y<=l&&s.count(*it-x+y))
			idx=*it+y;
		if (*it-y>=0&&s.count(*it+x-y))
			idx=*it-y;
		if (*it-x>=0&&s.count(*it-x+y))
			idx=*it-x;
	}
	if (bx&&by)
		printf("0");
	else if (!bx&&by)
		printf("1\n%d",x);
	else if (!by&&bx)
		printf("1\n%d",y);
	else
	{
		if (idx)
			printf("1\n%d",idx);
		else
			printf("2\n%d %d",x,y);
	}
	return 0;
}
