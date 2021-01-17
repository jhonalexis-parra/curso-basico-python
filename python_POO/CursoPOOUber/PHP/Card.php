<?php
require_once("Payment.php");

    class Card extends Payment {
        public $card_number;
        public $card_date;
        public $card_cvv;

        public function __construct($id, $amount, $card_number, $card_date, $card_cvv){
            parent::__construct($id, $amount);
            $this->card_number = $card_number;
            $this->card_date = $card_date;
            $this->card_cvv = $card_cvv;
        }
    }
?>