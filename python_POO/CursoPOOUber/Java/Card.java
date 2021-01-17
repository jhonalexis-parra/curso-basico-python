class Card extends Payment {
    Integer card_number;
    String card_date;
    Integer card_cvv;
    
    public Card (Integer id, Integer amount, Integer card_number, String card_date, Integer card_cvv){
        super(id, amount);
        this.card_number = card_number;
        this.card_date = card_date;
        this.card_cvv = card_cvv;
    }
}