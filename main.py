while True:
  print("""Witaj w kalkulatorze BMR
  Prosimy o wypelnienie inofrmacji""")
  print("\n")
  wzrost  = int(input("Podaj wzrost (w cm): "))
  waga = int(input("Podaj wagę (w kg): "))
  wiek = int(input("Podaj wiek: "))
  plec = str(input("Podaj plec (M lub K): "))
  #zmiana centymterow na metry
  cm_na_m = wzrost/100
  #podniesienie wzrostu do kwadratu
  wzrost_kwadrat = pow(wzrost,2)
  bmi = waga * wzrost_kwadrat
  #zaokraglanie liczb (zbyt dluga liczba)
  bmi_round = str(round(bmi,2))
  #zaokralgnie liczb (recznie)
  zaokraglanie = bmi_round[0:2] + "." + bmi_round[2:4]
  #obliczenie zapotrzebowanie kalorycznego dla kobiet
  zapotrzebowanie_k = (10 * waga) + (6.25 * wzrost) - (5* wiek) -161
  #obliczenie zapotrzebowanie kalorycznego dla mezczyzn
  zapotrzebowanie_m = (10 * waga) + (6.25 * wzrost) - (5* wiek) + 5
  

  def kategoria_bmi():
    if zaokraglanie <"16":
        print("Twoje BMR wynosi "  + zaokraglanie + ": Wyglodzenie")
      
    elif zaokraglanie >="16" and zaokraglanie <="16.99":
        print("Twoje BMR wynosi "  + zaokraglanie + ": Wychudzenie")
    
    elif zaokraglanie >="17" and zaokraglanie<="18.49":
      print("Twoje BMR wynosi "  + zaokraglanie + ": Niedowaga")
    
    elif zaokraglanie>="18.5"  and zaokraglanie<="24.99":
        print("Twoje BMR wynosi "  + zaokraglanie + ": Waga prawilowa")
    
    elif zaokraglanie>="25"  and zaokraglanie<="29.99":
      print("Twoje BMR wynosi "  + zaokraglanie + ": Otylosc")
    
    elif zaokraglanie>="30"  and zaokraglanie<="34.99":
      print("Twoje BMI wynosi "  + zaokraglanie + ": I stopien otylosci")
    
    elif zaokraglanie>="35"  and zaokraglanie<="39.99":
      print("Twoja BMR wynosi "  + zaokraglanie + ": II stopien otylosci")
    
    else:
      print("Twoja BMR wynosi "  + zaokraglanie + ": Skrajna otylosc")
    
  
  
  #wyswietlanie zapotrzebowanie kalorycznego ze wzgledu na plec
  def zapotrzebowanie():
    if plec == "M":
      print("Twoja przemiana materii wynosi " + str(zapotrzebowanie_m) + " kcal")
      print("\n")
    
    elif plec == "K":
      print("Twoja przemiana materii wynosi " + str(zapotrzebowanie_k) + " kcal")
      print("\n")
      

    

  if __name__ == "__main__":
    kategoria_bmi()
    zapotrzebowanie_k
