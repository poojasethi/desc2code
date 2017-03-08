import java.util.*;
import java.io.*;
class WATSY
{


    /************************ SOLUTION STARTS HERE ***********************/
    static class Node 
    {
	long key;
	int height;
	int size;
	Node left,right,parent;
	Node(long key)
	{
	    this.key = key;
	    height = 1;
	    size = 1;
	    left = right = parent = null;
	}
	@Override
	public String toString() {
	    return "[key = "+key+" h = "+height+"]"+ " p = "    
		    +          (parent != null ? parent.key :"null")  
		    +" l = " + (left   != null ? left.key   :"null")  
		    +" r = " + (right  != null ? right.key  :"null");
	}
    }

    static class AVLTree
    {
	Node root;
	public AVLTree() {
	    root = null;	    
	}
	private int height(Node n)
	{
	    return n == null ? 0 : n.height;
	}
	public void add(long key)
	{	    
	    root = add(key, root, null);
	    Node N = search(root, key);
	    root = rebalance(N);
	}
	public boolean find(long key)
	{
	    return search(root, key) != null;
	}
	public int query(long key)
	{
	    return query(root, key);
	}
	private int query(Node root , long key)
	{
	    if(root != null)
	    {
		if(key > root.key)
		    return 1 + size(root.left) + query(root.right, key);
		else
		    return query(root.left, key);
	    }
	    else
		return 0;
	}
	private int size(Node n)
	{
	    return n == null ? 0 : n.size;
	}
	private void adjustHeight(Node N)
	{
	    N.height = 1 + Math.max(height(N.left),height(N.right));	    
	    adjustSize(N);    //Small hack , so that I need not call it explicitly!!
	}
	private void adjustSize(Node N)
	{
	    N.size = 1 + size(N.left) + size(N.right);
	}
	private Node rotateRight(Node N)
	{
	    Node oldPar = N.parent;
	    Node newN = N.left;
	    N.left = newN.right;
	    if(newN != null && newN.right != null && newN.right.parent != null)
		newN.right.parent = N;
	    adjustHeight(N);
	    newN.parent = oldPar;
	    newN.right = N;
	    adjustHeight(newN);
	    N.parent = newN;
	    if(oldPar != null)
	    {
		if(oldPar.left == N)
		    oldPar.left = newN;
		else
		    oldPar.right = newN;

		adjustHeight(oldPar);
	    }
	    return newN;
	}
	private Node rotateLeft(Node N)
	{
	    Node oldPar = N.parent;
	    Node newN = N.right;
	    N.right = newN.left;
	    if(newN != null  && newN.left != null && newN.left.parent != null)
		newN.left.parent = N;
	    adjustHeight(N);
	    newN.parent = oldPar;
	    newN.left = N;
	    N.parent = newN;
	    adjustHeight(newN);
	    if(oldPar != null)
	    {
		if(oldPar.left == N)
		    oldPar.left = newN;
		else
		    oldPar.right = newN;

		adjustHeight(oldPar);
	    }
	    return newN;
	}
	private Node search(Node root , long key)
	{
	    if(root != null)
		return ((root.key == key) ? root : (key < root.key ? search(root.left, key) : search(root.right, key)));
	    else
		return null;
	}


	private Node rebalance(Node N)
	{
	    Node par = N.parent;
	    if (height(N.left) - height(N.right) >= 2)
	    {
		Node M = N.left;
		if(height(M.right) > height(M.left))
		    M = rotateLeft(M);
		N = rotateRight(N);
	    }
	    if(height(N.right) - height(N.left) >= 2)
	    {
		Node M = N.right;
		if(height(M.left) > height(M.right))
		    M = rotateRight(M);

		N = rotateLeft(N);
	    }

	    if(par != null)	    
		return rebalance(par);	    
	    else 
		return N;

	}
	private Node add(long key,Node root, Node parent)
	{
	    if(root == null)
	    {
		Node newNode = new Node(key);
		newNode.parent = parent;
		return newNode;
	    }
	    else
	    {
		if(key < root.key)
		    root.left = add(key, root.left , root);
		else 
		    root.right = add(key, root.right, root);		

		adjustHeight(root);
		return root;
	    }
	}
    }


    private static void solve(FastScanner s1, PrintWriter out){

	int t = s1.nextInt();
	while(t-->0)
	{
	    AVLTree tree = new AVLTree();   
	    int len = s1.nextInt();
	    while(len-->0)
	    {
		long key = s1.nextLong();
		tree.add(key);
		out.print(tree.query(key) + " ");
	    }
	    out.println();
	}

    }



    /************************ SOLUTION ENDS HERE ************************/





    /************************ TEMPLATE STARTS HERE *********************/

    public static void main(String []args) throws IOException {
	FastScanner in  = new FastScanner(System.in);
	PrintWriter out = 
		new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)), false); 
	solve(in, out);
	in.close();
	out.close();
    }    

    static class FastScanner{
	BufferedReader reader;
	StringTokenizer st;
	FastScanner(InputStream stream){reader=new BufferedReader(new InputStreamReader(stream));st=null;}	
	String next()
	{while(st == null || !st.hasMoreTokens()){try{String line = reader.readLine();if(line == null){return null;}		    
	st = new StringTokenizer(line);}catch (Exception e){throw new RuntimeException();}}return st.nextToken();}
	String nextLine()  {String s=null;try{s=reader.readLine();}catch(IOException e){e.printStackTrace();}return s;}	    	  	
	int    nextInt()   {return Integer.parseInt(next());}
	long   nextLong()  {return Long.parseLong(next());}		
	double nextDouble(){return Double.parseDouble(next());}
	char   nextChar()  {return next().charAt(0);}
	int[]  nextIntArray(int n)         {int[] arr= new int[n];   int i=0;while(i<n){arr[i++]=nextInt();}  return arr;}
	long[] nextLongArray(int n)        {long[]arr= new long[n];  int i=0;while(i<n){arr[i++]=nextLong();} return arr;}	
	int[]  nextIntArrayOneBased(int n) {int[] arr= new int[n+1]; int i=1;while(i<=n){arr[i++]=nextInt();} return arr;}	    	
	long[] nextLongArrayOneBased(int n){long[]arr= new long[n+1];int i=1;while(i<=n){arr[i++]=nextLong();}return arr;}	    	
	void   close(){try{reader.close();}catch(IOException e){e.printStackTrace();}}				
    }

    /************************ TEMPLATE ENDS HERE ************************/
}