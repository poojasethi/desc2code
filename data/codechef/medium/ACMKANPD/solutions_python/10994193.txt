import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class ACMKANPD {

	public static int binaryToDecimal(String binary) {
		
		int total = 0;
		int binLen = binary.length();
		for(int i = 0; i < binLen; i++) {
			total = total * 2 + (binary.charAt(i) - '0');
		}
		return total;
	}
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] inputLine = br.readLine().split(" ");
		String input = inputLine[0];
		StringBuilder binary = new StringBuilder();
		int flag = 0;
		
		for(int i = 1; !input.equals("~"); i++) {
			
			if(input.equals("0")) {
				flag = 1;
			} else if(input.equals("00")) {
				flag = 0;
			} else if(input.equals("#")) {
				System.out.println(binaryToDecimal(binary.toString()));
				binary = new StringBuilder();
			} else {
				int numZerosInBlock = input.length();
				for(int j = 0; j < numZerosInBlock-2; j++) {
					binary.append(flag);
				}
			}
			if(i < inputLine.length) {
				input = inputLine[i];
			} else {
				inputLine = br.readLine().split(" ");
				i = 0;
				input = inputLine[0];
			}
		}
	}
}