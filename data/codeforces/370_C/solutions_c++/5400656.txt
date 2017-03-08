#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int N,M;
	cin >> N >> M;
	int C[5050];
	for(int i=0;i<N;i++) cin >> C[i];
	sort(C,C+N);
	int cnt = 0;
	for(int i=0;i<N;i++) cnt += (C[i] != C[(i+N/2)%N]);
	cout << cnt << endl;
	for(int i=0;i<N;i++) cout << C[i] << ' ' << C[(i+N/2)%N] << endl;
	return 0;
}
