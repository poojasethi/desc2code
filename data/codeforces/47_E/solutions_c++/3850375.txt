#include <stdio.h>
#include <algorithm>
using namespace std;
#include <math.h>
double al[100000];
double X[100000];
double Y[100000];
int d[100000];
bool cmp(int x,int y){return(al[x]<al[y]);};
pair<double,double> W[100000];
int main(){
    int n,v;
    scanf("%d%d",&n,&v);
    for (int i=0;i<n;i++)
        scanf("%lf",&al[i]),d[i]=i;
    int m;
    scanf("%d",&m);
    for (int i=0;i<m;i++){
        int x,y;
        scanf("%lf%lf",&W[i].first,&W[i].second);
    }
    sort(W,W+m);
    sort(d,d+n,cmp);
    int j=0;
    for (int k=0;k<n;k++){
        int i=d[k];
        double alpha=al[i];
       double x=v*v/9.8*sin(2*alpha);
        bool r=false;
        while (j<m&&W[j].first<x){
            double t=W[j].first/(v*cos(alpha));
            double h=v*sin(alpha)*t-9.8*t*t/2;
            if (h<=W[j].second){
                X[i]=W[j].first;
                Y[i]=h;
                r=true;
                break;
            }
            j++;
        }
        if (!r)
            X[i]=x, Y[i]=0;
    }
    for (int i=0;i<n;i++)
        printf("%lf %lf\n",X[i],Y[i]);
}