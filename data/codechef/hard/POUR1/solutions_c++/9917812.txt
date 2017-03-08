#include<cstdio>
#include<algorithm>
using namespace std;
int pour(int A,int B,int C){
int move=1,a=A,b=0,tfr;
while(a!=C && b!=C){
           tfr=min(a,B-b);
           b+=tfr;
           a-=tfr;
           move++;
           if(a==C || b==C)
                   break;
           if(a==0){
                    a=A;
                    move++;
           }
           if(b==B){
                b=0;
                move++;
           }
     }
     return move;
}
int gcd(int a,int b){
    if(b==0)
        return a;
    return gcd(b,a%b);
}
int main(){
int t,a,b,c;
scanf("%d",&t);
while(t--){
           scanf("%d%d%d",&a,&b,&c);
           if(c>a && c>b)
                  printf("-1\n");
           else if(c%gcd(a,b) != 0)
                printf("-1\n");
           else if(c==a || c==b)
                printf("1\n");
           else
               printf("%d\n",min(pour(a,b,c),pour(b,a,c)));
}
return 0;
}