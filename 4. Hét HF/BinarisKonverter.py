


def main():
    Dec = int(input('Adja meg az adot számot amelyet Binárisra szeretne alakítani: \n'))
    FBinar="" 
    Binar=""

    while 0 != Dec:
        if Dec%2==0:
            FBinar+="0"
            Dec=Dec/2
        else:
            FBinar+="1"
            Dec-=1
            Dec=Dec/2
            
    Helper=len(FBinar)-1

    while Helper!=0:
        Binar+=FBinar[Helper]
        Helper-=1

    print(Binar)
            


if __name__ == "__main__":
    main()