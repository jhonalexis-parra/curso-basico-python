class UberPool extends Car {
    String typeCarAccepted;
    String model;
    
    public UberPool (String license, Account driver, String typeCarAccepted, String model){
        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.model = model;
    }
}