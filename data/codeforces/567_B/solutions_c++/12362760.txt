#include<bits/stdc++.h>

using namespace std;

char a[10];
int ch[1000006];
int main(){
	int n,tp,min=0,size=0;
	cin >> n;
	for(int i=0;i<n;i++){
		scanf("%s %d",a,&tp);
		if(a[0]=='+'){	
			size++;
			ch[tp]=1;
		}
		else if(a[0]=='-'){
			if(ch[tp])
				size--;
			else{
				min++;
				ch[tp]=1;
			}

		}
		if(size>min)
			min=size;
	}
	cout << min << endl;
	return 0;
}

