def main():
    Na= int(input("Nátrium: "))
    Cl= int(input("Klór: "))
    NaCl=0
    eNa=0
    eCl=0

    if Cl*2 == Na/2 :
        NaCl = Na
    elif Cl*2 > Na/2:
        NaCl = Na
        eCl=Cl*2-Na/2
    else:
        NaCl = Cl
        eNa=Na/2-Cl*2

    print(f"Keletkező konyhasó: {NaCl},\nmaradék nátriumatom: {eNa},\nmaradék klóratom: {eCl}")

if __name__ == "__main__":
    main()