#include <stdio.h>
#include <cmath>

int main()
{
    double s,p,length,breadth,height,volume;
    double a=3;
    double b=-(s/2);
    double c=p/2;

    double root2;
    double root1;
    double sroot;

    int cases;

    scanf("%d",&cases);

    while(cases--){
        scanf("%lf",&s);
        scanf("%lf",&p);


        b=-(s/2);
        c=p/2;

        root1=((s/2)*(s/2))-(4*a*c);
        sroot=sqrt(root1);
        root1=(-1*b)+sroot;
        root2=(-1*b)-sroot;

        root1=root1/(2*a);
        root2=root2/(2*a);

        if(root1<root2 && root1>0){
            breadth=root1;
        }else
            breadth=root2;


        length=(s-(8*breadth))/4;


        volume=(length*breadth*breadth);

        printf("%.2f\n",volume);
    }

    return 0;
}
