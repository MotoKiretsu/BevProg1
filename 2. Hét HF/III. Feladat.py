def main():
    Na= int(input("Nátrium: "))
    Cl= int(input("Klór: "))
    NaCl=0
    eNa=0
    eCl=0

    if Cl == Na/2 :
        NaCl = Na
    elif Cl > Na/2:
        NaCl = Na
        eCl=Cl-Na/2
    else:
        NaCl = Cl*2
        eNa=Na/2-Cl

    print("Keletkező konyhasó: {0},\nmaradék nátriumatom: {1},\nmaradék klóratom: {2}".format(NaCl, eNa, eCl))

if __name__ == "__main__":
    main()