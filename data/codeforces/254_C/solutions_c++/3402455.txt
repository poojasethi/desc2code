#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;

string s,t;
int s_arr[256] = {0};
int t_arr[256] = {0};

ifstream in("input.txt");
ofstream out("output.txt");

int main(){
  in >> s >> t;
  for(int i=0; i<s.length(); i++){
    s_arr[s[i]]++;
    t_arr[t[i]]++;
  }

  int op = 0;
  for(int i=0; i<s.length(); i++){
    if(s_arr[s[i]] > t_arr[s[i]]){
      for(int j = 'A'; j<='Z'; j++){
	if(s_arr[j] < t_arr[j]){
	  if(j < s[i] || t_arr[s[i]] == 0){
	    s_arr[s[i]]--;
	    s[i] = j;
	    s_arr[j]++;
	    op++;
	    break;
	  }
	  else{
	    t_arr[s[i]]--;
	    s_arr[s[i]]--;
	    break;
	  }
	}
      }
    }
  }
  out << op << endl << s << endl;
  return 0;
}
