import java.util.Scanner;
class CLNDR {

	public static int leap(int n)
	{
		if(n%4==0)
		{
			if(n%100==0)
			{
				if(n%400==0)				
					return 1;	
				else
					return 0;
			}
			else
				return 1;
		}
		else
			return 0;
		
	}
	

	public static void main(String args[])
	{
		Scanner s1=new Scanner(System.in);
	    String str_arr[];
	    int n,olu,year,dt,leap_yr,mon,j,h=0,t=0,o=0;
	    String month="";
	    n=s1.nextInt();
	    StringBuffer sb=new StringBuffer();
	    for(olu=1;olu<=n;olu++)
	    {
	        str_arr=(s1.next()).split("-");
	        dt=Integer.parseInt(str_arr[0]);
	        year=Integer.parseInt(str_arr[2]);
	        leap_yr=leap(year);
	        month=str_arr[1];
	        if(month.equals("JAN"))
	            mon=1;
	        else if(month.equals("FEB"))
	            mon=2;
	        else if(month.equals("MAR"))
	            mon=3;
	        else if(month.equals("APR"))
	            mon=4;
	        else if(month.equals("MAY"))
	            mon=5;
	        else if(month.equals("JUN"))
	            mon=6;
	        else if(month.equals("JUL"))
	            mon=7;
	        else if(month.equals("AUG"))
	            mon=8;
	        else if(month.equals("SEP"))
	            mon=9;
	        else if(month.equals("OCT"))
	            mon=10;
	        else if(month.equals("NOV"))
	            mon=11;
	        else if(month.equals("DEC"))
	            mon=12;
	        else
	            mon=-1;
	        
	        //System.out.printf("Date %d Month %d Year %d olu%d\n",dt,mon,year,olu);
	        for(j=1;j<mon;j++)
	        {
	            if(j%2==0)
	            {
	                if(j==2)
	                {
	                    if(leap_yr==1)
	                        h+=29;
	                    else
	                        h+=28;
	                }
	                else if(j>=8)
	                    h+=31;
	                else
	                    h+=30;
	            }
	            else
	            {
	                if(j>=9)
	                    h+=30;
	                else
	                    h+=31;
	            }
	        }
	        h+=dt;
	        if(h>300)
	        {
	            t=h-300;
	            h=300;
	            if(t>60)
	            {
	                o=t-60;
	                t=60;
	            }
	        }	        
	        //System.out.printf("Case %d: ",olu);
	        sb.append("Case "+olu+": ");
	        if(o!=0)
	            //System.out.printf("%d Ones",o);
	        	sb.append(o+" Ones");
	        else if(t!=0)
	            //System.out.printf("%d Tens",t);
	        	sb.append(t+" Tens");
	        else
	            //System.out.printf("%d Hundreds",h);
	        	sb.append(h+" Hundreds");
	        //System.out.printf("\n");
	        sb.append("\n");
	        h=0;
	        t=0;
	        o=0;
	    }
	    System.out.print(sb);
	}

}
