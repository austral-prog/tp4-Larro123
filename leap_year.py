def leap_year():
    
    año = input("Ingresar un año:")
    año_fl = float(año)
    año_div = año_fl % 4
    año_cent = año_fl %400
    if año_div == 0 and año_cent == 0:
        print(f"El año {año} es bisiesto")
    else:
        print(f"El año {año} no es bisiesto")
        