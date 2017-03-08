#include <string>
#include <iostream>
#include <vector>
using namespace std;
int main(){
	int n;
	cin>>n;
	vector<string> name(n);
	vector<int> a(n);
	vector<int> h(n,1);
	for(int i=0;i<n;i++)
		cin>>name[i]>>a[i];
	for(int i=0;i<n;i++)
		for(int j=0;j<n-1;j++)
			if(a[j]>a[j+1])
				swap(a[j],a[j+1]),swap(name[j],name[j+1]);
	for(int i=0;i<n;i++)
		if(i<a[i]){
			cout<<-1<<endl;
			return 0;
		}
	vector<int> vi;
	vector<string> vs;
	for(int i=0;i<n;i++){
		vi.insert(vi.begin()+a[i],n-i);
		vs.insert(vs.begin()+a[i],name[i]);
	}
	for(int i=0;i<n;i++)
		cout<<vs[i]<<" "<<vi[i]<<endl;
	return 0;
}

