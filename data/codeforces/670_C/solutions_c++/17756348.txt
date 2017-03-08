#include <iostream>
#include <map>

using namespace std;

map<int, int> tot;

const int maxn=200000;
int n,m,maxi;
int b[maxn+5],c[maxn+5];

int main(){
  cin >> n;
  int te_a;
  while (n--){
    cin >> te_a;
    tot[te_a]++;
  }
  cin >> m;
  for (int i=0;i<m;i++) cin >> b[i];
  for (int i=0;i<m;i++) cin >> c[i];
  int maxi = 0;
  int max_p = tot[b[0]];
  int max_s = tot[c[0]];
  for (int i=1;i<m;i++){
    if (tot[b[i]]>tot[b[maxi]]) maxi=i;
    else if (tot[b[i]]==tot[b[maxi]] && tot[c[i]]>tot[c[maxi]]) maxi=i;
  }
  cout << maxi+1;
  return 0;
}

