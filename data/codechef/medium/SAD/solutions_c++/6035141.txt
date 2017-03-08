#include<iostream>
#include<cstdio>
#include<climits>
using namespace std;

int main(){
    int r,c;
    int **a;
    scanf("%d %d",&r,&c);
    a = new int *[r];
    for(int i=0;i<r;i++){
        a[i] = new int[c];
    }
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            scanf("%d",&a[i][j]);
        }
    }
    int minr[r];
    int maxc[c];
    for(int i=0;i<r;i++){
        minr[i]=INT_MAX;
    }
    for(int i=0;i<c;i++){
        maxc[i]=INT_MIN;
    }
    for(int i=0;i<r;i++){
        minr[i] = INT_MAX;
        for(int j=0;j<c;j++){
            if(minr[i]>a[i][j]){
                minr[i]=a[i][j];
            }
        }
    }
    for(int j=0;j<c;j++){
        maxc[j]=INT_MIN;
        for(int i=0;i<r;i++){
            if(maxc[j]<a[i][j]){
                maxc[j]=a[i][j];
            }
        }
    }
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            if(minr[i]==a[i][j] && maxc[j]==a[i][j]){
                printf("%d",a[i][j]);
                return 0;
            }
        }
    }
    printf("GUESS");
    return 0;
}
