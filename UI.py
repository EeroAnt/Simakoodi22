from Fuksikoodi22 import Kurssi, Kayttaja

    
def ohje(self):
    print("1 Näytä kurssit")    #printtaa kurssit
    print("2 Valitse kurssi")   #avaa kyseisen kurssin valikon -- kurssivalikko(kurssinnimi)
    print("3 Lisää kurssi")     # 
    print("0 Lopeta")   #
    print()

def kysely(self):
    self.ohje()
    while True:
        print("")
        komento = input("komento: ")
        if komento == "0":
            break
        elif komento == "1":
            for kurssi in kurssit:
                print(kurssi)
        elif komento == "2":
            i = 1
            for i in (1, length(kurssit)+1):
                print(f"{i}: kurssit[i-1]")
                i = i+1
            kurssinro = int(input("Anna kurssin numero, tai 0 jos haluat palata edelliseen valikkoon: "))
            if kurssinumero == 0:
                self.ohje()
            else: 
                    #siirry funktioon, jossa voi tehdä kurssiin liittyviä asioita
        elif komento == "3":
            nimi = input("Anna kurssin nimi: ")
            viikot = int(input("Anna kurssin kesto viikkoina: "))
            muuttuja = Kurssi(nimi, viikot)
            kurssivalikko(muuttuja) #kutsut valikkofunktiota
        else:
            #self.ohje()

def suorituksen_haku(): #kopioitu Githubista Ohpe-tehtävästä
    nimi = input("kurssi: ")
    suoritus = self.__luettelo.hae_suoritus(nimi)
    if suoritus == None:
        print("ei suoritusta")
    else:
        print(f"{suoritus.nimi()} ({suoritus.laajuus()} op) arvosana {suoritus.arvosana()}")

def kurssivalikko(kurssi):
    print("Valitse komento:")
    print("1: Katso tehtävän vastauksia")
    print("2: Lisää tehtävän vastaus")
    print("0: Palaa")
    komento = int(input("Valitse komento: "))
    if komento == 1:
        tehtavavalikko(kurssi)
    elif komento == 2:
        viikko = int(input("Anna viikon numero: "))
        tehtavanro = int(input("Anna tehtävän numero: "))
        Kurssi.lisaa_tehtava(viikko, tehtavanro)
        vastaus = input("Anna tehtävän vastaus: ")
        Kurssi.lisaa_vastaus()

    #kyselyjä: katso tehtävä, lisää tehtävä/vastaus

def tehtavavalikko(kurssi):
    pass
    #
 

if __name__ == "__main__":
    pass