Phone1 = float(input("Hoeveel kost de IPhone? "))
Phone2 = float(input("Hoeveel kost de Galaxy? "))
Difference = 0

if Phone1 > Phone2:
    print("De Iphone is het duurst, de telefoon kost: " + str(Phone1) + " Euro.")
    print("De Galaxy is het goedkoopst, de telefoon kost: " + str(Phone2) + " Euro.")
    Difference = Phone1 - Phone2
    if Difference > 50:
        print("Koop de Galaxy. De Iphone is " + str(Difference) + " euro duurder.")
    else:
        print("Koop de IPhone. De Iphone is maar " + str(Difference) + " euro duurder.")
if Phone1 < Phone2:
    print("De Galaxy is het duurst, de telefoon kost: " + str(Phone2) + " Euro.")
    print("De IPhone is het goedkoopst, de telefoon kost: " + str(Phone1) + " Euro.")
    print("Koop de Iphone. De Iphone is " + str(Difference) + " euro goedkoper.")
if Phone1 == Phone2:
    print("Koop de IPhone. Ze zijn beide even duur.")
if Phone1 > 900: