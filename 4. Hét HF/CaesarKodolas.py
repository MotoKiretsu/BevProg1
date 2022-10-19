def main():
    kod = "kwwsv=22|rxwx1eh2gTz7z<Zj[fT"
    buvosSzam=3
    NewKod=""
    i=0
    
    while len(kod) >i:
        NewKod+=chr(ord(kod[i])-buvosSzam)
        i+=1
    
    #Szeretném megjegyezni hogy valahogy sejtettem mi lesz a vége 
    print(f"A kód megfejtése: {NewKod}.")
    

if __name__ == "__main__":
    main()