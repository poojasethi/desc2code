#include<iostream>
#include<string>
#include<cstdio>
#include<vector>
using namespace std;
const long long BASE=1000000;
const int BASE_pow=6;
int int_len(long long x)
{
    int count=0;
    do
    {
        x/=10;
        count++;
    }while(x!=0);
    return count;
}
void show(long long *N,int size)
{
    int i;
    for(i=size-1;N[i]<=0 && i>0;i--);
    int start=i;
    for(;i>=0;i--)
    {
        int len=int_len(N[i]);
        for(int j=0;j<BASE_pow-len && i!=start;j++)
        printf("0");
        printf("%lld",N[i]);
    }
    printf("\n");
}
void multiply_nor(long long *N1,long long *N2,int size1,int size2,int size,long long *N3)
{
    for(int i=0;i<size2;i++)
    {
        int k=0,carry2=0;
        long long x=N2[i];
        long long carry=0;
        for(int j=0;j<size1;j++)
        {
            long long y=N1[j];
//            long long z=x*y+carry;
//            carry=z/BASE;
//
//                N3[k+i]+=z%BASE+carry2;
//                carry2=N3[k+i]/BASE;
//                N3[k+i]%=BASE;
            N3[k+i]+=x*y;
            k++;
        }
//        while(carry>0)
//        {
//                N3[k+i]+=carry%BASE+carry2;
//                carry2=N3[k+i]/BASE;
//                N3[k+i]%=BASE;
//            k++;
//            carry/=BASE;
//        }

//        while(carry2>0)
//        {
//            N3[k+i]=carry2%BASE;
//            carry2/=BASE;
//        }
    }
}
void docarry(long long *N,int size)
{
    int carry=0;
    int j,i;
    for(j=size-1;N[j]<=0 && j>0;j--);
    for(i=0;i<=j;i++)
    {
        N[i]+=carry;
        carry=N[i]/BASE;
        N[i]%=BASE;
    }
    while(carry>0)
    {
        N[i]=carry%BASE;
        carry/=BASE;
        i++;
    }
}
int main()
{
    int t;
    scanf("%d",&t);
    long long N1[10000],N2[10000],N3[10000];
    while(t--)
    {
        bool sign1=false,sign2=false;
        int size1=0,size2=0,size3=0;
        string tmp;
        cin>>tmp;
        if(tmp[0]=='-')
        {
            sign1=true;
            tmp.erase(0,1);
        }
        size1=(tmp.length()-1)/BASE_pow + 1;
        for(int i=0;i<size1;i++)
        N1[i]=0;
        for(int i=0;i<tmp.length();i++)
        {
            N1[((tmp.length()-1-i)/BASE_pow)]=N1[(tmp.length()-1-i)/BASE_pow]*10+tmp[i]-'0';
        }

        cin>>tmp;
        if(tmp[0]=='-')
        {
            sign2=true;
            tmp.erase(0,1);
        }
        size2=(tmp.length()-1)/BASE_pow + 1;
        for(int i=0;i<size2;i++)
        N2[i]=0;
        for(int i=0;i<tmp.length();i++)
        {
            N2[((tmp.length()-1-i)/BASE_pow)]=N2[(tmp.length()-1-i)/BASE_pow]*10+tmp[i]-'0';
        }

        int size=size1>size2?size1:size2;
        for(int i=0;i<size1+size2;i++)
        N3[i]=0;
        if(sign1^sign2)
        cout<<'-';
        multiply_nor(N1,N2,size1,size2,size,N3);
        docarry(N3,size1+size2);
        show(N3, size1+size2);

    }
    return 0;
}
