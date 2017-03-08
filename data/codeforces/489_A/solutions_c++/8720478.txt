#include <iostream>

using namespace std;

int main(){
	int  n;
	cin>>n;
	int a[n];
	for (int i = 0; i < n; i++){
		cin>>a[i];
	}

	int k = 0;
	cout<<n<<endl;
	for (int j = n-1; j >= 0; j--){
		k = 0;
		for (int i = 0; i <= j; i++){
			if (a[i] > a[k])
				k = i;
		}
		cout<<k<<" "<<j<<endl;
		swap(a[k], a[j]);
	}


	return 0;
}