#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

char M[505][505];
int vist[505][505];
int n, m, res = 0;
stringstream ss;

void dfs(int i, int j, bool primer = true) {
  if (i < 0 or i >= n or j < 0 or j >= m or M[i][j] == '#' or vist[i][j]) return;
  
  vist[i][j] = true;
  ++res;
  ss << "B " << i + 1 << " " << j + 1 << endl;
  dfs(i + 1, j, false);
  dfs(i - 1, j, false);
  dfs(i, j + 1, false);
  dfs(i, j - 1, false);
  if (not primer) {
    res += 2;
    ss << "D " << i + 1 << " " << j + 1 << endl;
    ss << "R " << i + 1 << " " << j + 1 << endl;
  }
}

int main() {
  cin >> n >> m;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      cin >> M[i][j];      
    }
  }
  
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      if (not vist[i][j]) {
        dfs(i, j);        
      }
    }
  }
  
  cout << res << endl;
  string s;
  while (getline(ss, s)) {
    cout << s << endl;
  }
}