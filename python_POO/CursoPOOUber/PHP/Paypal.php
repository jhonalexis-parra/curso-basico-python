<?php
require_once("Payment.php")

    class Paypal extends Payment {
        public $email;
        public $password;


        public function __construct ($id, $amount, $email, $password){
            parent::__construct($id,$amount);
            $this->email = $email;
            $this->password = $password;
        }
    }

?>