def main():
    N= int(input("Fibonacci sorozat N. tagját: "))
    i=2
    s1=1
    s2=1
    

    if((N==1) or (N==2)):
        print("A Sorozat {0}. tagja az 1".format(N))
    else:
        while i < N:
            NewS=s1+s2
            s1=s2
            s2=NewS
            #Tesztelés szempontjábból marad itt
            #print(NewS)
        i += 1
        print("A Sorozat {0}. tagja az {1}}".format(N,NewS))

if __name__ == "__main__":
    main()