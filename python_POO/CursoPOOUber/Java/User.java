class User extends Account {
    Integer id;
    String email;
    String password;
    
    public User (Integer id, String name, String document, String email, String password){
        super(name, document);
        this.id = id;
        this.email = email;
        this.password = password;
    }
}