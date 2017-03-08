// Program question at: http://www.codechef.com/DMNT2012/problems/SPRLNMS
#include <cstdio>
using namespace std;

int main()
{
	int t; scanf("%d",&t);
	while(t--)
	{
		int n; scanf("%d",&n);
		printf("%d\n", n*( (n<<2)-3) );
	}
	return 0;
}
