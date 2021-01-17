class Paypal extends Payment {
    String email;
    String password;
    
    public Paypal (Integer id, Integer amount, String email, String password){
        super(id, amount);
        this.email = email;
        this.password = password;
    }
}