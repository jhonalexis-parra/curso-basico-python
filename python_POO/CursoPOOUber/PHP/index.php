<?php

    require_once("Car.php");
    require_once("UberX.php");
    require_once("UberPool.php");
    require_once("Account.php");

    $uberX = new UberX("AWS234",  new Account("Andres Herrera", "1234567890"), "Chevrolet", "Spark");
    $uberX->printDataCar();

    $uberPool = new UberPool("GCC675", new Account("Andrea Herrera", "9876543210"), "Chevrolet", "Sail");
    $uberPool->printDataCar();
?>