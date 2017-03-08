#include <iostream>

using namespace std;

#define M 1000000007

long long int a[1001][1001];

void calc(){
  int n,m,i,j;
  n = 1000;
  m = 1000;
  for(i=1;i<=n;i++){
    a[i][1] = 1;
    a[i][i] = 1;
  }
  for(i=1;i<=n;i++){
    for(j=2;j<=m;j++){
      if(j>i)
	a[i][j] = 0;
      else if(j < i){
	a[i][j] = (j*a[i-1][j] + a[i-1][j-1]);
	if(a[i][j] >= M)
	  a[i][j] = a[i][j]%M;	 
      }
    }
  }
}

void print(){
  int i,j;
  for(i=1;i<=1000;i++){
    for(j=1;j<=1000;j++){
      if(a[i][j] < 0)
	cout << "err ";
    }
  }
}

int main(){
  int t,n,i;
  calc();
  print();
  //  cout << a[1000][1000] << endl;
  cin >> t;
  while(t--){
    cin >> n;
    long long int ans = 0;
    for(i=1;i<=n;i++)
      ans = (ans + a[n][i])%M;
    ans = ans%M;
    cout << ans << endl;
  }  
  return 0;
}
