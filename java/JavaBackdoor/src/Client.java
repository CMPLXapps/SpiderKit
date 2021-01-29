import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Client {
	
	public static class t {
		public final Scanner USRIN = new Scanner(System.in);
		//public final Scanner FILEIN = new Scanner(new File());
		
		public String getUsrIn(String msg) {
			System.out.print(msg);
			Scanner scan = new Scanner(System.in);
			String in = scan.nextLine();
			scan.close();
			return in;
		}
		public void println(String msg) {System.out.print(msg);}
		public static void print(String msg) {System.out.println(msg);}
	}
	
	public class console {
		public String runcmd(String command) {
			Runtime runtime = Runtime.getRuntime();
			BufferedReader stdout = null;
			BufferedReader stderr = null;
			try {
				Process process = runtime.exec(command);
				stdout = new BufferedReader(new InputStreamReader(process.getInputStream()));
				stderr = new BufferedReader(new InputStreamReader(process.getErrorStream()));
			} catch (Exception e) {
				t.print("Console Errored!\n\n");
				e.printStackTrace();
				return "Done; fatal error.";
			}
			String consoleStream = "Console Errored!\n\n";
			try {
				consoleStream = "Out Stream:\n"+stdout.readLine()+"\nError Stream:\n"+stderr.readLine();
			} catch (Exception e) {
				e.printStackTrace();
			}
			return consoleStream;
		}
	}
	
	private static void main(String[] args) {
		
	}
}
