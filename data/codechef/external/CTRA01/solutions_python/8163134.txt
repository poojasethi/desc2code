#include <iostream>
using namespace std;
int c[8],b[8][8];
void populate(int i1, int j1){
    int i=i1;
    int j=j1;
    for(;i<8 && j<8;i++,j++)
        b[i][j]=1;
    i=i1;
    j=j1;
    for(;i<8 && j>=00;i++,j--)
        b[i][j]=1;
    i=i1;
    j=j1;
    for(;i>=0 && j<8;i--,j++)
        b[i][j]=1;
    i=i1;
    j=j1;
    for(;i>=0 && j>=0;i--,j--)
        b[i][j]=1;

    i=i1;
    for(j=0;j<8;j++)
        b[i][j]=1;
    j=j1;
    for(i=0;i<8;i++)
        b[i][j]=1;
}
int main(){
long long test;
int check=0;
cin>>test;

for(int i=0; i<8; i++)
    for(int j=0; j<8; j++)
        b[i][j]=0;
while(test--){
    for(int i=0; i<8; i++)
    for(int j=0; j<8; j++)
        b[i][j]=0;
        check=0;
    for(int i=0; i<8; i++)
    {
        cin>>c[i];
        if(b[c[i]-1][i]==1)
            check=1;
        populate(c[i]-1,i);


        //cout<<endl<<check<<endl;
    }
    if(check==1)
        cout<<"No"<<endl;
    else
        cout<<"Yes"<<endl;

}
return 0;
}
