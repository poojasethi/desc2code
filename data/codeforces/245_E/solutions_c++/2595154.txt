#include <iostream>
using namespace std;

int main()
{
	int max = 0, min = 0;
	int cu = 0;
	char c;
	while(cin >> c)
	{
		if(c=='+')
			cu ++;
		else if(c=='-') cu--;
		max = max > cu ? max : cu;
		min = min < cu ? min : cu;
	}
	min = -min;
	cout << max+min << endl;
}