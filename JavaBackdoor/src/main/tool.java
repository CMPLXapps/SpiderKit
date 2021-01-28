package main;

import java.util.*;

public class tool {
	public static final Scanner USRIN = new Scanner(System.in);
	//public static final Scanner FILEIN = new Scanner(new File());
	
	public String getUsrIn(String msg) {
		System.out.print(msg);
		Scanner scan = new Scanner(System.in);
		String in = scan.nextLine();
		scan.close();
		return in;
	}
	public static void println(String msg) {System.out.print(msg);}
	public static void print(String msg) {System.out.println(msg);}
}