from math import pi


def TT(TA,TB):
    #Téglalap területe
    TT=TA*TB
    return TT

def KT(KS):
    #Téglalap területe
    KT=KS*KS*pi
    return KT

def HT(KS,TB):
    HT=KT(KS)*TB
    return HT


def main():
    TA= int(input("Téglalap 'a' oldala: "))
    TB= int(input("Téglalap 'b' oldala: "))
    KS= int(input("Kör sugara: "))

    print("Téglalap területe : ",TT(TA,TB))
    print("Kör területe : ",KT(KS))
    print("Henger területe : ",HT(KS,TB))


if __name__ == "__main__":
    main()