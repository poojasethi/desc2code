#include<cstdio>
#include<cstring>
using namespace std;

#define MAX 110

int m[MAX][MAX];

int main()
{
	int n, x;

	scanf("%d", &n);
	for(int i=0; i<n; ++i)
	{
		scanf("%d", &m[i][0]);
		for(int j=0; j<m[i][0]; ++j) scanf("%d", &x), m[i][x] = 1;
	}
	
	for(int i=0; i<n; ++i)
	{
		bool can = 1;
		for(int j=0; j<n && can; ++j)
			if(i != j)
			{
				int count = 0;
				for(int k=1; k<=100; ++k)
					if(m[i][k] && m[j][k])
						++count;
				if(count == m[j][0]) can = 0;
			}
		can ? puts("YES") : puts("NO");
	}

	return 0;
}
