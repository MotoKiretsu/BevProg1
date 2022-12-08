def main():
    kodSzoveg="Cbcq Dgyk!\nDmeybh kce cew yrwyg hmrylyaqmr:\nrylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!\nAqmimjjyi:\nYnyb"
    ForditottKod=""
    for kod in kodSzoveg:
        if (97 <= ord(kod) and ord(kod) <=122): 
            if ord(kod)+2 > 122:
                ForditottKod+=(chr(ord(kod)+2-26))
            else:
                ForditottKod+=(chr(ord(kod)+2))   
        elif(65 <= ord(kod) and ord(kod) <=90):
            if ord(kod)+2 > 90:
                ForditottKod+=(chr(ord(kod)+2-26))
            else:
                ForditottKod+=(chr(ord(kod)+2))
        else:
            ForditottKod+=(kod)

    print(ForditottKod)

if __name__ == "__main__":
    main()