package main;

import java.util.*;

public class Tools {
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
	public void print(String msg) {System.out.println(msg);}
}