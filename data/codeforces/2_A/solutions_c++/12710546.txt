#include <bits/stdc++.h>

using namespace std;
map<string,int> f,g;
string s[1000];
int c[1000],i, m=0;

int main()
{
int n;
cin >> n;

for(i=0; i<n; i++) 
cin >> s[i] >> c[i], f[s[i]] += c[i];

for(i=0; i<n; i++)
if(m < f[s[i]]) m = f[s[i]];
for(i=0; f[s[i]] < m || (g[s[i]] += c[i]) < m; i++);

cout << s[i];
return 0;

}