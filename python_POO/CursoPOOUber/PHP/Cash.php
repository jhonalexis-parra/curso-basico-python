<?php
require_once("Payment.php")

    class Cash extends Payment {
        
        public function __construct($id, $amount){
            parent::__construct($id, $amount);
            
        }
}

?>