#include<cstdio>
char s[500005];
int i,j,n,k,A,d;
int main(){
    scanf("%d%d%s",&n,&k,s);
    if(k==2){
        for(i=0;i<n;i++)
            if(s[i]=='A'+(i&1))d++;
        A=n-d<d?n-d:d;
        for(i=0;i<n;i++)
            s[i]='A'+(((d==A)+i)&1);
    }
    else
        for(i=0;i<n;i++)
            if(s[i]==s[i+1])
            {
                A++;
                char c='A';
                while(c==s[i]||c==s[i+2])
                    c++;
                s[i+1]=c;
            }
    printf("%d\n%s",A,s);
}