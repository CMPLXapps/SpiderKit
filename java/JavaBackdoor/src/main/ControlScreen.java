package main;

import java.awt.*;

import javax.swing.*;

public class ControlScreen {
	
	private static final int w = 800;
	private static final int h = 600;
	
	ControlScreen() {
		JFrame frame = new JFrame();
		JPanel panel = new JPanel();
		
		//Panel Configuration
		panel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
		panel.setLayout(new GridLayout(0, 1));
		
		//Frame Configuration
		frame.add(panel, BorderLayout.CENTER);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setTitle("JavaBackdoor v1.0.0 | Backdoor Controls");
		frame.pack();
		
		//Window Elements
		
		
		//----------------------
		frame.setSize(w, h);
		frame.setVisible(true);
	}
}