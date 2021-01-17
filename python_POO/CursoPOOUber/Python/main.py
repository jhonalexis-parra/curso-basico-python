from car import Car
from account import Account
from UberX import UberX


if __name__ == "__main__":
    
    carroX = UberX("AMS234", Account("Andres Herrera", "ANDA876"), "Chevrolet", "Spark")
    print(vars(carroX))
    print(vars(carroX.driver))

#    car2 = Car()
#    car2.license = "OPS345"
#    car2.driver = "Martha"
#    print(vars(car2))
