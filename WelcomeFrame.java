import javax.swing.*;
import java.awt.*;
import java.awt.event.*;


public class WelcomeFrame extends JFrame implements ActionListener {
    private JTextField usernameField;
    private JPasswordField passwordField;
    private JButton loginButton;
    private JButton createAccount;

    public WelcomeFrame() {
        this.initComponents();

    }

    public void actionPerformed(ActionEvent event){
        System.out.println("button Clicked");

    }


    private void initComponents() {
        usernameField = new JTextField(20);// 20=width you can put the default value also 
        passwordField = new JPasswordField(20);
        loginButton =new JButton("Login");
        createAccount= new JButton("Create Account");
        createAccount.addActionListener(this);


        this.setLayout(new FlowLayout ());

        this.add(usernameField);
        this.add(passwordField);
        this.add(loginButton);
        this.add(createAccount);

        this.setSize(500,300);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//exit_on_close is as static variable of Class JFrame thats why it is in al CapsLetter


    }

}