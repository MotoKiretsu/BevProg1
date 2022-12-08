def main():
    #oldalak = input("Mely oldalakat szeretné kiníomtatni: ")
    oldalak = "1-4,7,9,11-15"
    oldalakLista=oldalak.split(",")
    NyomtatandoOldalak=[]
    for x in oldalakLista:
        try: 
            NyomtatandoOldalak.append(int(x))
        except ValueError:
            for y in range(int(x.split("-")[1])+1):
                if int(x.split("-")[0]) <= y:
                    NyomtatandoOldalak.append(y)
    
    # Már csak hogy úgy nézen ki mint a megoldás
    Szoveg=""
    for x in NyomtatandoOldalak:
        if x != max(NyomtatandoOldalak):
            Szoveg+=str(x)+","
        else:
            Szoveg+=str(x)+"."
    print(Szoveg)

if __name__ == "__main__":
    main()