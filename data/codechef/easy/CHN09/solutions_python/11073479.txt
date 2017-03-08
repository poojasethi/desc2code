import java.io.*;

class Test {
    public static void main(String args[]) throws java.lang.Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader (System.in));
        
        int t, n, i, a=0, b=0;
        t = Integer.parseInt(br.readLine());
        for(; t>0; t--)
        {
            String s = br.readLine();
            n = s.length();
            char ch[] = s.toCharArray();
            a=0;b=0;
            for(i=0; i<n; i++)
            {
                if(ch[i] =='a')
                   a++;
                else
                   b++;
            }
            if(a>b)
                System.out.println(b);
            else
                System.out.println(a);
        }
    }
}