import java.util.*;
class Program{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		
		while(t!=0){
		    
		    String str=sc.next();
		    int c=0,d=0,p=0;
		    for(int i=0;i<str.length();i++){
		        if(str.charAt(i)=='a')
		            c++;
		        else if(str.charAt(i)=='b')
		            d++;
		    }
		    if(c<=d&&c!=0){
		        p=c;}
		    else if(d<=c&&d!=0){
		        p=d;}
		    else if(c==0||d==0){
		        p=0;}
		    System.out.println(p);
		    t--;
		}
	}
} 