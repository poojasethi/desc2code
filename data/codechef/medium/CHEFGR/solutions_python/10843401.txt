#include <iostream>
using namespace std;

int main() {
	int t,N,M;
	cin>>t;
	while(t--){
	    cin>>N>>M;
	    int arr[N],max=0,c=0;
	    for(int i=0;i<N;i++){
	        cin>>arr[i];
	        if(arr[i]>max)
	            max=arr[i];
	    }
	    
	    for(int i=0;i<N;i++){
	        if(arr[i]==max) 
	            continue;
	        c+=max-arr[i];
	    }
	    if(c==M)
    	    cout<<"Yes"<<endl;
	    else if((M-c)%N==0)
	        cout<<"Yes"<<endl;
	    else
	        cout<<"No"<<endl;
	}
	return 0;
}
