#include <iostream>
#include <algorithm>

using namespace std;

int arr[4];

int main()
{
	int n;
	cin >> n;
	int inp;
	for(int i=0; i<n; i++)
	{
		cin >> inp;
		arr[inp] ++;
	}
	cout << n - *max_element(arr, arr+4) << endl;
	return 0;
}
