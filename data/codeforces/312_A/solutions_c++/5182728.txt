#include <iostream>
#include <string>
using namespace std;
int n,i,z,zz;
string s;
main()
{
    cin>>n;
    getline(cin,s);
    for (i=1; i<=n; i++)
    {
        z=0; zz=0;
        getline(cin,s);
        if (s.rfind("lala.")==s.size()-5) z++;
        if (s.find("miao.")==0) zz++;
        if (z==1 && zz==0) cout<<"Freda's"<<endl; else
        if (z==0 && zz==1) cout<<"Rainbow's"<<endl;  else
        cout<<"OMG>.< I don't know!"<<endl;
    }
}
