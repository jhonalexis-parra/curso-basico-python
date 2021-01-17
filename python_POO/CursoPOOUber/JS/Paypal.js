class Paypal extends Payment {
    constructor(id, amount, email, password){
        super(id, amount);
        this.email = email;
        this.password = password;
    }
}