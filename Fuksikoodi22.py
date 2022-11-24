import json

class Kurssi:
    def __init__(self, nimi:str,viikkoja:int):
        self.nimi = nimi
        self.viikot = {}
        for i in range(1,viikkoja+1):
            self.viikot[i] = {}

    def listaa_viikot(self):
        for i in self.viikot:
            print(i)

    def lisaa_tehtava(self, viikko, tehtavanro):
        self.viikot[viikko][tehtavanro]=[]

    def listaa_tehtavat(self, viikkonro):
        for i in self.viikot[viikkonro]:
            print(i)

    # def lisaa_vastaus(self, viikkonro, tehtavanro, vastaus):
    #     self.viikot[viikkonro][tehtavanro].append(vastaus)

    # def listaa_vastaus(self, viikkonumero, tehtavanro):
    #     for i in self.viikot[viikkonumero][tehtavanro]:
    #         print(i)

class Kayttaja:
    def __init__(self, nimi):
        self.nimi = nimi
        self.kurssit = []
        self.tehtavat = []
        self.vastaukset = {}


    def lisaa_kurssi(self, kurssinnimi:Kurssi):
        self.kurssit.append(kurssinnimi)

    def lisaa_vastaus(self, kurssi:Kurssi, viikkonro, tehtavanro, vastaus):
        kurssi.viikot[viikkonro][tehtavanro].append(vastaus)
        self.tehtavat.append((kurssi.nimi,viikkonro,tehtavanro))
        if kurssi.nimi not in self.vastaukset.keys():
            self.vastaukset[kurssi.nimi]={}
        if viikkonro not in self.vastaukset[kurssi.nimi].keys():
            self.vastaukset[kurssi.nimi][viikkonro] = {}
        if tehtavanro not in self.vastaukset[kurssi.nimi][viikkonro]:
            self.vastaukset[kurssi.nimi][viikkonro][tehtavanro] = ""
        self.vastaukset[kurssi.nimi][viikkonro][tehtavanro] = vastaus

    def katso_vastaukset(self, kurssi:Kurssi, viikkonro, tehtavanro):
        if (kurssi.nimi,viikkonro,tehtavanro) in self.tehtavat:
            for i in kurssi.viikot[viikkonro][tehtavanro]:
                print(i)
        else:
            return False

    def __str__(self):
        return self.nimi

def tallenna_kayttaja(kayttaja:Kayttaja):
    with open("tiedot.json","r") as tiedot:
        data = json.load(tiedot)
    if kayttaja.nimi not in data["user"].keys():
        data["user"][kayttaja.nimi] = {}
    kurssien_nimet = []
    for i in kayttaja.kurssit:
        kurssien_nimet.append(i.nimi)
    data["user"][kayttaja.nimi] = [kurssien_nimet, kayttaja.tehtavat, kayttaja.vastaukset]
    with open("tiedot.json","w") as tiedot:
        json.dump(data,tiedot)

def tallenna_kurssi(kurssi:Kurssi):
    with open("tiedot.json","r") as tiedot:
        data = json.load(tiedot)
    if kurssi.nimi not in data["courses"].keys():
        data["courses"][kurssi.nimi]={}
    data["courses"][kurssi.nimi]=kurssi.viikot
    with open("tiedot.json", "w") as tiedot:
        json.dump(data, tiedot)

def start():            #palauttaa tuplen, jossa ensimmäisenä on olemassaolevat käyttäjät ja toisena olemassaolevat kurssit
    with open("tiedot.json","r") as tiedot:
        data = json.load(tiedot)
    kayttajat = []
    for i in data["user"]:
        pala = Kayttaja(i)
        kayttajat.append(pala)
        for j in data["user"][i][0]:
            pala.kurssit.append(j)
        for k in range(len(data["user"][i][1])):
            pala.tehtavat.append((data["user"][i][1][k][0],data["user"][i][1][k][1],data["user"][i][1][k][2]))
    kurssit = []
    for j in data["courses"]:
        kurssit.append(j)
    return (kayttajat,kurssit)

print(start())


# kurssi = Kurssi("Linis",6)

# kurssi.lisaa_tehtava(1,2)
# kurssi.lisaa_tehtava(1,3)
# tallenna_kurssi(kurssi)
# juuseri = Kayttaja("Eero")
# juuseri.lisaa_kurssi(kurssi)
# juuseri.lisaa_vastaus(kurssi,1,2,"oikea vastaus")
# juuseri.lisaa_vastaus(kurssi,1,3,"väärä vastaus")
# tallenna_kayttaja(juuseri)
# kurssi.listaa_tehtavat(1)
# tallenna_kurssi(kurssi)
# #  
# # with open("sample.json", "w") as outfile:
#     json.dump(dictionary, outfile)