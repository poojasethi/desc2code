#include<iostream>
using namespace std;
string T[5]={"S","M","L","XL","XXL"};

int main(){
	int M[5];
	int k;
	string s;

	for(int i = 0; i < 5; i++) cin>>M[i];
	cin>>k;
	
	for(int i = 0; i < k; i++){
		cin>>s;
		int ind;
		for(int j = 0;j < 5; j++){
			if(T[j] == s){
				ind = j;
				break;
			}
		}
		
		int j = 0;
		while(1){
			if( (ind + j < 5) && (M[ind + j] > 0)){
				ind += j;
				break;
			}
			if( (ind - j >= 0) && (M[ind - j] > 0)){
				ind -= j;
				break;
			}
			j++;
		}
		
		cout<<T[ind]<<endl;
		M[ind]--;
	}
	return 0;
}