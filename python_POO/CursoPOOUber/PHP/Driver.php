<?php
require_once("Account.php");

    class Driver extends Account {
        public $id;
        public $email;
        public $password;

        public function __construct($id, $name, $document, $email, $password){
            parent::__construct($name, $document);
            $this->id = $id;
            $this->email = $email;
            $this->password = $password;
        }
    }
?>