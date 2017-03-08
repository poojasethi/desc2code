#include <bits/stdc++.h>
using namespace std;

int main(){
  int state = -1;
  bool coma = false ;
  string in, out;
  char act;
  getline(cin,in);
  act = in[0];
  for(int i = 0; i < in.size(); i++){    
    if(in[i] == '@' and (state > 0 or i == 0)) {
      puts("No solution");
      return 0;
    }
    else  if(in[i] == '@' and state <= 0) state = 1;

    if(i+1 < in.size()) if(in[i+1] == '@' and state == 2)  {
      out+= ',';
      state = 0;
    }
    if(state == 1 and in[i]!= '@') state = 2; 
    out += in[i];
  } 
  if(state != 2 ) puts("No solution");
  else cout<<out<<'\n';
  return 0;
}