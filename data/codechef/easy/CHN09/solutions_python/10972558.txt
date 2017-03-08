import java.util.Scanner;

class zeros {
	
	public static void main(String[] args) {
		
		Scanner scan=new Scanner(System.in);
		int t=scan.nextInt();
		if(t>=1&&t<=100){
		for(int i=0;i<t;i++){
			String bal=scan.next();
			if(bal.length()>=1&&bal.length()<=100){
			int a=0,b=0;
			for(int j=0;j<bal.length();j++){
				if(bal.charAt(j)=='a'){a++;}
				else if(bal.charAt(j)=='b'){b++;}
			}
			if(a==0||b==0){System.out.println("0");}
			else if(b>=a){System.out.println(a);}
			else{System.out.println(b);}
		}
		}
				}
			scan.close();
		}
	
}