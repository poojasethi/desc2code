#include<iostream>
#include<string>
#include<vector>
using namespace std;
bool p[100000];
vector<int> next[100000][5];
void preprocess()
{
  for (int i = 2; i*i < 100000; i++) if (!p[i]) {
      for (int j = i*i; j < 100000; j += i) p[j] = 1;
    }
  for (int i = 2; i < 100000; i++) if (!p[i]) {
      for (int k = i, j = 1; j < 5; j++) next[k/=10][j].push_back(i);
    }
}
string fr;
int n;
char safe[6][6];
int solve(int r)
{
  int x = 0;
  for (int i = 1; i < r; i++) x = 10*x + safe[r][i]-'0';

  if (r == n) return next[x][1].size();

  int ret = 0;
  for (int i = 0; i < next[x][n-r+1].size(); i++) {
    int y = next[x][n-r+1][i];
    for (int j = n; j >= 1; j--) {
      safe[r][j] = safe[j][r] = y%10 + '0';
      y /= 10;
    }
    ret += solve(r+1);
  }
  return ret;
}
int main()
{
  preprocess();
  int t; cin>>t;
  while (t--) {
    cin>>fr; n = fr.size();

    for (int i = 1; i <= n; i++)
      safe[1][i] = safe[i][1] = fr[i-1];
    cout<<solve(2)<<endl;
  }
  return 0;
}
