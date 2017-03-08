#include <stdio.h>
#include <memory.h>
int a[200][200];
int main(){
    int n,m;
    scanf("%d%d",&n,&m);
    if (n*m==1){
        printf("1");
        return 0;
    }
    
    if (n*m<=3||(n==2&&m==2)){
        printf("-1");
        return 0;
    }
    
    for (int i=0;i<n;i++)
        for (int j=0;j<m;j++)
            if ((i+j)%2==0){
                a[i][j]=(n*m/2)+(i*m+j)/2+1;
            }else
                 a[i][j]=(i*m+j)/2+1;
        
    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++)
            printf("%d ",a[i][j]);
        printf("\n");
    }
                   
}