#include<iostream>
#include<vector>
using namespace std;

class cars
{
    public:

    bool loaded;
    int startTime;
    int endTime;

    cars()
    {
        loaded=false;
        startTime=-1;
        endTime=-1;
    }
};

int main()
{
    int t;  //test cases
    int n;  //number of safari cars
    int m;  //number of passengers wandering in the museum
    int q;  //number of passengers in park gate
    int p;  //passenger rides for time p
    int r;  //after every r units of time one passenger from museum adds to q
    int k;  //jurassic park remains open for

    int pc; //passengers who have completed park rid
    int cw; //cars waiting
    int cl; //cars loaded

    cin>>t;

    while(t--)
    {
        cin>>n>>m>>q>>p>>r>>k;

        vector<cars> car;
        car.resize(n);

        int ck=1;

        cw=n;
        cl=0;
        pc=0;

        //process cars while time remains
        while(ck<=k)
        {
                if(m>0 && ck%r==0)
                {
                    q++;
                    m--;
                }

            for(int ci=0;ci<n;ci++)
            {

               if(car[ci].loaded && car[ci].endTime==ck)
                {
                    car[ci]= cars();

                    pc++;
                    cw++;
                    cl--;
                }

                if(q>0 && !car[ci].loaded)
                {
                    car[ci].loaded=true;
                    car[ci].startTime=ck;
                    car[ci].endTime=ck+p;

                    q--;
                    cl++;
                    cw--;
                }


            }

            ck++;
        }

        cout<<cw<<" "<<pc<<" "<<m<<" "<<q<<endl;
    }
}
