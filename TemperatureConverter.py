"""
Marie-Ange Mouwakdie
Augustin Lassus
1ere1
Conversion de temperatures
11/11/20
"""
joues = True
while joues:
    valeur = float(input("Saississez la valeur de la temperature de depart: "))
    depart = input("Quelle est l'unite de la valeur entre (En majuscule):")
    arrive = input("Vers quelle unite voulez-vous convertir?")

    def ck():
        global valeur
        global arrive
        if valeur < -273.15:
            print("Cette valeur ne peut pas etre convertit en Kelvin.")
        else:
            valeur += 273.15
            print(valeur, arrive)
        
            
    def cf():
        global valeur
        global arrive
        valeur = 9*(valeur / 5) + 32
        print(valeur, arrive)
        

    def kc():
        global valeur
        global arrive
        if valeur < 0:
            print("La valeur Minimale du Kelvin est 0")
            return
        valeur -= 273.15
        print(round(valeur, 2), arrive)

        

    def kf():
        global valeur
        global arrive
        if valeur < 0:
            print("La valeur Minimale du Kelvin est 0")
            return
        valeur = valeur * (9/5) - 459.67
        print(round(valeur, 2), arrive)
        

    def fc():
        global valeur
        global arrive
        valeur = (valeur - 32) * 5/9
        print(round(valeur, 2), arrive)
        
    
    def fk():
        global valeur
        global arrive
        valeur = (valeur - 32) * 5/9 + 273.15
        print(round(valeur, 2), arrive)
        

    if depart == arrive:
        print(valeur, arrive)


    if depart == "C" and arrive == "K":
        ck()
        
    if depart == "C" and arrive == "F":
        cf()
        
    if depart == "K" and arrive == "C":
        kc()
        
    if depart == "K" and arrive == "F":
        kf()
        
    if depart == "F" and arrive == "C":
        fc()
        
    if depart == "F" and arrive == "K":
        fk()

    joues = input("Souhaitez vous relancer?")
    if joues == "Non":
        joues = False


        




     
