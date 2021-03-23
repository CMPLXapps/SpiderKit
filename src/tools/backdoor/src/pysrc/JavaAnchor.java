package pysrc;

import java.util.HashMap;
import java.util.Map;

public abstract class JavaAnchor {
	public static Map<String, String> fileMap = new HashMap<String, String>();
	
	public static void main(String[] args) {
		fileMap.put("listener", "listener.py"); fileMap.put("client", "client.pyw"); fileMap.put("kill", "killswitch.py"); fileMap.put("char", "cfg/chars.json");
		fileMap.put("config", "configure.pyw"); fileMap.put("token_generator", "generate_new_token.pyw"); fileMap.put("help", "cfg/help.txt");
		
		
	}
}