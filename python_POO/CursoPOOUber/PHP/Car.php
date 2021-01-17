<?php

    require_once("Account.php");

    class Car {

        public $id;
        public $license;
        public $driver;
        public $pasenger;

        public function __constructor ($license, $driver) {
            $this->license = $license;
            $this->driver = $driver;
        }
        
        public function printDataCar () {
            echo "license: $this->license, conductor: {$this->driver->name}, document: {$this->driver->document}";
        }
    }

?>
