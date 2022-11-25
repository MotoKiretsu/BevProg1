def main():
    anagramma1= input("Adja meg a szót: ")
    anagramma2= input("Adja meg az anagrammáját: ")
    helper=anagramma2.lower()
    
    for A in range(len(anagramma1)):
        for B in range(len(helper)):
            if anagramma1[A].lower()==helper[B] and anagramma1[A]!=" ":
                helper.replace(B,"")
                break
    
    if helper==[""] or helper==[" "]:
        print(f"A(z) {anagramma1} anagrammája a(z) {anagramma2}")
    else:
        print(f"A(z) {anagramma1} nem anagrammája a(z) {anagramma2}")
    
    
if __name__ == "__main__":
    main()