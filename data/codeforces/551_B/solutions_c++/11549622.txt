#include <iostream>
#include <string>
using namespace std;

int ca[26], cb[26], cc[26];
int check(int *x, int *y){
	int c = 999999;
	for(int i=0;i<26;i++){
		if (y[i]>0 && x[i]==0) return 0;
		if (y[i]>0){
			int t= x[i]/ y[i];
			c= min(c, t);
		}
	}
	return c;
}
void cut(int *x, int *y){
	for(int i=0;i<26;i++)
		x[i]-= y[i];
}
int main(){
	string a, b, c;
	cin >> a >> b >> c;
	for(int i=0;a[i];i++) 
		ca[a[i]-'a']++;
	for(int i=0;b[i];i++) 
		cb[b[i]-'a']++;
	for(int i=0;c[i];i++) 
		cc[c[i]-'a']++;
	
	string sol = "";
	while (1){
		int t1= check(ca,cb);
		int t2= check(ca,cc);
		if (!t1 && !t2)
			break;
		
		if (t1>t2){
			sol+= b;
			cut(ca, cb);
		}
		else {
			sol+= c;
			cut(ca, cc);
		}
	}
	for(int i=0;i<26;i++)
		while (ca[i]){
			sol+= ('a'+ i);
			ca[i]--;
		}
	cout << sol << endl;
	return 0;
}
