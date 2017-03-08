import java.io.*;
import java.util.*;
class Malvika{
	public static void main(String args[]) throws IOException{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int t=Integer.parseInt(br.readLine());
		while(t>0){
			String s = br.readLine();
			ArrayList<Character> a1 = new ArrayList<Character>();
			ArrayList<Character> a2 = new ArrayList<Character>();
			for(int i = 0;i < s.length();i++){
				if(s.charAt(i) == 'a')
					a1.add(s.charAt(i));
				else
					a2.add(s.charAt(i));
			}
			if(a1.size() < a2.size())
				System.out.println(a1.size());
			else
				System.out.println(a2.size());
			t--;
		}
	}
}