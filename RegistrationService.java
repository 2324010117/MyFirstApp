public class RegistrationService {
    public void register(String username,String password){

        //validate the parameters

        DataAccessObject dao;

        dao = new FileDAO();
        dao.save(username,password);

        dao = new DatabaseDAO();
        dao.save(username,password);
    } 
} 