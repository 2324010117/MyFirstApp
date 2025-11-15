public class Main{
    public static void main(String []args){
        //WelcomeFrame frame = new WelcomeFrame();
        //RegistrationFrame frame = new RegistrationFrame();
        DatabaseDAO dao = new DatabaseDAO();
        dao.save("kit","kit123");
        //frame.setVisible(true);
        
    }
}