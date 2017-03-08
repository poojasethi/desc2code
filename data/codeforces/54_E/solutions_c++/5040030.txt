#include<cmath>
#include<cstdio>
#include<algorithm>
using namespace std;
typedef struct point{
    double x,y;
    point(){ x = y = 0.0; }
    point(double _x,double _y){ x = _x; y = _y; }
    void read(){ scanf("%lf%lf",&x,&y); }
}Point;
Point P[200001];
double A[200001];
int n;
double cross(point p1,point p2,point p3){
    return (p2.x-p1.x)*(p3.y-p1.y) - (p2.y-p1.y)*(p3.x-p1.x);
}
double dot(point p1,point p2,point p3){
    return (p2.x-p1.x)*(p3.x-p1.x) + (p2.y-p1.y)*(p3.y-p1.y);
}
double area(point p1,point p2,point p3){
    return abs(p1.x*p2.y+p2.x*p3.y+p3.x*p1.y-p1.y*p2.x-p2.y*p3.x-p3.y*p1.x)*0.5;
}
double dist(point p1,point p2){
    return sqrt((p2.x-p1.x)*(p2.x-p1.x)+(p2.y-p1.y)*(p2.y-p1.y));
}
double findArea(point p1,point p2,point p3){
    double t = dot(p2,p1,p3),d = dist(p1,p2),c = cross(p2,p1,p3);
    return 0.5*abs(t/d*c/d);
}
double qArea(int a,int b){
    //printf("%d %d!!!%lf %lf\n",a,b,area(P[1],P[a],P[b]),A[b-1]-A[a-1]);
    if(a%(n+1) > b%(n+1)) return area(P[1],P[a],P[b])+A[b-1]-A[a-1];
    else return A[b-1]-A[a-1]-area(P[1],P[a],P[b]);
}
int main(){
    double ans = 1e17;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        P[i].read(); P[n+i] = P[i]; 
    }
    for(int rt=0;rt<2;rt++){
        for(int i=1;i<2*n-1;i++)
            A[i] = area(P[1],P[i],P[i+1]) + A[i-1];//printf("%d : %lf\n",i,A[i]);
        int id = 2;
        for(int i=1;i<=n;i++){
            if(id <= i) id = i+1;
            double t = dot(P[i+1],P[i],P[id]);
            while(dot(P[i+1],P[i],P[id+1])-t < 1e-12) t = dot(P[i+1],P[i],P[++id]);
            if(id == i+1)
                ans = 0.00;
            else
                ans = min(ans,findArea(P[i],P[i+1],P[id])-qArea(i+1,id));
            //printf("%d : %d %lf %lf %lf %lf\n",i,id,ans,findArea(P[i],P[i+1],P[id]),qArea(i+1,id),t);
        }
        reverse(P+1,P+n+n+1);
    }
    printf("%.10lf\n",ans);
    return 0;
}