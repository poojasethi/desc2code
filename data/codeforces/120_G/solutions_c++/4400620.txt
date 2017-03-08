//                  be naame khoda

#include <fstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <queue>
#include <vector>
#include <string>

using namespace std;


#define cout fout
#define cin fin
ifstream fin("input.txt");
ofstream fout("output.txt");


int n, t, a[200][5], b[200][5], m, c[500], now, d[500][500], flag = 1, i, nowt;
string s[500];
vector <int> ans[500];
queue <int> Q;

int main()
{
    cin >> n >> t;
    for(int i = 0; i < n; i++)
        cin >> a[i][1] >> b[i][1] >> a[i][2] >> b[i][2];
    cin >> m;
    for(int i = 0; i < m; i++)
    {
        cin >> s[i] >> c[i];
        Q.push(i);
    }
    nowt = t;
    while(!Q.empty())
    {
        int p, q, T, k, j;
        k = Q.front();
        Q.pop();
        j = i / n % 2;
        q = 1 - j;
        j++;
        q++;
        T = max(1, c[k] - a[i%n][j] - b[i%n][q] - d[i%n][k]);
        if(T <= nowt)
        {
            nowt -= T;
            ans[i%n].push_back(k);
        }
        else
        {
            d[i%n][k] += nowt;
            nowt  = t;
            Q.push(k);
            i++;
        }
        if(!nowt)
        {
            nowt = t;
            i++;
        }
    }
    for(int i = 0; i < n; i++)
    {
        cout << ans[i].size() << endl;
        for(int j = 0; j < ans[i].size(); j++)
            cout << s[ans[i][j]] << endl;
    }
}