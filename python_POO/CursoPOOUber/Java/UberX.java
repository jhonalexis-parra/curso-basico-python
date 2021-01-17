class UberX extends Car {
    String typeCarAccepted;
    String model;
    
    public UberX (String license, Account driver, String typeCarAccepted, String model){
        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.model = model;
    }
}