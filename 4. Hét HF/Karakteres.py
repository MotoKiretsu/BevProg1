def Megfejtes (kod):
    KodDekodolo="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    i=0
    a=0
    while len(kod) <=i:
         while len(KodDekodolo) <=a:
            if kod[i]==KodDekodolo[a]:
                Megfejtes+=kod[i]
                break
            a+=1
    i+=1

def main():
    kod = input('Adja meg a kodolt üzenetett: \n')
    print(Megfejtes(kod))


if __name__ == "__main__":
    main()