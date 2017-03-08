#include<stdio.h>
#include<string.h>

typedef long long int lld;
#define gc getchar_unlocked

void si(lld *p)
{ lld x =0,neg=0;
     char c=gc();
    //  if(c=='-'){ neg=-1; printf("bb") ;} 
     while((c<'0'|| c>'9') && c!='-')
          c=gc();
     if(c=='-') {neg=1; c=gc();} 
     for(;c>='0' && c<='9';c=gc())
     {
          x=x*10+c-48;
     }
     if(neg==1)         
       x=-1*x;
                        
          *p=x;
}

lld upbs(lld *a,lld i,lld j,lld p,lld size)
{   lld m,flag=0,res=-1,o_m;
     while(i<j+1)
     {
          m=(i+j)/2;
          o_m=m;
          if(a[m]>=p)
          {    res=m;
               j=m-1;
          }

          else
          {
               i=m+1;       
          }
                                                                               //printf("func m=%lld\n",m);


       //    if(m==o_m)
         //       break;
          
     }

     if(res==-1)
          return -1;
     else
          return res;
}

int main (){
     lld a[100010],b[100010],c[100010],i,j,n,m,res,test,i1,p,q,r;//,temp[100010]={ 0};
     si(&test);
     unsigned long long int sum,a1,a2;
     for(i1=0;i1<test;i1++)
     {    sum=0;       lld temp[100010]={ 0 };
          si(&p);        //  printf("%lld\n",p);

          for(i=0;i<p;i++)
               si(&a[i]);

          si(&q);

          for(i=0;i<q;i++)
               si(&b[i]);

          si(&r);

          for(i=0;i<r;i++)
               si(&c[i]);


          //   scanf("%d",&p);
          i=0; 

          for(j=0;j<q;j++)
          {
              a2=upbs(c,j,r-1,b[j],r);  // printf("a2=%lld\n",a2);
              if(a2!=-1)
                   temp[j]=r-a2;
              else
                  { temp[j]=0;
                       break;
                  }
                                  // printf("tempinti =%lld\n\n",temp[j]);
          }

          for(j=q-2;j>=0;j--)
          {
               if(temp[j]!=0 )
                    temp[j]+=temp[j+1];
                    
                                //   printf("temp=%lld\n",temp[j]);
          }   
      ///    for(j=0;j<q;j++) printf("%lld ",temp[j]);   printf("\n");

          for(i=0;i<p;i++)
          {
               a1=upbs(b,i,q-1,a[i],q);
                                           //     printf("%lld\n",a1);

               if(a1!=-1)              //   printf("a1=%lld\n",a1) ;
               {
                  if(temp[a1]!=-1)
                       sum+=temp[a1];  //printf("sum=%lld\n",sum);
                
               }

               if(a1==-1)
               {
                    break;
               }

          }

          printf("%lld\n",sum);

   // memset(temp,0,sizeof(q))  ;    
         
     }
     return 0;
}

