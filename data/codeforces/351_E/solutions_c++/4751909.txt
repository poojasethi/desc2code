#include <cstdio>
#include <algorithm>

#define N 3000

using namespace std;

int arr[N];

int main() {
	int n;
	scanf("%d",&n);
	for(int i=0; i<n; i++) {
		scanf("%d",&arr[i]);
		arr[i]=abs(arr[i]);
	}
	int ret=0;
	for(int i=0; i<n; i++) {
		int x=0,y=0;
		for(int j=i+1; j<n; j++) {
			if(arr[j]<arr[i]) {
				x++;
			}
		}
		for(int j=0; j<i; j++) {
			if(arr[j]<arr[i]) {
				y++;
			}
		}
		ret+=min(x,y);
	}
	printf("%d\n",ret);
	return 0;
}
