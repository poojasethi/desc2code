
import java.io.IOException;
import java.util.Arrays;
import java.util.InputMismatchException;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author hitarthk
 */
class KOl1 {
    public static void main(String[] args) {
        FasterScanner in=new FasterScanner();
        int t=in.nextInt();
        while(t-->0){
            long n=in.nextLong();
            int k=in.nextInt();
            if(k==0 || n<k){
                if(n==1){
                    System.out.println(1);
                }
                else
                System.out.println(getFibonacciNumber(n+2));
                continue;
            }
            total=constructTotalMat(k);
            excl=constructExclMat(k);
            constructIdentity(k);
            long[][] ansTotal=matrixExp(total, n-1, true);
            long[][] ansExcl=matrixExp(excl, n-1, false);
            //System.out.println("ExpTotal "+Arrays.deepToString(ansTotal));
            //System.out.println("Exp excl "+Arrays.deepToString(ansExcl));
            long[][] initTotal=new long[2*k][1];
            long[][] initExcl=new long[2*k][1];
            //System.out.println("Total "+Arrays.deepToString(total));
            //System.out.println("Excl "+Arrays.deepToString(excl));
            initTotal[0][0]=2;
            if(k==1){
                initTotal[0][0]++;
            }
            initTotal[1][0]=1;
            if(k>=2){
                initTotal[2][0]=1;
            }
            initExcl[0][0]=1;
            if(k==1){
                initExcl[0][0]++;
            }
            initExcl[1][0]=1;
            if(k>=2){
                initExcl[2][0]=1;
            }
            long[][] finalTotal=multiply(ansTotal, initTotal);
            long[][] finalExcl=multiply(ansExcl, initExcl);
            //System.out.println("vectrtotal "+Arrays.deepToString(finalTotal));
            //System.out.println("vectorExclusive "+Arrays.deepToString(finalExcl));
            long finalAns=((finalTotal[0][0]-finalExcl[0][0])%mod+mod)%mod;
            System.out.println(finalAns);
        }
    }
    
    static long[][] matrixExp(long[][] T,long n,boolean type){
        if(n==0){
            return identity;
        }
//        if(n==1){
//            if(type){
//                return total;
//            }
//            else
//                return excl;
//        }
//        
        else{
            long[][] ans=matrixExp(T, n/2, type);
            ans=multiply(ans, ans);
            if((n&1)!=0){
                if(type){
                    ans=multiply(ans, total);
                }
                else{
                    ans=multiply(ans, excl);
                }
            }
            return ans;
        }
    }
    
    static void constructIdentity(int k){
        identity=new long[2*k][2*k];
        for(int i=0;i<2*k;i++){
            identity[i][i]=1;
        }
    }
    
    static long[][] total;
    static long[][] excl;
    static long[][] identity;
    static long mod=(long)1e7+7;
    static long[][] constructTotalMat(int k){
        long[][] a=constructExclMat(k);
        for(int i=0;i<2*k;i++){
            if(i%2==0){
                a[i][i]+=1;
                a[i][i+1]+=1;
            }
            
        }
        return a;
       
    } 
    
    static long[][] constructExclMat(int k){
        long[][] a=new long[2*k][2*k];
        for(int i=0;i<2*k;i++){
            if(i%2==0){
                int fs=i/2;
                int ss=((fs-1)%k+k)%k;
                int ts=2*ss;
                a[i][ts]=1;
                a[i][ts+1]=1;
                
            }
            else{
                a[i][i-1]=1;
            }
        }
        return a;
    }
    
    static long[][] multiply(long[][] a,long[][] b){
        long[][] c=new long[a.length][b[0].length];
        for(int i=0;i<c.length;i++){
            for(int j=0;j<c[0].length;j++){
                for(int k=0;k<b.length;k++){
                    c[i][j]+=(a[i][k]*b[k][j])%mod;
                    c[i][j]-=c[i][j]>=mod?mod:0;
                }
            }
        }
        return c;
    }
    
    /*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author hitarthk
 */
static class FasterScanner {

