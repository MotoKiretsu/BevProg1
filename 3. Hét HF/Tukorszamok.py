def main():
    TSz= input("Adjon meg egy tükör számot: ")
    SzamHossz=len(TSz)
    i=0
    s=0
    if(len(TSz)%2!=0):
        while i < (SzamHossz-1)/2:
            if(TSz[i]!=TSz[SzamHossz-i]):
                print("Az adott szám nem tükör szám")
                s=1
                break
        i += 1
    else:
        while i < SzamHossz/2:
            if(TSz[i]!=TSz[SzamHossz-i]):
                print("Az adott szám nem tükör szám")
                s=1
                break
        i += 1
    
    if(s==0):
        print("Az adott szám egy tükör szám")

    


if __name__ == "__main__":
    main()