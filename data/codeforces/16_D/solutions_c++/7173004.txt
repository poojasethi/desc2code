#include <bits/stdc++.h>
using namespace std;

int main(){
  int test, minuts = 0, ant = 0,cont = 1,h,m, p,recont = 0;
  scanf("%i\n", &test);
  string in;
  char a;

  while(test--){
    getline(cin,in);
    stringstream ss;
    ss<<in; ss.get();
    ss>>h; ss.get();
    ss>>m; ss.get();
    a = ss.get();
    minuts =  h*60 + m;
    if(a == 'p' and h < 12) minuts+= 12*60;
    if(a == 'a' and h == 12) minuts -= 12*60;
    if(minuts < ant) cont++;
    if(minuts == ant) recont++;
    else {
      cont+= recont/10;
      recont = 0;
    } 
    ant = minuts;
  }
  cont+= recont/10;
  cout<<cont<<endl;
  return 0;
}