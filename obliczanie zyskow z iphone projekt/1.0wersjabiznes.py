import json
import os
import random

# Sprawdzamy, czy plik z bazą w ogóle istnieje na dysku
if os.path.exists("baza.json"):
    with open("baza.json", "r") as plik:
        # Wczytujemy dane i zamieniamy tekst z powrotem na listę
        baza_telefonow = json.load(plik)
else:
    # Jeśli pliku nie ma (np. pierwsze uruchomienie), tworzymy pustą listę
    baza_telefonow = []

with open("cennik.json", "r") as plik_cennika:
    CENNIK_CEX = json.load(plik_cennika)


while True:
    wybor = int(input("""
    1.Dodaj telefon do listy    
    2.Wyswietl liste
    3.Usun telefon z listy    
    4.Wyjdz
                      
    Wybierz opcje:  """))


    if wybor == 1:
        model_input = input("\nPodaj model iPhone: ").strip()
        model = 'iPhone ' + model_input
        gb_input = input("\n Podaj pamięć iPhone : ").strip()
        gb = gb_input + 'GB'
        stan = input("\n Podaj stan iPhone A/B/C: ").strip().upper()
        kolor = input("\n Podaj kolor iPhone: ")
        cena = int(input("\nPodaj cene iPhone: "))
        
        
        cena_skupu = CENNIK_CEX[model][gb][stan]
        profit = cena_skupu - cena

        baza_telefonow.append({"model": model,"gb": gb,"stan": stan,"kolor": kolor,"cena": cena, "profit": profit} )
        print(f"\nTwoj telefon zostal pomyslnie dodany! Szacowany zys z tej sztuki to: {profit} zł")
        with open("baza.json", "w") as plik:
            json.dump(baza_telefonow, plik)

    elif wybor == 2:
        if len(baza_telefonow) == 0:
            print("\nBaza telefonow jest pusta zeby wyswietlic liste pierw dodaj jakis telefon!")
        print("\nWyswietl liste: ")
        numer = 1
        total_zysk = 0 
        for telefon in baza_telefonow:
            print(f"\n {numer} iPhone Model: {telefon['model']},| gb: {telefon['gb']},| Stan: {telefon['stan']}, | Kolor: {telefon['kolor']}, | Cena:{telefon['cena']}, | Profit:{telefon['profit']} \n ")
            numer = numer + 1 
            total_zysk = total_zysk + telefon['profit']

        print(f"Twoj profit z tych paczek wynosi: {total_zysk}")

    elif wybor == 3:
        indeks = int(input("Podaj numer telefonu do usuniecia: "))
        indeks = indeks - 1
        baza_telefonow.pop(indeks)
        with open("baza.json", "w") as plik:
            json.dump(baza_telefonow, plik)
        print("Telefon został pomyślnie usunięty z bazy!")


    elif wybor == 4:
        print("Wyjdz")
        with open("baza.json", "w") as plik:
            json.dump(baza_telefonow, plik)
        break