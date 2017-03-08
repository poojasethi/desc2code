#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    int year;
    cin>>t;
    string a[7];

    a[0] = "monday";
    a[1] = "tuesday";
    a[2] = "wednesday";
    a[3] = "thursday";
    a[4] = "friday";
    a[5] = "saturday";
    a[6] = "sunday";
/*

    for(i=0;i<T;i++)
    {
        c=0;
        if(year[i]>=2001&&year[i]<=2500)
        {
            d=year[i]-2001;
            c+=d;
            if(d>=4)
                c+=d/4;
            c=c%7;

        }
        else if(year[i]<2001&&year[i]>=1900)
        {
            d=2001-year[i];
            c-=d;
            if(d>=4)
                c-=d/4;
            c=6+(c%7);

        }*/
    while(t--)
    {
        cin>>year;
        int ind = 0;
        int ctr = 0;
            if(year < 2001)
            {
                for(int i = 1900; i < year; i++ )
                {
                    if( (i % 4 == 0 && i % 100 != 0) || (i % 400 == 0) )
                        ctr++;
                    ctr++;
             //       if(ctr %  7 == 0)
                //        cout<<i<<endl;
                }
               // if(ctr % 7 == 0)
                  //  ind = 0;
                ind =( ctr% 7 ) ;
            }
            else if(year == 2001)
                ind = 0;

            else
            {
                for(int i = 2001;i < year; i++)
            {
                if( (i % 4 == 0 && i % 100 != 0) || (i % 400 == 0) )
                {
                    ctr++;
                }
                ctr++;
            }
            ind = ctr % 7;
            }
        /*if(year >= 2001 && year <= 2500)
            {
                //ind = ind + (year - 2001);
                //if((year - 2001) >= 4)
                   // ind = ind + (year - 2001)/4;
                ind = (ind + ( year - 2001) / 4 + (year - 2001))  % 7;
            }

            else if(year< 2001 && year >= 1900)
            {
              //  ind = ind - (2001 - year);
                //if((2001 - year) >= 4)
                   // ind = ind - (2001 - year)/4;
                ind = 6 + (ind - (2001 - year) / 4 - (2001 - year))%7;
            }
*/
            cout<<a[ind]<<endl;

    }
    return 0;
}
