#include <iostream>
#include <cmath>
using namespace std;

int main(){
	int n,sum,x,d,c=0;
	while (true){
		c++;
		cin >> n;
		if(n==0)
			break;
		int a[n];
		sum=0;
		d=0;
		for(int i=0;i<n;i++){
			cin >> a[i];
			sum+=a[i];
		}
		x=sum/n;
		for(int i=0;i<n;i++){
			d+=abs(x-a[i]);
		}
		cout << "Set #"<< c << endl;
		cout << "The minimum number of moves is " << d/2 << "." <<endl;
	}
}
