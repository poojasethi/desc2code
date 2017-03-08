#include <iostream>
#include <stdio.h>
#include <string.h>
#include <set>

using namespace std;

set<int> S;
set<int>::iterator it,pt;
pair<set<int>::iterator,bool> ret;
char in[300005]={0};
int chk[30]={0};
long long num[30]={0};
int main()
{
    int n,id;
    scanf("%s",in+1);
    n=strlen(in+1);
    S.insert(n+1);
    for(int i=n;i>0;i--)
    {
        id=in[i]-'a';
        if(chk[id]!=0) S.erase(chk[id]);
        ret=S.insert(i);
        chk[id]=i;
        pt=ret.first;
        it=pt;it++;
        for(int j=1;it!=S.end();it++,pt++,j++)
        {
            num[j]+=(*it)-(*pt);
        }
    }
    cout << S.size()-1 << endl;
    for(int i=1;i<S.size();i++) cout << num[i] << endl;
    return 0;
}
