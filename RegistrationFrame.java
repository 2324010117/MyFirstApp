import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.lang.*;

public class RegistrationFrame extends JFrame implements ActionListener{
    private JTextField usernameField;
    private JPasswordField passwordField;
    //private JPasswordField confirmPasswordField;
    private JButton registrationButton;

    RegistrationFrame(){
        this.initComponents();
    }

    public void actionPerformed(ActionEvent event){
        String username = usernameField.getText();
        String password = passwordField.getText();
        //String confirmPassword = confirmPasswordFieldpasswordField.getText();

        RegistrationService service = new RegistrationService();
        service.register(username,password);

    }

    void initComponents(){
        usernameField = new JTextField(20);
        passwordField = new JPasswordField(20);
        //confirmPasswordField = new JPasswordField(20);
        registrationButton = new JButton("Register");
        registrationButton.addActionListener(this);

        this.setLayout(new FlowLayout ());

        this.add(usernameField);
        this.add(passwordField);
        //this.add(confirmPasswordField);
        this.add(registrationButton);

        this.setSize(500,300);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    }

}