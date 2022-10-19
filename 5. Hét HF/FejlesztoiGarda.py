class CegFejlesztoi:
    def __init__(self,Nev,EltoltottEvekSzama,Fizetes) -> None:
        self.Nev=Nev
        if (EltoltottEvekSzama==""):
            self.EltoltottEvekSzama=0
            self.rang="Junior"
        else:
            self.EltoltottEvekSzama=EltoltottEvekSzama
        self.Fizetes=Fizetes

    def FizetesEmeles(self):
        self.Fizetes+=10000
        print(f"Fizetés emelést kapot {self.Nev} így most már {self.Fizetes} fizetést kap.")

    def FejlesztoiEvek(self):
        self.EltoltottEvekSzama+=1
        print(f"{self.Nev} már egy újabb éve dolgozik nálunk így már {self.EltoltottEvekSzama} éve itt van velünk.")

    def Rang(self):
        if(self.EltoltottEvekSzama==0):
            self.rang="Intern"
        elif(self.EltoltottEvekSzama==1 or self.EltoltottEvekSzama==2):
            self.rang="Junior"
        elif(2<=self.EltoltottEvekSzama and self.EltoltottEvekSzama<=5):
            self.rang="Medior"
        else:
            self.rang="Senior"

        print(f"{self.Nev} fejlesztő {self.EltoltottEvekSzama} éve dolgozik a cégnél ezért {self.rang}")

def main():
    A1 = CegFejlesztoi("Lajos","",300000)

    A1.FejlesztoiEvek()
    A1.FizetesEmeles()
    A1.Rang()

if __name__ == "__main__":
    main()