package main;

import java.io.*;

public class Console {
	
	private static final Tools t = new Tools();
	
	public String run(String command) {
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
