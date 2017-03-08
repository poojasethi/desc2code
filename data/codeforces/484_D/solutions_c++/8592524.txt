#include <iostream>
using namespace std;

long long cur,curm,curM;
int n;

int main()
{
	long long x;
	cin >> n;
	for(int i=0;i<n;i++)
	{
		cin >> x;
		if(i==0 || cur-x>curm)
			curm = cur-x;
		if(i==0 || cur+x>curM)
			curM = cur+x;
		cur = max(cur, curM-x);
		cur = max(cur, curm+x);
	}
	cout << cur << endl;
	
	return 0;
}

