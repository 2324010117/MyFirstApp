import java.io.*;

public class FileDAO implements DataAccessObject {
    public void save(String username, String password) {
        // file handling code
        //System.out.println("Saved to file");
        try{
            String fileName="users.txt ";
            FileWriter writer = new FileWriter(fileName,true);
            try{
                // process data
                //String data = usernamae + "," + password + "\n" ;
                String data = String.format("%s,%s\n", username,password);
                writer.write(data);

            }finally{
                //close file
                writer.close();
            }
        }catch(Exception ex){
            //handle Error
            ex.printStackTrace();
        }
    }


}