    private byte[] buf = new byte[1024];
    private int curChar;
    private int numChars;

    public int read() {
        if (numChars == -1) {
            throw new InputMismatchException();
        }
        if (curChar >= numChars) {
            curChar = 0;
            try {
                numChars = System.in.read(buf);
            } catch (IOException e) {
                throw new InputMismatchException();
            }
            if (numChars <= 0) {
                return -1;
            }
        }
        return buf[curChar++];
    }

    public String nextLine() {
        int c = read();
        while (isSpaceChar(c)) {
            c = read();
        }
        StringBuilder res = new StringBuilder();
        do {
            res.appendCodePoint(c);
            c = read();
        } while (!isEndOfLine(c));
        return res.toString();
    }

    public String nextString() {
        int c = read();
        while (isSpaceChar(c)) {
            c = read();
        }
        StringBuilder res = new StringBuilder();
        do {
            res.appendCodePoint(c);
            c = read();
        } while (!isSpaceChar(c));
        return res.toString();
    }

    public long nextLong() {
        int c = read();
        while (isSpaceChar(c)) {
            c = read();
        }
        int sgn = 1;
        if (c == '-') {
            sgn = -1;
            c = read();
        }
        long res = 0;
        do {
            if (c < '0' || c > '9') {
                throw new InputMismatchException();
            }
            res *= 10;
            res += c - '0';
            c = read();
        } while (!isSpaceChar(c));
        return res * sgn;
    }

    public int nextInt() {
        int c = read();
        while (isSpaceChar(c)) {
            c = read();
        }
        int sgn = 1;
        if (c == '-') {
            sgn = -1;
            c = read();
        }
        int res = 0;
        do {
            if (c < '0' || c > '9') {
                throw new InputMismatchException();
            }
            res *= 10;
            res += c - '0';
            c = read();
        } while (!isSpaceChar(c));
        return res * sgn;
    }

    public int[] nextIntArray(int n) {
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = nextInt();
        }
        return arr;
    }

    public long[] nextLongArray(int n) {
        long[] arr = new long[n];
        for (int i = 0; i < n; i++) {
            arr[i] = nextLong();
        }
        return arr;
    }

    private boolean isSpaceChar(int c) {
        return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
    }

    private boolean isEndOfLine(int c) {
        return c == '\n' || c == '\r' || c == -1;
    }
}

    public static int getFibonacciNumber(long n)
 	{
 		// %1000000007
 		int F[][] = { { 1, 1 }, { 1, 0 } };
 		if (n == 0)
 			return 0;
 		matrixpower(F, n - 1);
 		return F[0][0];
 	}

 	public static void matrixpower(int F[][], long n) 
 	{
 		if (n == 0 || n == 1)
 			return;
 		int M[][] = { { 1, 1 }, { 1, 0 } };

 		matrixpower(F, n / 2);
 		multiply(F, F);

 		if (n % 2 != 0)
 			multiply(F, M);
 	}

 	public static void multiply(int F[][], int M[][]) 
 	{
 		long t;

 		long x = F[0][0] % mod;
 		x *= M[0][0] % mod;
 		t = F[0][1] % mod;
 		t *= M[1][0] % mod;
 		x += t % mod;
 		x %= mod;

 		long y = F[0][0] % mod;
 		y *= M[0][1] % mod;
 		t = F[0][1] % mod;
 		t *= M[1][1] % mod;
 		y += t % mod;
 		y %= mod;

 		long z = F[1][0] % mod;
 		z *= M[0][0] % mod;
 		t = F[1][1] % mod;
 		t *= M[1][0] % mod;
 		z += t % mod;
 		z %= mod;

 		long w = F[1][0] % mod;
 		w *= M[0][1] % mod;
 		t = F[1][1] % mod;
 		t *= M[1][1] % mod;
 		w += t % mod;
 		w %= mod;

 		F[0][0] = (int) x;
 		F[0][1] = (int) y;
 		F[1][0] = (int) z;
 		F[1][1] = (int) w;
 	}

    
}
