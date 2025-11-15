import java.sql.*;

public class DatabaseDAO implements DataAccessObject{
    public void save( String username, String password){
        //System.out.println("Save to Database");
        try{
            //1.Load the driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            System.out.println("Drievr Loaded");

            //2. create connection
           
           String url = "jdbc:mysql://localhost:3306/kit";
           String user = "root";
           String pass = "abc123";
           Connection  con;
           con = DriverManager.getConnection(url, user, pass);

            //System.out.println("Connected to DB")

             //3create and run the query
            String query ="insert into users(username,password) values(?,?)";
            PreparedStatement ps = con.prepareStatement(query);
            ps.setString(1,username);
            ps.setString(2,password);
            ps.executeUpdate();

            //4.close the connection
            con.close();




        } catch(Exception ex){
            ex.printStackTrace();
        }
    }

}