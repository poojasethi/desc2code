#include <iostream>
#include <vector>

using namespace std;

const int maxN = 100000;
const int MOD = 1000000007;

vector<int> p(maxN+1);
vector<int> mark(maxN+1);


int main()
{
	int T;
	cin >> T;

	for(;T--;)
	{
		int N;
		cin >> N;
		int j = 0;
		for (int i = 2; i <= N; i+=2)
			p[++j] = i;
		for (int i = 1; i <= N; i+=2)
			p[++j] = i;
		for (int i = 1; i <= N; i++)
			mark[i]=0;

		int count = 0;
		for (int i = 1; i <= N ; ++i)
		{
			if(!mark[i])
			{
				count++;
				for (int j = i; !mark[j] ; j=p[j])
					mark[j] = 1; 
			}
		}
		unsigned long long ans = 1;
		while(count--)
			ans = (ans*26)%MOD;
		cout << ans << "\n";
	}
	return 0;
}