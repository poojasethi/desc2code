#include<bits/stdc++.h>

using namespace std;

string s;

int main(){

	int t;

	cin>>t;
	int i,j,k,l;

	while(t--){

		cin>>s;

		int a[20];

		for(i=0;i<20;i++){
			a[i]=0;
		}

		int net=0;

		for(i=1;i<=12;i++){
			if(12%i!=0)continue;
		
			l=12/i;


			for(j=0;j<12;j+=1){
				int t=0;
				for(k=j;k<12;k+=l){
					if(s[k]=='X'){
						t++;
					}
				}
				if(t==i){
					net++;
					a[i]=1;
					break;
				}

			}
		}

		cout<<net<<" ";

		for(i=1;i<=12;i++){
			if(a[i]==1){
				cout<<(i)<<"x"<<(12/i)<<" ";
			}
		}cout<<endl;
	
	}

	return 0;
}