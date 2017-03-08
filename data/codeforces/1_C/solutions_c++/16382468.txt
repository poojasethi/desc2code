#include <bits/stdc++.h>

using namespace std;

double gcd(double x, double y)
{
    return fabs(y)<1e-4?x:gcd(y,fmod(x,y));
}

int main() 
{
    double a,b,c,R,A,B,C,S,n,area,Ax,Ay,Bx,By,Cx,Cy;
    scanf("%lf%lf%lf%lf%lf%lf",&Ax,&Ay,&Bx,&By,&Cx,&Cy);
    a=sqrt( (Bx-Cx)*(Bx-Cx) + (By-Cy)*(By-Cy) );
    b=sqrt((Ax-Cx)*(Ax-Cx)+(Ay-Cy)*(Ay-Cy));
    c=sqrt((Ax-Bx)*(Ax-Bx) + (Ay-By)*(Ay-By));
    S=(a+b+c)/2;
    S=sqrt(S*(S-a)*(S-b)*(S-c));
    R=(a*b*c)/(4*S);
    A=acos((b*b+c*c-a*a)/(2*b*c));
    B=acos((a*a+c*c-b*b)/(2*a*c));
    C=acos((b*b+a*a-c*c)/(2*b*a));
    n=M_PI/gcd(gcd(A,B),C);
    area=(n*R*R*sin((2*M_PI)/n))/2;
    printf("%0.8lf\n",area);
    return 0;
}
