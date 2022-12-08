def main():
    f = open("9. Hét HF\PIVers.txt",'r')
    f2 = open("9. Hét HF\PISzam.txt",'w')
    li = f.readlines()
    Pite=""
    for x in li:
        if "nulla" in x:
            Pite+="0"

        if "egy" or "tiz" in x:
            Pite+="1"

        if "kettő" or "husz" in x:
            Pite+="2"

        if "három" or "harminc" in x:
            if "három egész" in x:
                Pite+="3,"
            elif "három" in x or "harminc" in x :
                Pite+="3"

        if "négy" or "negyven" in x:
            Pite+="4"

        if "öt" in x:
            Pite+="5"

        if "hat" in x:
            Pite+="6"

        if "hét" or "hetven" in x:
            Pite+="7"

        if "nyolc" in x:
            Pite+="8"

        if "kilenc" in x:
            Pite+="9"

    print(Pite,file=f2)
    f.close()
    f2.close()

if __name__ == "__main__":
    main()