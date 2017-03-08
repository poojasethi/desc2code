#include<cstdio>
#include<cmath>
#define MAXN 110

int x[MAXN],y[MAXN],n,xs,ys,xe,ye,BL;

double d[MAXN],FirstX,FirstY,FirstD,SecondX,SecondY,SecondD,Ans1,Ans2,Ans3,Ans4,D;

struct pt{int a,b,c;} A,B;

double MIN(double a,double b){return a<b?a:b;}

double DIS(double a,double b){return sqrt(a*a+b*b);}

int XJ(int a,int b,int c,int d,int e,int f){return (c-a)*(f-b)-(d-b)*(e-a);}

void Get(double&X,double&Y,double&D,int i)
{
	A.a=ye-ys;
	A.b=xs-xe;
	A.c=A.a*xe+A.b*ye;
	B.a=y[i]-y[i+1];
	B.b=x[i+1]-x[i];
	B.c=B.a*x[i]+B.b*y[i];
	if(A.a*B.b-B.a*A.b==0)return;
	X=1.0*(A.c*B.b-B.c*A.b)/(A.a*B.b-B.a*A.b);
	Y=(A.c-A.a*X)/A.b;
	D=d[i]+DIS(x[i]-X,y[i]-Y);
	BL++;
	if(BL==2&&fabs(FirstX-SecondX)<1e-4&&fabs(FirstY-SecondY)<1e-4)
		BL--;	
}

int main()
{
	int i;
	scanf("%d%d%d%d%d",&xs,&ys,&xe,&ye,&n);
	for(i=0;i<n;i++)
		scanf("%d%d",x+i,y+i);
	x[n]=x[0];
	y[n]=y[0];
	for(i=1;i<=n;i++)
		d[i]=d[i-1]+DIS(x[i]-x[i-1],y[i]-y[i-1]);
	for(i=0;i<n&&BL<2;i++)
		if(
			XJ(xe,ye,x[i],y[i],x[i+1],y[i+1])*
			XJ(xs,ys,x[i],y[i],x[i+1],y[i+1])<=0&&
			XJ(x[i],y[i],xe,ye,xs,ys)*
			XJ(x[i+1],y[i+1],xe,ye,xs,ys)<=0
			)
		{
			if(BL)
				Get(SecondX,SecondY,SecondD,i);
			else
				Get(FirstX,FirstY,FirstD,i);
		}
	if(!BL)
		printf("%.6lf\n",DIS(xe-xs,ye-ys));
	else
	{
		D=fabs(SecondD-FirstD);
		if(D>d[n]-D)
			D=d[n]-D;
		Ans1=DIS(xs-FirstX,ys-FirstY)+DIS(xe-SecondX,ye-SecondY);
		Ans2=DIS(xs-SecondX,ys-SecondY)+DIS(xe-FirstX,ye-FirstY);
		Ans3=D;
		Ans4=2*DIS(FirstX-SecondX,FirstY-SecondY);
		printf("%.10lf\n",MIN(Ans1,Ans2)+MIN(Ans3,Ans4));
	}
	return 0;
}