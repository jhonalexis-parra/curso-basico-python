def exchanges (moneda_inicial, valor_inicial, moneda_final):
    print("Calculando salida")

    if (moneda_inicial == 1) & (moneda_final == 1):
        print("Su dinero en COP es: {}".format(valor_inicial))
    if moneda_inicial == 1 & moneda_final == 2:
        print("Su dinero en Dolares es: {}".format(valor_inicial/3800))
    if moneda_inicial == 1 & moneda_final ==3:
        print("Su dinero en Dolares es: {}".format(valor_inicial/4500))
    
    if moneda_inicial == 2 & moneda_final == 1:
        print("Su dinero en COP es: {}".format(valor_inicial * 3800))
    if moneda_inicial == 2 & moneda_final == 2:
        print("Su dinero en Dolares es: {}".format(valor_inicial))
    if moneda_inicial == 2 & moneda_final ==3:
        print("Su dinero en Dolares es: {}".format(valor_inicial/1.2))

    if (moneda_inicial == 3) & (moneda_final == 1):
        print("Su dinero en COP es: {}".format(valor_inicial * 4500))
    if moneda_inicial == 3 & moneda_final == 2:
        print("Su dinero en Dolares es: {}".format(valor_inicial * 1.2))
    if moneda_inicial == 3 & moneda_final ==3:
        print("Su dinero en Dolares es: {}".format(valor_inicial))

if __name__ == '__main__':

    moneda_inicial = int(input(
            
            '''Ingresa tu tipo de moneda:
            [1] --> COP
            [2] --> DOLAR
            [3] --> EURO
            '''
        )) 
    valor_inicial = float(input(''' 

            Ingresa la cantidad de dinero que posees:        
        
        '''))

    print(valor_inicial)

    moneda_final = int(input(''' 
            Ingresa el tipo de moneda a convertir:
            [1] --> COP
            [2] --> DOLAR
            [3] --> EURO
        '''))

    exchanges(moneda_inicial, valor_inicial, moneda_final)