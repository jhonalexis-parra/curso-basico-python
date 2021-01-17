class Card extends Payment{
    constructor(id, amount, card_number, card_date, card_cvv){
        super(id, amount);
        this.card_number = card_number;
        this.card_date = card_date;
        this.card_cvv = card_cvv;
    }
}